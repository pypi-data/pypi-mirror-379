import ast


def mapping_fn(_node: ast.Attribute, _d, res_str: str):
    attr_str: str = res_str.split(".")[-1]
    if attr_str.isupper():
        return f"GLFW_{attr_str}"
    return res_str
