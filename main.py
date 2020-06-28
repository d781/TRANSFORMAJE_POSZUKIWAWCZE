from funkcje import *
from klasy import *
from komunikaty import *
import sys
import copy
import datetime
import os

if __name__ == '__main__':
    sciezka_wejscie = 'dane_wejsciowe'
    sciezka_wyjscie = 'dane_wyjsciowe'
    wiersz = 'T'
    q_max = 2
    dl_max = 3
    parametr_sortowania = 'q'
    dok = 5
    dok_bl =2

    #Wyświetlenie nagłówka programu
    naglowek()

    #Dostosowanie opcji programu
    sciezka_wejscie, sciezka_wyjscie, wiersz, dok, dok_bl, parametr_sortowania, q_max, dl_max = komunikat_glowny(sciezka_wejscie, sciezka_wyjscie, wiersz, dok, dok_bl, parametr_sortowania, q_max, dl_max)

    # Sprawdzenie czy folder istnieje i utworzenie go
    if os.path.exists(sciezka_wejscie) == False:
        os.mkdir(sciezka_wejscie)
    if os.path.exists(sciezka_wyjscie) == False:
        os.mkdir(sciezka_wyjscie)

    #Import danych z pliku
    ep0 = wczytaj(sciezka_wejscie + '/' + 'P1.txt', wiersz)
    ep1 = wczytaj(sciezka_wejscie + '/' + 'P2.txt', wiersz)

    #Obliczenie transformacji dla każdych par punktów jako punkty dostosowania
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

    #Wyświetlenie pierwszej części raportu
    if parametr_sortowania == 'q':
        wybor_par_rap(transformacje_sort, dok, dok_bl, parametr_sortowania, q_max)
    elif parametr_sortowania == 'dl':
        wybor_par_rap(transformacje_sort, dok, dok_bl, parametr_sortowania, dl_max)

    #Wybór pary punktów dostosowania
    wyb_it = 0
    zmiana = 'p'
    print()
    print('*'*79)
    print()
    print('Do dalszych obliczeń wybrano punkty dostosowania z iteracji {}'.format(wyb_it))
    while (zmiana != 'T' and zmiana != 'N'):
        zmiana = str(input('Czy zmienić wybraną pare punktów ( T / N ): ')).upper()
    if zmiana == 'T':
        wyb_it = int(input('Podaj numer wybranej iteracji: '))
    print()
    print('*' * 79)
    print()

    #Wybór najlepszej pierwszej pary punktów
    wybrana = transformacje_sort[wyb_it]

    #Sprawdzenie warunku ilości puktów dostosowania o parametrze mniejszym niż zakładany
    if parametr_sortowania == 'q':
        if wybrana.lpq < 3:
            print('Brak dostatecznej liczby punktów spełniających warunek q < q_max')
            sys.exit(0)
    else:
        if wybrana.lpdl < 3:
            print('Brak dostatecznej liczby punktów spełniających warunek dl < dl_max')
            sys.exit(0)

    #Wyliczanie parametrów transformcaji podając punkty dostosowania które spełniają założony parametr
    proces_trans = []
    proces_trans.append(wybrana)
    it = 0
    stereo = 'T'
    while stereo == 'T':
        tmpEp0 = copy.deepcopy(proces_trans[it].W)
        tmpEp1 = copy.deepcopy(proces_trans[it].P)
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
            break
        tmpTrans = transform(tmpEp1, tmpEp0, ep1, ep0)
        tmpTrans.parametry()
        tmpTrans.wspolrzedne()
        tmpTrans.zliczanie_q(q_max)
        tmpTrans.zliczanie_dl(dl_max)
        tmpTrans.zliczanie_sumy()
        proces_trans.append(tmpTrans)
        it += 1
        del tmpTrans

    #Wyświetlanie raportu z właściwego procesu transformacji
    if parametr_sortowania == 'q':
        wybor_stalych_rap(proces_trans, dok, dok_bl, parametr_sortowania, q_max )
    elif parametr_sortowania == 'dl':
        wybor_stalych_rap(proces_trans, dok, dok_bl, parametr_sortowania, dl_max )
    #Wyświetlanie podsumowania wyników
    if parametr_sortowania == 'q':
        podsumowanie(proces_trans[-1], dok, dok_bl, parametr_sortowania, q_max )
    elif parametr_sortowania == 'dl':
        podsumowanie(proces_trans[-1], dok, dok_bl, parametr_sortowania, dl_max )

    #Wyświetlanie stopki programu
    teraz = datetime.datetime.now()
    stopka(teraz)

    #Zapisanie raportu do pliku tekstowego
    if parametr_sortowania == 'q':
        raport_skrocony(sciezka_wyjscie + '/' + 'RAPORT_SKROCONY.txt', proces_trans[-1], dok, dok_bl, parametr_sortowania, q_max, teraz)
        raport_pelny(sciezka_wyjscie + '/' + 'RAPORT_PELNY.txt', transformacje_sort, dok, dok_bl, parametr_sortowania, q_max, teraz,proces_trans)
    elif parametr_sortowania == 'dl':
        raport_skrocony(sciezka_wyjscie + '/' + 'RAPORT_SKROCONY.txt', proces_trans[-1], dok, dok_bl, parametr_sortowania, dl_max, teraz)
        raport_pelny(sciezka_wyjscie + '/' + 'RAPORT_PELNY.txt', transformacje_sort, dok, dok_bl, parametr_sortowania, dl_max, teraz,proces_trans)


    #Opracowali:
    #inż. Damian Ozga
    #inż. Kamil Olko
    #inż. Maria Słowiak












