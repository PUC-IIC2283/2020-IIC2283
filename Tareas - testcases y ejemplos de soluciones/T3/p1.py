INF = 1e19

def mod(x, m):
    x %= m
    return x+m if x < 0 else x

def gcdext(a, b):
    r2, x2, y2 = a, 1, 0
    r1, x1, y1 = b, 0, 1
    while r1 > 0:
        q = r2 // r1
        r0 = r2 % r1
        x0 = x2 - q * x1
        y0 = y2 - q * y1
        r2, x2, y2 = r1, x1, y1
        r1, x1, y1 = r0, x0, y0
    g, x, y = r2, x2, y2
    if g < 0: g, x, y = -g, -x, -y
    return g, x, y

def lincongeq(a, b, m):
    a = mod(a,m)
    b = mod(b,m)
    g, s, t = gcdext(a,m)
    if b % g == 0:
        bb = b//g
        mm = m//g
        n = -s*bb//mm
        x = s*bb + n*mm
        if x < 0: x += mm
        return (True, x)
    return False

def main():
    w, h, x0, y0, vx, vy = map(int, input().split())
    t_min = INF
    if vx != 0:
        if vx > 0:
            hsteps20 = 2*w-x0
            hsteps2w = w-x0
        else:
            hsteps20 = x0
            hsteps2w = x0+w
        # 1) x = x0 + 2wk + hsteps20 = 0 (mod 2w)
        # ----------------------------------------
        # 1.1) y0 + vy*(2wk + hsteps20) = 0 (mod 2h)
        # => (vy*2w) * k = -y0 - vy*hsteps20 (mod 2h)
        a = vy*2*w
        b = -y0 - vy*(hsteps20)
        ret = lincongeq(a, b, 2*h)
        if ret:
            k = ret[1]
            t = 2*w*k + hsteps20
            if t_min > t:
                t_min, xf, yf = t, 0, 0
        # ----------------------------------------
        # 1.2) y0 + vy*(2wk + hsteps20) = h (mod 2h)
        # => (vy*2*w) * k = h - y0 - vy*hsteps20
        a = vy*2*w
        b = h - y0 - vy*(hsteps20)
        ret = lincongeq(a, b, 2*h)
        if ret:
            k = ret[1]
            t = 2*w*k + hsteps20
            if t_min > t:
                t_min, xf, yf = t, 0, h
        # 2) x = x0 + 2wk + hsteps2w = w (mod 2w)
        # ----------------------------------------
        # 2.1) y0 + vy*(2wk + hsteps2w) = 0 (mod 2h)
        # => (vy*2w) * k = -y0 - vy*(hsteps2w) (mod 2h)
        a = vy*2*w
        b = -y0 - vy*(hsteps2w)
        ret = lincongeq(a, b, 2*h)
        if ret:
            k = ret[1]
            t = 2*w*k + hsteps2w
            if t_min > t:
                t_min, xf, yf = t, w, 0
        # ----------------------------------------
        # 2.2) y0 + vy*(2wk + hsteps2w) = h (mod 2h)
        # => (vy*2*w) * k = h - y0 - vy*(hsteps2w)
        a = vy*2*w
        b = h - y0 - vy*(hsteps2w)
        ret = lincongeq(a, b, 2*h)
        if ret:
            k = ret[1]
            t = 2*w*k + hsteps2w
            if t_min > t:
                t_min, xf, yf = t, w, h
    elif (x0 == 0 or x0 == w) and vy != 0: # vx == 0
        t_min = 0
        xf = x0
        yf = h if vy > 0 else 0
    if t_min == INF:
        print("-1")
    else:
        print("%d %d" % (xf, yf))

main()