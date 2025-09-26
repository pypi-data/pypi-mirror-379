


def walk(node, source_code:str, symbol_table: dict, declared_table: dict, used_table: dict, is_global_var, ignored_lines, ignored_blocks) -> list[dict]:

    violations = []

    ignored_line_nums  = {il["line"] - 1 for il in ignored_lines}
    ignored_block_nums = {ib["line"] - 1 for ib in ignored_blocks}

    if node.start_point[0] in ignored_block_nums:
        
        return violations  

    if node.start_point[0] not in ignored_line_nums:
        # Check for banned functions including new and delete
        if node.type == "call_expression":
            violations += check_banned_funcs(node, source_code)


        # Ban delete and new
        elif node.type == "new_expression":
            violations.append({
                "line": node.start_point[0] + 1,
                "function": "new",
                "message": "Usage of 'new' is banned. Use static or stack allocation instead."
            })


        elif node.type == "delete_expression":
            violations.append({
                "line": node.start_point[0] + 1,
                "function": "delete",
                "message": "Usage of 'delete' is banned. Use RAII or static allocation instead."
            })

        #Check for misuse of switch statements
        elif node.type == "switch_statement":
            violations += check_switch_statement(node, source_code)

        #Ban goto
        elif node.type == "goto":
            violations.append({
                "line": node.start_point[0] + 1,
                "message": "Usage of 'goto' and any uncontrolled jumps are banned."
            })
        
        #Ban function-like macros
        elif node.type == "preproc_function_def":
            violations.append({
                "line": node.start_point[0] + 1,
                "message": "Definition of function-like macros are banned. Consider using 'inline'."
            })
    

        for child in node.children:
            violations += walk(child, source_code, symbol_table, declared_table, used_table, is_global_var,
                               ignored_lines, ignored_blocks)
            

    return violations


# CHECKS


def check_banned_funcs(node, source_code: str) -> list[dict]:
    """
    Ensures function call is not banned. Unsafe functions are defined as those who either dynamically allocate memory or
    have the potential to cause overflow. 
    """

    banned_functions = {
        "malloc", "calloc", "realloc", "free",
        "printf", "sprintf", "scanf", "gets", "fgets",
        "rand", "srand", "time", "clock", "gettimeofday",
        "system", "fork", "exec", "exit",
        "va_start", "va_arg", "va_end",
        "cin", "cout", "cerr"
    }

    violations = []

    function_node = node.child_by_field_name('function')
    if function_node is not None:
        name = source_code[function_node.start_byte:function_node.end_byte].decode("utf-8")

        if '::' in name:
            name = name.split('::')[-1]
        
        
        if name in banned_functions:
            violations.append({
                "line": node.start_point[0] + 1,
                "function": name,
                "message": f"Usage of function '{name}' is banned. Please use safer alternative."
            })
    return violations

#Ban unsafe switch statement practices
def check_switch_statement(node, source_code: str) -> list[dict]:
    violations = []

    has_default = False

    for child in node.named_children:
        if child.type in {"default_label", "default_statement", "default"}:
            has_default = True

        def walk_switch_subtree(n):
            nonlocal has_default, violations
            if n.type in {"default_label", "default_statement", "default"}:
                has_default = True

            elif n.type in {"break_statement", "continue_statement"}:
                violations += check_break_continue_in_switch(n, source_code)

            for child in n.children:
                walk_switch_subtree(child)

    walk_switch_subtree(node)

    # Check for fallthrough
    children = [child for child in node.child_by_field_name("body").children if child.type not in {'{', '}'}]
    current_label = None
    current_block = []

    for child in children:
        if child.type in {"case_statement", "default_statement"}:
            if current_label is not None:
                if not block_has_terminator_or_fallthrough_comment(current_block, source_code):
                    violations.append({
                        "line": current_label.start_point[0] + 1,
                        "message": f"Case falls through implicitly. Add 'break;', 'return;', or comment like '/* fallthrough */'."
                    })
            current_label = child
            current_block = []
        else:
            current_block.append(child)

    if not has_default:
        violations.append({
            "line": node.start_point[0] + 1,
            "message": "Switch statement missing 'default' case."
        })

    return violations

# Check to make sure we are not using break or continue in standalone switch cases. danger of undefined logic
def check_break_continue_in_switch(node, source_code: str) -> list[dict]:
    violations = []
    current = node.parent

    # Find enclosing control structures
    inside_loop = False
    inside_switch = False

    while current:
        if current.type in {"for_statement", "while_statement", "do_statement"}:
            inside_loop = True
        if current.type == "switch_statement":
            inside_switch = True
            break
        current = current.parent
    if node.type == "break_statement":
        # 'break' is allowed in switch and loop — do not warn
        pass

    return violations


# Helper function to detect fallthrough comment to allow for fallthrough
def block_has_terminator_or_fallthrough_comment(stmts, source_code: str) -> bool:
    for stmt in reversed(stmts):
        text = source_code[stmt.start_byte:stmt.end_byte].decode("utf-8").strip()

        if stmt.type in {"break_statement", "return_statement", "throw_statement"}:
            return True
        if "fallthrough" in text.lower():
            return True
        if stmt.type != "comment":
            break  # hit a code statement that's not a terminator
    return False