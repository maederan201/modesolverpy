#pythran export centered1d(float[])
def centered1d(x):
    return (x[1:] + x[:-1]) / 2.

#pythran export centered2d(complex128[][])
#pythran export centered2d(float64[][])
def centered2d(x):
    return (x[1:, 1:] + x[1:, :-1] + x[:-1, 1:] + x[:-1, :-1]) / 4.
    

