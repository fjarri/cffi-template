#include "api.h"
#include "shared.h"

int cfunc1()
{
    return VAL1;
}


int cfunc3()
{
    return cfunc2() + 1;
}
