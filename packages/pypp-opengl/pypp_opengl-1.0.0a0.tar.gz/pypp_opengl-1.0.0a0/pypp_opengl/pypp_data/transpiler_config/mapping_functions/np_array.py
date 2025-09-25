import ast


def mapping_fn(node: ast.Call, d: Deps) -> str:
    assert len(node.args) > 0, "Need at least one arg for np.array"
    return f"{d.handle_expr(node.args[0])}.data_ref().data()"
