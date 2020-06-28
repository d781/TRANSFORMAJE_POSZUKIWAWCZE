from funkcje import *
from klasy import *
import sys
import copy

if __name__ == '__main__':
    wiersze = 1
    sciezka_wejscie = 'dane_wejsciowe/'
    sciezka_wyjscie = 'dane wyjsciowe/'
    naglowek = 't'
    q_max = 2
    dl_max = 3
    parametr_sortowania ='q'

    #Import danych z pliku
    ep0 = wczytaj(sciezka_wejscie + 'P1.txt', naglowek)
    ep1 = wczytaj(sciezka_wejscie + 'P2.txt', naglowek)


    #Obliczenie transformacji dla karzdych par punktów jako punkty dostosowania
    transformacje =[]
    nu = 0
    for i in range(nu, len(ep1), 1):
        nu += 1
        for j in range(nu, len(ep1), 1):
            t1 = transform([ep1[i], ep1[j]], [ep0[i], ep0[j]], ep1, ep0)
            t1.parametry()
            t1.wspolrzedne()
            t1.zliczanie_q(q_max)
            t1.zliczanie_dl(dl_max)
            t1.zliczanie_sumy()
            transformacje.append(t1)

    #Sortowanie wykonanych transformacji po zadanym parametrze sterującym
    if parametr_sortowania == 'q':
        #Sortowanie po ilości punktów których q jest mniejsze od zadanego
        transformacje_sort = sortuj_transQ(transformacje)
    elif parametr_sortowania == 'dl':
        # Sortowanie po ilości punktów których dl jest mniejsze od zadanego
        transformacje_sort = sortuj_transDL(transformacje)

    #Wybór najlepszej pierwszej pary punktów
    wybrana = transformacje_sort[0]

    #Wyświetlenie raportu z transformacji
    #*************************************************************************************************************************************************************************************

    #Sprawdzenie warunku ilości puktów dostosowania o parametrze mniejszym niż zakładany
    if parametr_sortowania =='q':
        if wybrana.lpq < 3:
            print('Brak dostatecznej liczby punktów spełniających warunek q < q_max')
            sys.exit(0)
        elif wybrana.lpdl < 3:
            print('Brak dostatecznej liczby punktów spełniających warunek dl < dl_max')
            sys.exit(0)

    proces_trans = []
    proces_trans.append(wybrana)
    it = 0
    stereo = 'T'
    while stereo == 'T':
        tmpEp0 = proces_trans[it].W
        tmpEp1 = proces_trans[it].P
        tmp = copy.deepcopy(proces_trans[it].pkt_potrans)
        for i in tmpEp0:
            tmp = usun(i.nr, tmp)
        if parametr_sortowania == 'q':
            tmp = sorted(tmp, key=lambda x: x.q)
            ilosc = zliczQ(tmp, q_max)
        else:
            tmp = sorted(tmp, key=lambda x: x.dl)
            ilosc = zliczDL(tmp, dl_max)

        if ilosc > 0:
            tmpEp0.append(szukaj(tmp[0].nr, ep0))
            tmpEp1.append(szukaj(tmp[0].nr, ep1))
        else:
            stereo = 'N'
        tmpTrans = transform(tmpEp1, tmpEp0, ep1, ep0)
        tmpTrans.parametry()
        tmpTrans.wspolrzedne()
        tmpTrans.zliczanie_q(q_max)
        tmpTrans.zliczanie_dl(dl_max)
        tmpTrans.zliczanie_sumy()

        for i in tmpTrans.pkt_potrans:
            print(
                'nr {} x={:<10.5f} y={:<10.5f} X={:<10.5f} Y={:<10.5f} dx={:<10.5f} dy={:<10.5f} dl={:<10.5f} MP={:<10.5f} q={:<10.5f}'.format(
                    i.nr, i.x, i.y, i.X, i.Y, i.dx, i.dy, i.dl, i.MP, i.q))
        print('<>'*200)




















"""

    for t1 in transformacje_sort:
        print('*'*150)
        print('q=', t1.lpq)
        print('dl=', t1.lpdl)
        print('sumadl={:<15.8f}'.format( t1.sumdl))
        print('m0=', t1.m0)
        print(
            'a={:<10.5f} b={:<10.5f} c={:<10.5f} d={:<10.5f} skala={:<12.10f} teta={:<12.10f}'.format(t1.a, t1.b, t1.c,
                                                                                                      t1.d, t1.skala,
                                                                                                      t1.teta))
        for i in t1.pkt_potrans:
            print(
                'nr {} x={:<10.5f} y={:<10.5f} X={:<10.5f} Y={:<10.5f} dx={:<10.5f} dy={:<10.5f} dl={:<10.5f} MP={:<10.5f} q={:<10.5f}'.format(
                    i.nr, i.x, i.y, i.X, i.Y, i.dx, i.dy, i.dl, i.MP, i.q))

    print('<>'*100)

"""