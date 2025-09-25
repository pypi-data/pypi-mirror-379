import ast


def mapping_fn(node: ast.Call, d: Deps) -> str:
    return "gladLoadGL(glfwGetProcAddress)"
