import numpy as np
from klasy import Point
from komunikaty import *


#Wczytywanie danych z pliku
def wczytaj(plik,naglowek):
    tmp = []
    with open(plik, 'r+') as pl:
        linie = pl.readlines()
        if naglowek == 'T':
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
def azymut(dx, dy, jednostka='g'):
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

#Zapis raportu skróconego
def raport_skrocony(sciezka,tr, dok, dok_bl, par, parmax,teraz):
    pl = open(sciezka , 'w+')
    pl.write('<>' * 39)
    pl.write('\n')
    pl.write('{:^78}\n'.format('Loża Szyderców and Company'))
    pl.write('{:^78}\n'.format('PRZEDSTAWIA'))
    pl.write('{:^78}\n'.format('Transformacje poszukiwawcze'))
    pl.write('Wykonali:\ninż. Damian Ozga\ninż. Kamil Olko\ninż. Maria Słowiak\n')
    pl.write('{:^78}\n'.format('AGH 2020'))
    pl.write('<>' * 39)
    pl.write('\n')
    pl.write('*' *78)
    pl.write('\n\n{:^78}\n'.format('SKRÓCONY RAPORT OBLICZEŃ'))
    pl.write('\n')
    pl.write('*' * 78)
    pl.write('\n')



    pl.write('PARAMETR STERUJĄCY: {}\n'.format(par))
    if par == 'q':
        pl.write('q_max = {}\n'.format(parmax))
    else:
        pl.write('dl_max = {}\n'.format(parmax))
    pl.write('\nPUNKTY DOSTOSOWANIE\n')
    pl.write('{:<13s}\t{:<20s}\t{:<20s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_zerowe [m]'))
    pl.write('{:<13s}\t{:<20s}\t{:<20s}\n'.format('', 'Y_aktualne [m]', 'Y_zerowe [m]'))
    for j in range(len(tr.P)):
        if dok == 0:
            pl.write('{:<13s}\t{:<20.0f}\t{:<20.0f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.0f}\t{:<20.0f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 1:
            pl.write('{:<13s}\t{:<20.1f}\t{:<20.1f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.1f}\t{:<20.1f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 2:
            pl.write('{:<13s}\t{:<20.2f}\t{:<20.2f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.2f}\t{:<20.2f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 3:
            pl.write('{:<13s}\t{:<20.3f}\t{:<20.3f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.3f}\t{:<20.3f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 4:
            pl.write('{:<13s}\t{:<20.4f}\t{:<20.4f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.4f}\t{:<20.4f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 5:
            pl.write('{:<13s}\t{:<20.5f}\t{:<20.5f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.5f}\t{:<20.5f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 6:
            pl.write('{:<13s}\t{:<20.6f}\t{:<20.6f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.6f}\t{:<20.6f}\n'.format('', tr.P[j].y, tr.W[j].y))
    pl.write('\nPARAMETRY TRANSFORMACJI\n')
    pl.write('a = {:<.10f}\n'.format(tr.a))
    pl.write('b = {:<.10f}\n'.format(tr.b))
    pl.write('c = {:<.10f} [m]\n'.format(tr.c))
    pl.write('d = {:<.10f} [m]\n'.format(tr.d))
    pl.write('Skala = {:<.10f}\n'.format(tr.skala))
    pl.write('Kąt skręcenia = {:<.10f} [grad]\n\n'.format(tr.teta))
    pl.write('PUNKTY STAŁE PO TRANSFORMACJI\n')
    pkt = copy.deepcopy(tr.pkt_potrans)
    stale = []
    przemieszczone = []
    for i in pkt:
        tmp = szukaj(i.nr, tr.P)
        if tmp == 'brak':
            przemieszczone.append(i)
        else:
            stale.append(i)
    dl_sr = 0
    for i in stale:
        dl_sr += i.dl
    dl_sr = dl_sr / len(stale)
    if par == 'q':
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]',
                                                                           'dx [mm]', 'dl [mm]', 'q'))
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]',
                                                                  'Mdl [mm]'))
    elif par == 'dl':
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]', 'dx [mm]',
                                                                  'dl [mm]'))
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\n'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]'))
    if par == 'q':
        for j in stale:
            if dok == 0:
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 1:
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 2:
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 3:
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', j.y, j.Y, j.dy))
            elif dok == 4:
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', j.y, j.Y, j.dy))
            elif dok == 5:
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', j.y, j.Y, j.dy))
            elif dok == 6:
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', j.y, j.Y, j.dy))
            if dok_bl == 0:
                pl.write('\t{:<10.0f}\n'.format(j.MP))
            elif dok_bl == 1:
                pl.write('\t{:<10.1f}\n'.format(j.MP))
            elif dok_bl == 2:
                pl.write('\t{:<10.2f}\n'.format(j.MP))
            elif dok_bl == 4:
                pl.write('\t{:<10.3f}\n'.format(j.MP))
    else:
        for j in stale:
            if dok == 0:
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 1:
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 2:
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 3:
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 4:
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 5:
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 6:
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\n'.format('', j.y, j.Y, j.dy))
    pl.write('\nPrzemieszczenia średnie na punktach stałych:\n')
    pl.write('DL_ŚR = {:<.4f} [mm]\n'.format(dl_sr))
    pl.write('\nPUNKTY PRZEMIESZCZONE\n')

    if par == 'q':
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]',
                                                                           'dx [mm]', 'dl [mm]', 'q'))
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('', 'Y_aktualne [m]', 'Y_wtórne [m]', 'dy [mm]',
                                                                  'Mdl [mm]'))
    elif par == 'dl':
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]', 'dx [mm]',
                                                                  'dl [mm]'))
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\n'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]'))

    if par == 'q':
        for j in przemieszczone:
            if dok == 0:
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 1:
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 2:
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 3:
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', j.y, j.Y, j.dy))
            elif dok == 4:
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', j.y, j.Y, j.dy))
            elif dok == 5:
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', j.y, j.Y, j.dy))
            elif dok == 6:
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', j.y, j.Y, j.dy))

            if dok_bl == 0:
                pl.write('\t{:<10.0f}\n'.format(j.MP))
            elif dok_bl == 1:
                pl.write('\t{:<10.1f}\n'.format(j.MP))
            elif dok_bl == 2:
                pl.write('\t{:<10.2f}\n'.format(j.MP))
            elif dok_bl == 4:
                pl.write('\t{:<10.3f}\n'.format(j.MP))

    else:
        for j in przemieszczone:
            if dok == 0:
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 1:
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 2:
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 3:
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 4:
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 5:
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 6:
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\n'.format('', j.y, j.Y, j.dy))

    #Stopka programu
    pl.write('\n')
    pl.write('<>' * 39)
    pl.write('')
    pl.write('\n\n{:>78s}'.format('Obliczył........................'))
    pl.write('')
    pl.write('\n\n{:22}Data wykonania {:02}.{:02}.{:04} {:02}:{:02}:{:02}\n'.format(' ', teraz.day,
                                                                           teraz.month, teraz.year, teraz.hour,
                                                                           teraz.minute, teraz.second))
    pl.write('<>' * 39)

