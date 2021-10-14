#pythran export centered1d(float[])
def centered1d(x):
    return (x[1:] + x[:-1]) / 2.