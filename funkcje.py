import numpy as np
from klasy import Point
from komunikaty import *


#Wczytywanie danych z pliku
def wczytaj(plik,naglowek):
    tmp = []
    with open(plik, 'r+') as pl:
        linie = pl.readlines()
        if naglowek == 't':
            del linie[0]
        for ln in linie:
            li = ln.rstrip().lstrip().split()
            pkt = Point(li[0], float(li[1]), float(li[2]))
            if len(li) > 3:
                pkt.mx = float(li[3])
                pkt.my = float(li[4])
                pkt.mp = float(li[5])
            tmp.append(pkt)

    return  tmp

#Wyszukiwanie punktów w zbiorze
def szukaj(nr,wsp):
    tmp = 'brak'
    for i in wsp:
        if str(i.nr) == str(nr):
            tmp = i
    return tmp

#Obliczenie azymutu
def azymut(p, k, jednostka='g'):
    dx = k.x - p.x
    dy = k.y - p.y
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

#Sortowanie listy z transformacjami po parametrze q
def sortuj_transQ(trans):
    posortowane = []
    tmp = []
    tm = []
    trans = sorted(trans, key=lambda x: x.lpq, reverse = True)
    lp = trans[0].lpq
    for i in trans:
        if i.lpq == lp:
            tm.append(i)
        elif i.lpq < lp:
            tmp.append(tm)
            lp = i.lpq
            tm = []
    tmp.append(tm)
    for i in tmp:
        i = sorted(i, key=lambda x: x.sumdl)
        posortowane += i
    return posortowane

#Sortowanie listy z transformacjami po parametrze dl
def sortuj_transDL(trans):
    posortowane = []
    tmp = []
    tm = []
    trans = sorted(trans, key=lambda x: x.lpdl, reverse = True)
    lp = trans[0].lpdl
    for i in trans:
        if i.lpdl == lp:
            tm.append(i)
        elif i.lpdl < lp:
            tmp.append(tm)
            lp = i.lpdl
            tm = []
    tmp.append(tm)
    for i in tmp:
        i = sorted(i, key=lambda x: x.sumdl)
        posortowane += i
    return posortowane

#Zliczanie punktów
def zliczQ(lista, qmax):
    l = 0
    for i in lista:
        if i.q <= qmax:
            l += 1
    return l

def zliczDL(lista, dlmax):
    l = 0
    for i in lista:
        if i.dl <= dlmax:
            l += 1
    return l
#Usuwanie punktów z listy
def usun(nr, lista):
    for i, it in enumerate(lista):
        if it.nr == nr:
            del lista[i]
    return lista