#Zapis raportu pełnego do pliku txt
def raport_pelny(sciezka,tr, dok, dok_bl, par, parmax,teraz, proces_trans):
    pl = open(sciezka , 'w+')
    pl.write('<>' * 39)
    pl.write('\n')
    pl.write('{:^78}\n'.format('Loża Szyderców and Company'))
    pl.write('{:^78}\n'.format('PRZEDSTAWIA'))
    pl.write('{:^78}\n'.format('Transformacje poszukiwawcze'))
    pl.write('Wykonali:\ninż. Damian Ozga\ninż. Kamil Olko\ninż. Maria Słowiak\n')
    pl.write('{:^78}\n'.format('AGH 2020'))
    pl.write('<>' * 39)
    pl.write('\n')

    pl.write('*' * 78)
    pl.write('\n{:^78}\n'.format('KOMBINACJE PAR DOSTOSOWANIA'))

    pl.write('*' * 78)
    pl.write('\n')  
    for i, it in enumerate(tr):
        pl.write('..' * 39)
        pl.write('\nITERACJA: {}\n'.format(i))
        pl.write('PARAMETR STERUJĄCY: {}\n'.format(par))
        if par == 'q':
            pl.write('q_max = {}\n'.format(parmax))
        else:
            pl.write('dl_max = {}\n'.format(parmax))
        pl.write('\nPUNKTY DOSTOSOWANIE\n')
        pl.write('{:<13s}\t{:<20s}\t{:<20s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_zerowe [m]'))
        pl.write('{:<13s}\t{:<20s}\t{:<20s}\n'.format('', 'Y_aktualne [m]', 'Y_zerowe [m]'))
        for j in range(len(it.P)):
            if dok == 0:
                pl.write('{:<13s}\t{:<20.0f}\t{:<20.0f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.0f}\t{:<20.0f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 1:
                pl.write('{:<13s}\t{:<20.1f}\t{:<20.1f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.1f}\t{:<20.1f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 2:
                pl.write('{:<13s}\t{:<20.2f}\t{:<20.2f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.2f}\t{:<20.2f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 3:
                pl.write('{:<13s}\t{:<20.3f}\t{:<20.3f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.3f}\t{:<20.3f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 4:
                pl.write('{:<13s}\t{:<20.4f}\t{:<20.4f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.4f}\t{:<20.4f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 5:
                pl.write('{:<13s}\t{:<20.5f}\t{:<20.5f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.5f}\t{:<20.5f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 6:
                pl.write('{:<13s}\t{:<20.6f}\t{:<20.6f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.6f}\t{:<20.6f}\n'.format('', it.P[j].y, it.W[j].y))
        pl.write('\nPARAMETRY TRANSFORMACJI\n')
        pl.write('a = {:<.10f}\n'.format(it.a))
        pl.write('b = {:<.10f}\n'.format(it.b))
        pl.write('c = {:<.10f} [m]\n'.format(it.c))
        pl.write('d = {:<.10f} [m]\n'.format(it.d))
        pl.write('Skala = {:<.10f}\n'.format(it.skala))
        pl.write('Kąt skręcenia = {:<.10f} [grad]\n\n'.format(it.teta))
        pl.write('PUNKTY TRANSFORMOWANE\n')
        if par == 'q':
            pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]', 'dx [mm]', 'dl [mm]', 'q'))
            pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]','dy [mm]', 'Mdl [mm]'))
        elif par == 'dl':
            pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]','dx [mm]', 'dl [mm]'))
            pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\n'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]'))
        if par == 'q':
            for j in range(len(it.pkt_potrans)):
                if dok == 0:
                    pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 1:
                    pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 2:
                    pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 3:
                    pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 4:
                    pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 5:
                    pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 6:
                    pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                if dok_bl ==0:
                    pl.write('\t{:<10.0f}\n'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 1:
                    pl.write('\t{:<10.1f}\n'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 2:
                    pl.write('\t{:<10.2f}\n'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 4:
                    pl.write('\t{:<10.3f}\n'.format(it.pkt_potrans[j].MP))
            pl.write('\nIlośc punktów spełniających warunek q < q_max = {}\n'.format(it.lpq))
            pl.write('Suma dl = {:<.4f}\n'.format(it.sumdl))
        else:
            for j in range(len(it.pkt_potrans)):
                if dok == 0:
                    pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 1:
                    pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 2:
                    pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 3:
                    pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 4:
                    pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 5:
                    pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 6:
                    pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
            pl.write('\nIlośc punktów spełniających warunek dl < dl_max = {}\n'.format(it.lpdl))
            pl.write('Suma dl = {:<.4f}\n'.format(it.sumdl))
    tr = proces_trans
    pl.write('*' * 78)
    pl.write('\n{:^78}\n'.format('ITERACYJNY WYBÓR PUNKTÓW STAŁYCH NA PODSTWIE WYBRANEJ PARY'))
    pl.write('*' * 78)
    pl.write('\n')
    for i, it in enumerate(tr):
        pl.write('..' * 39)
        pl.write('\nITERACJA: {}\n'.format(i))
        pl.write('PARAMETR STERUJĄCY: {}\n'.format(par))
        if par == 'q':
            pl.write('q_max = {}\n'.format(parmax))
        else:
            pl.write('dl_max = {}\n'.format(parmax))
        pl.write('\nPUNKTY DOSTOSOWANIE\n')
        pl.write('{:<13s}\t{:<20s}\t{:<20s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_zerowe [m]'))
        pl.write('{:<13s}\t{:<20s}\t{:<20s}\n'.format('', 'Y_aktualne [m]', 'Y_zerowe [m]'))
        for j in range(len(it.P)):
            if dok == 0:
                pl.write('{:<13s}\t{:<20.0f}\t{:<20.0f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.0f}\t{:<20.0f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 1:
                pl.write('{:<13s}\t{:<20.1f}\t{:<20.1f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.1f}\t{:<20.1f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 2:
                pl.write('{:<13s}\t{:<20.2f}\t{:<20.2f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.2f}\t{:<20.2f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 3:
                pl.write('{:<13s}\t{:<20.3f}\t{:<20.3f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.3f}\t{:<20.3f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 4:
                pl.write('{:<13s}\t{:<20.4f}\t{:<20.4f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.4f}\t{:<20.4f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 5:
                pl.write('{:<13s}\t{:<20.5f}\t{:<20.5f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.5f}\t{:<20.5f}\n'.format('', it.P[j].y, it.W[j].y))
            elif dok == 6:
                pl.write('{:<13s}\t{:<20.6f}\t{:<20.6f}\n'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                pl.write('{:<13s}\t{:<20.6f}\t{:<20.6f}\n'.format('', it.P[j].y, it.W[j].y))
        pl.write('\nPARAMETRY TRANSFORMACJI\n')
        pl.write('a = {:<.10f}\n'.format(it.a))
        pl.write('b = {:<.10f}\n'.format(it.b))
        pl.write('c = {:<.10f} [m]\n'.format(it.c))
        pl.write('d = {:<.10f} [m]\n'.format(it.d))
        pl.write('Skala = {:<.10f}\n'.format(it.skala))
        pl.write('Kąt skręcenia = {:<.10f} [grad]\n\n'.format(it.teta))
        pl.write('PUNKTY TRANSFORMOWANE\n')
        if par == 'q':
            pl.write(
                '{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]','dx [mm]', 'dl [mm]', 'q'))
            pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]', 'Mdl [mm]'))
        elif par == 'dl':
            pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]','dx [mm]', 'dl [mm]'))
            pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\n'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]'))
        if par == 'q':
            for j in range(len(it.pkt_potrans)):
                if dok == 0:
                    pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 1:
                    pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 2:
                    pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 3:
                    pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 4:
                    pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 5:
                    pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 6:
                    pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))

                if dok_bl == 0:
                    pl.write('\t{:<10.0f}\n'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 1:
                    pl.write('\t{:<10.1f}\n'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 2:
                    pl.write('\t{:<10.2f}\n'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 4:
                    pl.write('\t{:<10.3f}\n'.format(it.pkt_potrans[j].MP))
            pl.write('\nIlośc punktów spełniających warunek q < q_max = {}\n'.format(it.lpq))
            pl.write('Suma dl = {:<.4f}\n'.format(it.sumdl))
        else:
            for j in range(len(it.pkt_potrans)):
                if dok == 0:
                    pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 1:
                    pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 2:
                    pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 3:
                    pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 4:
                    pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 5:
                    pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 6:
                    pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\n'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\n'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
            pl.write('\nIlośc punktów spełniających warunek dl < dl_max = {}\n'.format(it.lpdl))
            pl.write('Suma dl = {:<.4f}\n'.format(it.sumdl))

    tr = proces_trans[-1]
    pl.write('\n')
    pl.write('*' *78)
    pl.write('\n{:^78}\n'.format('PODSUMOWANIE WYNIKÓW'))
    pl.write('*' * 78)
    pl.write('\n')



    pl.write('PARAMETR STERUJĄCY: {}\n'.format(par))
    if par == 'q':
        pl.write('q_max = {}\n'.format(parmax))
    else:
        pl.write('dl_max = {}\n'.format(parmax))
    pl.write('\nPUNKTY DOSTOSOWANIE\n')
    pl.write('{:<13s}\t{:<20s}\t{:<20s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_zerowe [m]'))
    pl.write('{:<13s}\t{:<20s}\t{:<20s}\n'.format('', 'Y_aktualne [m]', 'Y_zerowe [m]'))
    for j in range(len(tr.P)):
        if dok == 0:
            pl.write('{:<13s}\t{:<20.0f}\t{:<20.0f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.0f}\t{:<20.0f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 1:
            pl.write('{:<13s}\t{:<20.1f}\t{:<20.1f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.1f}\t{:<20.1f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 2:
            pl.write('{:<13s}\t{:<20.2f}\t{:<20.2f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.2f}\t{:<20.2f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 3:
            pl.write('{:<13s}\t{:<20.3f}\t{:<20.3f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.3f}\t{:<20.3f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 4:
            pl.write('{:<13s}\t{:<20.4f}\t{:<20.4f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.4f}\t{:<20.4f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 5:
            pl.write('{:<13s}\t{:<20.5f}\t{:<20.5f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.5f}\t{:<20.5f}\n'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 6:
            pl.write('{:<13s}\t{:<20.6f}\t{:<20.6f}\n'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            pl.write('{:<13s}\t{:<20.6f}\t{:<20.6f}\n'.format('', tr.P[j].y, tr.W[j].y))
    pl.write('\nPARAMETRY TRANSFORMACJI\n')
    pl.write('a = {:<.10f}\n'.format(tr.a))
    pl.write('b = {:<.10f}\n'.format(tr.b))
    pl.write('c = {:<.10f} [m]\n'.format(tr.c))
    pl.write('d = {:<.10f} [m]\n'.format(tr.d))
    pl.write('Skala = {:<.10f}\n'.format(tr.skala))
    pl.write('Kąt skręcenia = {:<.10f} [grad]\n\n'.format(tr.teta))
    pl.write('PUNKTY STAŁE PO TRANSFORMACJI\n')
    pkt = copy.deepcopy(tr.pkt_potrans)
    stale = []
    przemieszczone = []
    for i in pkt:
        tmp = szukaj(i.nr, tr.P)
        if tmp == 'brak':
            przemieszczone.append(i)
        else:
            stale.append(i)
    dl_sr = 0
    for i in stale:
        dl_sr += i.dl
    dl_sr = dl_sr / len(stale)
    if par == 'q':
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]',
                                                                           'dx [mm]', 'dl [mm]', 'q'))
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]',
                                                                  'Mdl [mm]'))
    elif par == 'dl':
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]', 'dx [mm]',
                                                                  'dl [mm]'))
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\n'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]'))
    if par == 'q':
        for j in stale:
            if dok == 0:
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 1:
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 2:
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 3:
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', j.y, j.Y, j.dy))
            elif dok == 4:
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', j.y, j.Y, j.dy))
            elif dok == 5:
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', j.y, j.Y, j.dy))
            elif dok == 6:
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', j.y, j.Y, j.dy))
            if dok_bl == 0:
                pl.write('\t{:<10.0f}\n'.format(j.MP))
            elif dok_bl == 1:
                pl.write('\t{:<10.1f}\n'.format(j.MP))
            elif dok_bl == 2:
                pl.write('\t{:<10.2f}\n'.format(j.MP))
            elif dok_bl == 4:
                pl.write('\t{:<10.3f}\n'.format(j.MP))
    else:
        for j in stale:
            if dok == 0:
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 1:
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 2:
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 3:
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 4:
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 5:
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 6:
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\n'.format('', j.y, j.Y, j.dy))
    pl.write('\nPrzemieszczenie średnie na punktach stałych:\n')
    pl.write('DL_ŚR = {:<.4f} [mm]\n'.format(dl_sr))
    pl.write('\nPUNKTY PRZEMIESZCZONE\n')

    if par == 'q':
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]',
                                                                           'dx [mm]', 'dl [mm]', 'q'))
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('', 'Y_aktualne [m]', 'Y_wtórne [m]', 'dy [mm]',
                                                                  'Mdl [mm]'))
    elif par == 'dl':
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\n'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]', 'dx [mm]',
                                                                  'dl [mm]'))
        pl.write('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\n'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]'))

    if par == 'q':
        for j in przemieszczone:
            if dok == 0:
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 1:
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 2:
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 3:
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', j.y, j.Y, j.dy))
            elif dok == 4:
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', j.y, j.Y, j.dy))
            elif dok == 5:
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', j.y, j.Y, j.dy))
            elif dok == 6:
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl,
                                                                                             j.q))
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', j.y, j.Y, j.dy))

            if dok_bl == 0:
                pl.write('\t{:<10.0f}\n'.format(j.MP))
            elif dok_bl == 1:
                pl.write('\t{:<10.1f}\n'.format(j.MP))
            elif dok_bl == 2:
                pl.write('\t{:<10.2f}\n'.format(j.MP))
            elif dok_bl == 4:
                pl.write('\t{:<10.3f}\n'.format(j.MP))

    else:
        for j in przemieszczone:
            if dok == 0:
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 1:
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 2:
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 3:
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 4:
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 5:
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\n'.format('', j.y, j.Y, j.dy))
            elif dok == 6:
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\n'.format(j.nr, j.x, j.X, j.dx, j.dl))
                pl.write('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\n'.format('', j.y, j.Y, j.dy))

    #Stopka programu
    pl.write('\n')
    pl.write('<>' * 39)
    pl.write('')
    pl.write('\n\n{:>78s}'.format('Obliczył........................'))
    pl.write('')
    pl.write('\n\n{:22}Data wykonania {:02}.{:02}.{:04} {:02}:{:02}:{:02}\n'.format(' ', teraz.day,
                                                                           teraz.month, teraz.year, teraz.hour,
                                                                           teraz.minute, teraz.second))
    pl.write('<>' * 39)













































































































