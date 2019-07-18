#  Euler's Method
def euler(f, t0, y0, h, N):
    tt = [t0]
    yy = [y0]
    # p = [(tt[0], yy[0])]
    for i in range(N):
        tt.append((t0 + (i+1)*h))
        m = f(t=tt[i], y=yy[i])
        yy.append((yy[i] + m*h))
        # p.append((tt[i+1], yy[i+1]))

    return tt, yy


#  Improved Euler's Method
def improved_euler(f, t0, y0, h, N):
    tt = [t0]
    yy = [y0]
    # p = [(tt[0], yy[0])]
    for i in range(N):
        tt.append((t0 + (i+1)*h))
        m1 = f(t=tt[i], y=yy[i])
        yyy = yy[i] + m1*h
        m2 = f(t=tt[i+1], y=yyy)
        m = (m1 + m2)/2
        yy.append((yy[i] + m*h))
        # p.append((tt[i+1], yy[i+1]))
    return tt, yy


#  Runge-Kutta Method
def runge_kutta(f, t0, y0, h, N):
    tt = [t0]
    yy = [y0]
    # p = [(tt[0], yy[0])]
    for i in range(N):
        tt.append((t0 + (i+1)*h))
        m1 = f(t=tt[i], y=yy[i])
        y2 = yy[i] + m1*h/2
        m2 = f(t=tt[i] + h/2, y=y2)
        y3 = yy[i] + m2*h/2
        m3 = f(t=tt[i] + h/2, y=y3)
        y4 = yy[i] + m3*h
        m4 = f(t=tt[i+1], y=y4)
        m = (m1 + 2*m2 + 2*m3 + m4)/6
        yy.append((yy[i] + m*h))
        # p.append((tt[i+1], yy[i+1]))
    return tt, yy


