import os, os.path
import shutil
import glob

from cffi import FFI


current_directory = os.path.dirname(__file__)
src_directory = os.path.abspath(os.path.join(current_directory, '..', 'src'))

package = 'cffitest'
api_header_name = 'api.h'

installation_api_header_path = os.path.join(src_directory, api_header_name)
runtime_api_header_path = os.path.join(current_directory, api_header_name)


def compile_library(installation=False):

    if installation:
        api_header_path = installation_api_header_path
        sources = glob.glob(os.path.join(src_directory, '*.c'))
        include_dirs = [src_directory]
    else:
        api_header_path = runtime_api_header_path
        sources = []
        include_dirs = []

    api_header = open(api_header_path).read()

    ffi = FFI()
    ffi.cdef(api_header)
    print("Compiling with", sources)
    lib = ffi.verify(
        api_header,
        ext_package=package,
        sources=sources,
        include_dirs=include_dirs)
    return ffi, lib


def create_api_header():
    shutil.copyfile(installation_api_header_path, runtime_api_header_path)
    return [api_header_name]


def get_library_closure():
    lib = [None]
    def get_lib():
        if lib[0] is None:
            _, _lib = compile_library()
            lib[0] = _lib
        return lib[0]
    return get_lib

get_library = get_library_closure()


def get_extension():
    ffi, _ = compile_library(installation=True)
    return ffi.verifier.get_extension()
