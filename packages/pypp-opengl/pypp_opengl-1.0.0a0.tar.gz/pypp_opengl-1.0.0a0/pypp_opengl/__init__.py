import OpenGL.GL as GL
import numpy as np
from .custom import (
    gl_gen_buffer,
    gl_gen_buffers,
    gl_delete_buffer,
    gl_gen_vertex_array,
    gl_gen_vertex_arrays,
    gl_delete_vertex_array,
    gl_delete_vertex_arrays,
    gl_shader_source,
    gl_shader_sources,
    gl_get_shader_iv,
    gl_get_program_iv,
    gl_get_shader_info_log,
    gl_get_program_info_log,
)
from .glad_loader import glad_load_gl


__all__ = [
    "GL",
    "np",
    "gl_gen_buffer",
    "gl_gen_buffers",
    "gl_delete_buffer",
    "gl_gen_vertex_array",
    "gl_gen_vertex_arrays",
    "gl_delete_vertex_array",
    "gl_delete_vertex_arrays",
    "gl_shader_source",
    "gl_shader_sources",
    "gl_get_shader_iv",
    "gl_get_program_iv",
    "gl_get_shader_info_log",
    "gl_get_program_info_log",
    "glad_load_gl",
]
