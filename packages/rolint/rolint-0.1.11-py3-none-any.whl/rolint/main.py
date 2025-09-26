from pathlib import Path
from collections import defaultdict
from rolint.parser import parser as parser_module
from rolint.rules import c_rules
from rolint.rules.python_rules import run_python_linter
from rolint.rules import cpp_rules
import sys
from rolint.rules import override
from rolint.reporter.json import report_json
from rolint.rules.struct_table_builder import build_struct_table


EXTENSION_MAP = {
    ".c": "c",
    ".h": "c",
    ".cpp": "cpp",
    ".cc": "cpp",
    ".cxx": "cpp",
    ".hpp": "cpp",
    ".hxx": "cpp",
    ".py": "python"
}

def detect_language(path: Path) -> str:
    return EXTENSION_MAP.get(path.suffix.lower(), None)

def collect_files(base_path: Path) -> dict[str, list[Path]]:
    lang_files = defaultdict(list)
    for file_path in base_path.rglob("*"):
        if file_path.is_file():
            lang = detect_language(file_path)
            if lang:
                lang_files[lang].append(file_path)
    return lang_files

def run_linter(path: Path, lang: str = None, output_format: str = "text", output_path: Path = None):

    violations = []
    ignored_lines = []
    ignored_blocks = []
    if path.is_dir():
        lang_to_files = collect_files(path)
        if not lang_to_files:
            print("ERROR: No source files found.")
            return
        for lang, files in lang_to_files.items():
            print(f"\n🔧 Linting {len(files)} {lang.upper()} file(s):")
            for f in files:
                print(f"  - {f}")
                
                v, il, ib = run_file_lint(f, lang)
                violations.extend(v)
                ignored_lines.extend(il or [])
                ignored_blocks.extend(ib or [])
        
        #Exit with status 1 code if there are violations to prevent commit
        if violations:
            if output_format == "json":
                report_json(violations, ignored_lines, ignored_blocks, output_path=output_path)
                print(f"📄 Output at {output_path}")
            print("Blocking Commit.")
            print(" - John 8:11")
            sys.exit(1)
        else:
            sys.exit(0)

    elif path.is_file():
        inferred_lang = lang or detect_language(path)
        if not inferred_lang:
            print(f"⚠️ Could not detect language for {path}")
            return

        print(f"🔍 Linting: {path}")
        print(f"🌐 Language: {inferred_lang}")
        print(f"📤 Output format: {output_format}")

        v, il, ib = run_file_lint(path, inferred_lang)  # ← capture

        violations.extend(v)
        ignored_lines.extend(il or [])
        ignored_blocks.extend(ib or [])
        

        if violations:
            if output_format == "json":
                report_json(violations, ignored_lines, ignored_blocks, output_path=output_path)  # ← keyword
                if output_path:
                    print(f"📄 Output at {output_path}")
            print("Blocking commit.")
            print(" - John 8:11")
            sys.exit(1)
        else:
            sys.exit(0)


def run_file_lint(file_path: Path, lang: str):
    violations = []
    ignored_lines = []
    ignored_blocks = []


    if lang == "c":
        tree, source = parser_module.parse_file(file_path, lang)
        ## Tables for tracking variable contexts.
        symbol_table = {}
        declared_table = {
            "variables": {}, 
            "functions": {}
        }
        used_table = {
            "variables": set(),
            "functions": set()
        }
        global_struct_table = build_struct_table(tree.root_node, source)

        ignored_lines, ignored_blocks = override.detect_override_lines(source)


        if file_path.suffix in {".h"}:
            violations += c_rules.check_header_guard(source, str(file_path))
            violations += c_rules.check_object_definitions_in_header(tree, source)
        else:
            violations += c_rules.walk(tree.root_node, source, symbol_table, declared_table, used_table, global_struct_table,
                                        is_global_var=True, ignored_lines=ignored_lines, ignored_blocks=ignored_blocks)
            violations += c_rules.check_recursion(tree.root_node, source)
            violations += c_rules.check_unused(declared_table, used_table)
        
        if violations:
            for v in violations:
                v["file"] = str(file_path)
                print(f"🚫 VIOLATION: {file_path}:{v['line']} - {v['message']}")

        if ignored_blocks or ignored_lines:
            for il in ignored_lines:
                il["file"] = str(file_path)
                print(f"⚠️  FLAG: {file_path} - Line ignored or overridden at line {il['line']}")
            for il in ignored_blocks:
                il["file"] = str(file_path)
                print(f"⚠️  FLAG: {file_path} - Line ignored or overridden at block {il['line']}")

        
        

    elif lang in {"cpp"}:
        tree, source = parser_module.parse_file(file_path, lang)
        ## Tables for tracking variable contexts.
        symbol_table = {}
        declared_table = {
            "variables": {}, 
            "functions": {}
        }
        used_table = {
            "variables": set(),
            "functions": set()
        }

        ignored_lines, ignored_blocks = override.detect_override_lines(source)

        violations += cpp_rules.walk(tree.root_node, source, symbol_table, declared_table, used_table, is_global_var=True,
                                     ignored_lines=ignored_lines, ignored_blocks=ignored_blocks)

        if violations:
            for v in violations:
                v["file"] = str(file_path)
                print(f"🚫 VIOLATION: {file_path}:{v['line']} - {v['message']}")

        if ignored_blocks or ignored_lines:
            for il in ignored_lines:
                il["file"] = str(file_path)
                print(f"⚠️  FLAG: {file_path} - Line ignored or overridden at line {il['line']}")
            for il in ignored_blocks:
                il["file"] = str(file_path)
                print(f"⚠️  FLAG: {file_path} - Line ignored or overridden at block {il['line']}")


    elif lang in {"python"}:
        source = file_path.read_text(encoding="utf-8")
        ignored_lines, ignored_blocks = override.detect_py_overrides(source)
        

        violations += run_python_linter(file_path, ignored_lines, ignored_blocks)
        
        if violations:
            for v in violations:
                v["file"] = str(file_path)
                print(f"🚫 VIOLATION: {file_path}:{v['line']}: {v['message']}")
        
        if ignored_blocks or ignored_lines:
            for il in ignored_lines:
                il["file"] = str(file_path)
                print(f"⚠️  FLAG: {file_path} - Line ignored or overridden at line {il['line']}")
            for il in ignored_blocks:
                il["file"] = str(file_path)
                print(f"⚠️  FLAG: {file_path} - Line ignored or overridden at block {il['line']}")
    else:
        print(f"⚠️ Unknown language: {lang}")
    

    return violations, ignored_lines, ignored_blocks
