import ast


def mapping_fn(node: ast.Call, d: Deps, name_str: str) -> str:
    return name_str.split(".")[1]
