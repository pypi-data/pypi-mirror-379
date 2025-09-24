__all__ = ["lib", "ffi"]

import os
from .ffi import ffi

lib = ffi.dlopen(os.path.join(os.path.dirname(__file__), 'libpython_slugify_pi.so'))
del os
