# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    x = int(x)
    y = int(y)
    if 0 <= x <= 100 and 0 <= y <= 100:
        a = [x, y]
        return sum(a)
    else:
        return "Error - please check the numbers are integers between 0 and 100"
    #raise NotImplementedError()
