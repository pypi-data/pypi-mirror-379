import ast


def mapping_fn(node: ast.Call, d: Deps, caller_str: str) -> str:
    a: list[str] = caller_str.split(".")
    assert len(a) == 2, f"more than one dot found in {caller_str}"
    fn_camel_case: str = "".join(x.capitalize() for x in a[1].split("_") if x)
    args_str: str = d.handle_exprs(node.args)
    return f"glfw{fn_camel_case}({args_str})"
