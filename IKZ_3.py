import math as m


eps = 10 ** (-3)
n = 1
Fi = (m.sqrt(5) - 1) / 2
data = []


def F(x, y):
    return x ** 2 + y ** 2 - 10 * x - 15 * y


def L1(x, y):
    return 5 * x + 13 * y - 51


def L2(x, y):
    return 15 * x - 7 * y - 107


def set_positive(L):
    return L if (L > 0) else 0


def Fine_Function(x, y):
    return F(x, y) + 100 * n * (set_positive(L1(x, y)) ** 2+set_positive(L2(x, y)) ** 2)


def dxFF(x, y):
    d = 10 ** (-6)
    return (Fine_Function(x + d, y) - Fine_Function(x - d, y)) / (2 * d)


def dyFF(x, y):
    d = 10 ** (-6)
    return (Fine_Function(x, y + d) - Fine_Function(x, y - d)) / (2 * d)


def golden_ratio_for_h(x, y):
    a = 0
    b = 1
    h1 = 0
    h2 = 0
    k = 0
    x1, x2, y1, y2 = 0, 3, 0, 3
    while abs((b - a)) > eps:
        h1 = a - (Fi - 1) * (b - a)
        h2 = a + Fi * (b - a)
        x1 = x - h1 * dxFF(x, y)
        y1 = y - h1 * dyFF(x, y)
        x2 = x - h2 * dxFF(x, y)
        y2 = y - h2 * dyFF(x, y)
        if Fine_Function(x1, y1) < Fine_Function(x2, y2):
            b = h2
        else:
            a = h1
        k += 1
    if Fine_Function(x1, y1) < Fine_Function(x2, y2):
        return h1
    else:
        return h2


def fastest_descent(x, y):
    xk = -1
    yk = 4
    while m.sqrt((xk - x) ** 2 + (yk - y) ** 2) > eps:
        x = xk
        y = yk
        h = golden_ratio_for_h(x, y)
        xk = x - h * dxFF(x, y)
        yk = y - h * dyFF(x, y)
    return xk, yk


def penalty_function_method():
    x1 = -10
    y1 = 0
    x2 = 0
    y2 = 1
    global n

    while ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 > eps:
        x1 = x2
        y1 = y2
        x2, y2 = fastest_descent(x1, y1)
        data.append([n, x2, y2])
        n += 1

    return x2, y2


penalty_function_method()
print(f'penalty_function_method = {data[-1]}')
