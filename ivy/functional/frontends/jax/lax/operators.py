# global
import ivy


def add(x, y):
    return ivy.add(x, y)


add.unsupported_dtypes = {"torch": ("float16", "bfloat16")}


def tan(x):
    return ivy.tan(x)


tan.unsupported_dtypes = {"torch": ("float16", "bfloat16")}


def concatenate(operands, dimension):
    return ivy.concat(operands, dimension)


def full(shape, fill_value, dtype=None):
    return ivy.full(shape, fill_value, dtype=dtype)


full.unsupported_dtypes = {"torch": ("float16", "bfloat16")}


def sqrt(x):
    return ivy.sqrt(x)
     

sqrt.unsupported_dtypes = {"torch": ("float16", "bfloat16")}


def qr(x, *, full_matrices=True):
    return ivy.qr(x, "complete" if full_matrices else "reduced")


qr.unsupported_dtypes=("float16",)