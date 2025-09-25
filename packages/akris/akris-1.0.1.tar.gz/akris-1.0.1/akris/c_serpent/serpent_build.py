import os
from cffi import FFI

ffibuilder = FFI()
# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("""
    void                serpent_init      (uint8_t *skey,uint8_t const *key,size_t key_size);
    void                serpent_cbc_ciph  (uint8_t const *skey,uint8_t *dst,uint8_t const *src,size_t size);
    void                serpent_cbc_deciph(uint8_t const *skey,uint8_t *dst,uint8_t const *src,size_t size);
""")

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
base_dir = os.path.dirname(__file__)
ffibuilder.set_source(
    "_serpent_cffi",
    """
        #include "lib/serpent.h"
        #include "crypto.h"
    """,
    sources=[
        os.path.join(base_dir, "lib/serpent.c"),
        os.path.join(base_dir, "c_serpent.c")
    ],
    include_dirs=[os.path.join(base_dir, "lib"), base_dir],
) # library name, for the linker

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
