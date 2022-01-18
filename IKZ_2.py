import math as m

eps = 10**(-6)
Fi = (m.sqrt(5)-1)/2
data21 = []
data22 = []
data31 = []
data32 = []


def J1(x, y):
    return 3*x**2-3*x*y+4*y**2-2*x+y


def dxJ1(x, y):
    return 6*x-3*y-2


def dyJ1(x, y):
    return 8*y-3*x+1


def J2(x, y, z):
    return 3*x**2+4*y**2+5*z**2+2*x*y-x*z-2*y*z+x-3*z


def dxJ2(x, y, z):
    return 6*x+2*y-z+1


def dуJ2(x, y, z):
    return 8*y+2*x-2*z


def dzJ2(x, y, z):
    return 10*z-x-2*y-3


def golden_ratio_for_h2(x, y):
    a = 0
    b = 1
    n = 1
    h1 = 0
    h2 = 0
    while abs((Fi ** n) * (b - a)) > eps:
        h1 = a - (Fi - 1) * (b - a)
        h2 = a + Fi * (b - a)

        x1 = x - h1 * dxJ1(x, y)
        y1 = y - h1 * dyJ1(x, y)
        x2 = x - h2 * dxJ1(x, y)
        y2 = y - h2 * dyJ1(x, y)
        if J1(x1, y1) < J1(x2, y2):
            b = h2
        else:
            a = h1
        n += 1
    if J1(x1, y1) < J1(x2, y2):
        return h1
    else:
        return h2


def fastest_descent2():
    '''
    Для двух переменных
    '''
    x = -4.0
    y = 4.0
    xk = -2.0
    yk = 2.0
    n = 0
    while ((xk - x) ** 2 + (yk - y) ** 2) ** 0.5 > eps:
        x = xk
        y = yk
        h = golden_ratio_for_h2(x, y)
        xk = x - h * dxJ1(x, y)
        #         h = golden_ratio_for_h(xk, y)
        yk = y - h * dyJ1(xk, y)
        n += 1
        data21.append([n, xk, yk])
    return xk, yk


def golden_ratio_for_h3(x, y, z):
    a = 0
    b = 1
    n = 1
    h1 = 0
    h2 = 0
    while abs((Fi ** n) * (b - a)) > eps:
        h1 = a - (Fi - 1) * (b - a)
        h2 = a + Fi * (b - a)

        x1 = x - h1 * dxJ2(x, y, z)
        y1 = y - h1 * dуJ2(x, y, z)
        z1 = z - h1 * dzJ2(x, y, z)
        x2 = x - h2 * dxJ2(x, y, z)
        y2 = y - h2 * dуJ2(x, y, z)
        z2 = z - h2 * dzJ2(x, y, z)
        if J2(x1, y1, z1) < J2(x2, y2, z2):
            b = h2
        else:
            a = h1
        n += 1
    if J2(x1, y1, z1) < J2(x2, y2, z2):
        return h1
    else:
        return h2


def fastest_descent3():
    '''для трёх переменных'''
    x = -4.0
    y = 4.0
    z = 6.0
    xk = -2.0
    yk = 2.0
    zk = 3.0
    h = 1.0
    n = 0
    while ((xk - x) ** 2 + (yk - y) ** 2 + (zk - z) ** 2) ** 0.5 > eps:
        x = xk
        y = yk
        z = zk
        h = golden_ratio_for_h3(x, y, z)
        xk = x - h * dxJ2(x, y, z)
        #         h = golden_ratio_for_h(xk, y)
        yk = y - h * dуJ2(xk, y, z)
        zk = z - h * dzJ2(xk, yk, z)
        n += 1
        data31.append([n, xk, yk, zk])
    return xk, yk, zk


def exploratory_search_x2(x, y, h):
    basisVal = J1(x, y)

    xk1 = x + h
    xk2 = x - h

    if J1(xk1, y) < basisVal:
        return xk1
    elif J1(xk2, y) < basisVal:
        return xk2
    else:
        return x


def exploratory_search_y2(x, y, h):
    basisVal = J1(x, y)

    yk1 = y + h
    yk2 = y - h

    if J1(x, yk1) < basisVal:
        return yk1
    elif J1(x, yk2) < basisVal:
        return yk2
    else:
        return y


def search_for_example2(v, vk):
    return v + 2 * (vk - v)


def analyse_basis2(x, y, h):
    basisVal = J1(x, y)

    xk = exploratory_search_x2(x, y, h)
    xk = search_for_example2(x, xk)
    if J1(xk, y) < basisVal:
        x = xk

    yk = exploratory_search_y2(x, y, h)
    yk = search_for_example2(y, yk)
    if J1(x, yk) < basisVal:
        y = yk

    return x, y


def hook_jeeves2():
    x, y = -4, 4
    n = 0
    h = 0.1
    while h > eps:
        xk, yk = analyse_basis2(x, y, h)
        data22.append([n, x, y])
        if x == xk and y == yk:
            h = h / 10
        else:
            x, y = xk, yk
        n += 1
    return x, y


def exploratory_search_x3(x, y, z, h):
    basisVal = J2(x, y, z)

    xk1 = x + h
    xk2 = x - h
    if J2(xk1, y, z) < basisVal:
        return xk1
    elif J2(xk2, y, z) < basisVal:
        return xk2
    else:
        return x


def exploratory_search_y3(x, y, z, h):
    basisVal = J2(x, y, z)

    yk1 = y + h
    yk2 = y - h
    if J2(x, yk1, z) < basisVal:
        return yk1
    elif J2(x, yk2, z) < basisVal:
        return yk2
    else:
        return y


def exploratory_search_z3(x, y, z, h):
    basisVal = J2(x, y, z)

    zk1 = z + h
    zk2 = z - h
    if J2(x, y, zk1) < basisVal:
        return zk1
    elif J2(x, y, zk2) < basisVal:
        return zk2
    else:
        return z


def search_for_example3(v, vk):
    return v + 2 * (vk - v)


def analyse_basis3(x, y, z, h):
    basisVal = J2(x, y, z)

    xk = exploratory_search_x3(x, y, z, h)
    xk = search_for_example3(x, xk)
    if J2(xk, y, z) < basisVal:
        x = xk

    yk = exploratory_search_y3(x, y, z, h)
    yk = search_for_example3(y, yk)
    if J2(x, yk, z) < basisVal:
        y = yk

    zk = exploratory_search_z3(x, y, z, h)
    zk = search_for_example3(z, zk)
    if J2(x, y, zk) < basisVal:
        z = zk

    return x, y, z


def hook_jeeves3():
    x, y, z = -4, 4, 4
    n = 1
    h = 0.1
    while h > eps:
        xk, yk, zk = analyse_basis3(x, y, z, h)
        data32.append([n, x, y, z])
        if x == xk and y == yk and z == zk:
            h = h / 10
        else:
            x, y, z = xk, yk, zk
        n += 1
    return x, y, z


fastest_descent2()
fastest_descent3()
hook_jeeves2()
hook_jeeves3()
print(f'fastest_descent2 = {data21[-1]}')
print(f'fastest_descent3 = {data31[-1]}')
print(f'hook_jeeves2 = {data22[-1]}')
print(f'hook_jeeves3 = {data32[-1]}')

