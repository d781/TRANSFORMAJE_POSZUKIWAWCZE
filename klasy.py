import numpy as np
import funkcje as f
# Klasy

class Point():
    """Opis punktu"""
    def __init__(self, nr='', x=0, y=0, mx=0, my=0, mp=0, X=0, Y=0):
        self.mx = mx
        self.my = my
        self.mp = mp
        self.x = x
        self.y = y
        self.nr = nr
        self.X = X
        self.Y = Y
        self.dx = 0
        self.dy = 0
        self.dl = 0
        self.MP = 0
        self.q = 0


class transform():
    """Transformacja Helmerta"""
    def __init__(self, P = [], W = [], pkt_pier = [], pkt_wtor = []):
        self.P = P
        self.W = W
        self.pkt_pier = pkt_pier
        self.pkt_wtor = pkt_wtor
        self.pkt_potrans = []
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.skala = 0
        self.teta = 0
        self.covX = 0
        self.m0 = 0
        self.covO = 0
        self.opisA = []
        self.v =[]
        self.lpq = 0
        self.lpdl = 0
        self.sumdl = 0


    """Obliczenie parametrów transformacji Helmerta"""
    def parametry(self):
        Ax = []
        Ay = []
        Lx = []
        Ly = []
        for i in self.P:
            self.opisA.append('X_' + i.nr)
        for i in self.P:
            self.opisA.append('Y_' + i.nr)
        for i in self.P:
            Ax.append([i.x, -i.y, 1, 0])
            Ay.append([i.y, i.x, 0, 1])
        for i in self.W:
            Lx.append(i.x)
            Ly.append(i.y)
        A = np.array(Ax + Ay)
        L = np.array(Lx + Ly)
        dX = np.linalg.inv(A.T @ A) @ A.T @ L
        self.a = dX[0]
        self.b = dX[1]
        self.c = dX[2]
        self.d = dX[3]
        v = np.array(A @ dX - L)
        if len(self.P) < 3:
            self.m0 = 1
        else:
            self.m0 =np.sqrt(((v.T @ v) / ((len(self.P) * 2) - 4))) * 1000
        self.covX = (self.m0 ** 2) * np.linalg.inv(A.T @ A)
        self.covO = A @ self.covX @ A.T
        self.teta = f.azymut(self.a, self.b)
        self.skala = np.sqrt(self.a ** 2 + self.b **2)




    """Obliczenie współrzędnych punktów w układzie wtornym"""
    def wspolrzedne(self):
        for i in self.pkt_pier:
            pu = f.szukaj(i.nr, self.pkt_wtor)
            x = pu.x
            y = pu.y
            X = self.a * i.x - self.b * i.y + self.c
            Y = self.b * i.x + self.a * i.y + self.d
            p = f.szukaj(i.nr, self.pkt_wtor)
            MP = np.sqrt(i.mp ** 2 + p.mp ** 2)
            dx = (X - x) * 1000
            dy = (Y - y) * 1000
            dl = np.sqrt(dx ** 2 + dy ** 2)
            q = np.abs(dl) / MP
            tmp = Point(nr=i.nr, x=x, y=y, X=X, Y=Y)
            tmp.MP = MP
            tmp.dx = dx
            tmp.dy = dy
            tmp.q = q
            tmp.dl = dl
            self.pkt_potrans.append(tmp)

    """Obliczanie ilosci pkt których parametr q jest mniejszy od zakladanego"""
    def zliczanie_q(self, q):
        for i in self.pkt_potrans:
            if i.q <= q:
                self.lpq +=1

    """Obliczanie ilosci pkt których parametr dl jest mniejszy od zakladanego"""
    def zliczanie_dl(self, dl):
        for i in self.pkt_potrans:
            if i.dl <= dl:
                self.lpdl +=1

    """Obliczanie sumy przemieszczenia liniowego"""
    def zliczanie_sumy(self):
        for i in self.pkt_potrans:
            self.sumdl = self.sumdl + np.abs(i.dl)
