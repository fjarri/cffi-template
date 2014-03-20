from cffitest._wrapper import get_library


def cfunc1():
    lib = get_library()
    return lib.cfunc1()


def cfunc2():
    lib = get_library()
    return lib.cfunc2()


def cfunc3():
    lib = get_library()
    return lib.cfunc2()
