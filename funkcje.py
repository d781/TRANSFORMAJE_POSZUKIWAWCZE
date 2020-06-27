import numpy as np
#Wczytywanie danych z pliku
def wczytaj(plik,wiersze):
    tmp = []
    with open(plik, 'r+') as pl:
        linie = pl.readlines()
        for ln in linie:
            li = ln.rstrip().lstrip().split()
            tmp.append(li)
    del tmp[wiersze-1]

    return  tmp

#Wyszukiwanie punktów w zbiorze
def szukaj(nr,wsp):
    tmp = 'brak'
    for i in wsp:
        if str(i[0]) == str(nr):
            tmp = i
    return tmp

#Obliczenie azymutu
def azymut(p, k, jednostka='g'):
    dx = k[1] - p[1]
    dy = k[2] - p[2]
    if dy == 0:
        if dx > 0:
            az = 0
        elif dx < 0:
            az = 200
    elif dx == 0:
        if dy > 0:
            az = 100
        elif dy < 0:
            az = 300
    else:
        if dx < 0:
            az = 200 + np.arctan(dy / dx) * 200 / np.pi
        elif dx > 0:
            if dy > 0:
                az = np.arctan(dy / dx) * 200 / np.pi
            elif dy < 0:
                az = 400 + np.arctan(dy / dx) * 200 / np.pi
    if az >= 400:
        az = az - 400

    if jednostka == 'r':
        az = az * np.pi /200
    elif jednostka == 's':
        az = az * 9 / 10
    return az

#Wyznaczenie parametrów transformacji Helmerta
def parametry_Helmert(P,W):
    opisA = []
    for i in P:
        opisA.append('X_'+ i[0])
    for i in P:
        opisA.append('Y_'+ i[0])
        Ax = []
        Ay = []
        Lx = []
        Ly = []
    for i in P:
        Ax.append([i[1], -i[2], 1, 0])
        Ay.append([i[2], i[1], 0, 1])
        pkt = szukaj(i[0],W)
        Lx.append(pkt[1])
        Ly.append(pkt[2])
    A = np.array(Ax + Ay)
    L = np.array(Lx + Ly)
    X = np.linalg.inv(A.T @ A) @ A.T @ L
    v = A @ X - L
    m0 = np.sqrt((v.T @ v) / len(P) - 4)
    covX = (m0 ** 2) * np.linalg.inv(A.T @ A)
    covO = A @ covX @ A.T
    teta = azymut([0,0,0], [0,X[0],X[1]])
    skala = X[0] / np.cos(teta * np.pi / 200)
    return  X, m0, covX, covO, teta, skala

#Wyznaczenie współrzędnych punktów w układzie wtórnym
def wspolrzedne_Helmert(par,pkt):
    punkty = []
    for i in pkt:
        X  = par[0] * i[1] - par[1] * i[2] + par[2]
        Y = par[1] * i[1] + par[0] * i[2] + par[3]
        punkty.append([i[0], X, Y, i[5]])
    return punkty

#Wyznaczenie różnicy między współrzędnymi
def roznica_uklady(zerowy, aktualny):
    punkty = []
    for i in zerowy:
        pkt = szukaj(i[0], aktualny)
        dx = (pkt[1] - i[1]) * 1000
        dy = (pkt[2] - i[2]) * 1000
        dl = np.sqrt( dx ** 2 + dy ** 2)
        kwad = i[5] ** 2 + pkt[3] ** 2
        if kwad <= 0:
            bl = 0
            q = dl/1
        else:
            bl = np.sqrt( kwad )
            q = dl / bl
        punkty.append([i[0], i[1], i[2],i[5], pkt[1], pkt[2], pkt[3], dx, dy, dl, bl, q ])
    return punkty
