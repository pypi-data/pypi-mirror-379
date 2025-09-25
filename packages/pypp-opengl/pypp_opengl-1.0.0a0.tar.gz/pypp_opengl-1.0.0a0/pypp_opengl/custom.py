from OpenGL.GL import (
    glGenBuffers,
    glGenVertexArrays,
    GLuint,
    glShaderSource,
    GLenum,
    glGetShaderiv,
    glGetProgramiv,
    glGetShaderInfoLog,
    glGetProgramInfoLog,
    glDeleteBuffers,
    glDeleteVertexArrays,
)


def gl_gen_buffer() -> GLuint:
    return glGenBuffers(1)


def gl_gen_buffers(n: int) -> list[GLuint]:
    return glGenBuffers(n)


def gl_delete_buffer(buffer: GLuint):
    glDeleteBuffers(1, [buffer])


def gl_gen_vertex_array() -> GLuint:
    return glGenVertexArrays(1)


def gl_gen_vertex_arrays(n: int) -> list[GLuint]:
    return glGenVertexArrays(n)


def gl_delete_vertex_array(array: GLuint):
    glDeleteVertexArrays(1, [array])


def gl_delete_vertex_arrays(arrays: list[GLuint]):
    glDeleteVertexArrays(len(arrays), arrays)


def gl_shader_source(shader: GLuint, source: str):
    glShaderSource(shader, source)


def gl_shader_sources(shader: GLuint, sources: list[str]):
    glShaderSource(shader, sources)


def gl_get_shader_iv(shader: GLuint, pname: GLenum) -> int:
    return glGetShaderiv(shader, pname)


def gl_get_program_iv(program: GLuint, pname: GLenum) -> int:
    return glGetProgramiv(program, pname)


def gl_get_shader_info_log(shader: GLuint) -> str:
    return glGetShaderInfoLog(shader)


def gl_get_program_info_log(program: GLuint) -> str:
    return glGetProgramInfoLog(program)
