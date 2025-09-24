import ast


def _calc_type_for_special_default_dict(arg1: ast.expr) -> str | None:
    if isinstance(arg1, ast.Name):
        value_type = arg1.id
        if value_type in {"int", "float", "str", "bool"}:
            return value_type
    elif isinstance(arg1, ast.Subscript):
        if isinstance(arg1.value, ast.Name):
            value_type = arg1.value.id
            if value_type in {"list", "dict", "set"}:
                return value_type
    return None


def good_default_dict(node: ast.Call, d, caller_str: str) -> str:
    if len(node.args) == 0:
        d.value_err("defaultdict must be called with at least one argument", node)
    value_type = _calc_type_for_special_default_dict(node.args[0])
    if value_type is not None:
        arg = ""
        if len(node.args) > 1:
            arg = d.handle_expr(node.args[1])
        return f"{caller_str}::{value_type}_factory({arg})"
    args_str = d.handle_exprs(node.args)
    return f"{caller_str}({args_str})"
