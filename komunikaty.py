import copy
import funkcje as f
import os

#Nagłówek programu
def naglowek():
    print('<>' * 39)
    print('{:^78}'.format('Loża Szyderców and Company'))
    print('{:^78}'.format('PRZEDSTAWIA'))
    print('{:^78}'.format('Transformacje poszukiwawcze'))
    print('Wykonali:\ninż. Damian Ozga\ninż. Kamil Olko\ninż. Maria Słowiak')
    print('{:^78}'.format('AGH 2020'))
    print('<>' * 39)
    print('')

#Stopka programu
def stopka(teraz):

    print('')
    print('<>' * 39)
    print('')
    print('{:>78s}'.format('Obliczył........................'))
    print('')
    print('{:22}Data wykonania {:02}.{:02}.{:04} {:02}:{:02}:{:02}'.format(' ',teraz.day,
                                                teraz.month,teraz.year, teraz.hour, teraz.minute, teraz.second ))
    print('<>' * 39)

#Raport z wyboru pary pierwszej
def wybor_par_rap(tr, dok, dok_bl,par, parmax):
    print('*' * 78)
    print('{:^78}'.format('KOMBINACJE PAR DOSTOSOWANIA'))
    print('*' * 78)
    for i, it in enumerate(tr):
        print('..' * 39)
        print('ITERACJA: {}'.format(i))
        print('PARAMETR STERUJĄCY: {}'.format(par))
        if par == 'q':
            print('q_max = {}'.format(parmax))
        else:
            print('dl_max = {}'.format(parmax))
        print('\nPUNKTY DOSTOSOWANIE')
        print('{:<13s}\t{:<20s}\t{:<20s}'.format('Nr_pkt', 'X_aktualne [m]', 'X_zerowe [m]'))
        print('{:<13s}\t{:<20s}\t{:<20s}'.format('', 'Y_aktualne [m]', 'Y_zerowe [m]'))
        for j in range(len(it.P)):
            if dok == 0:
                print('{:<13s}\t{:<20.0f}\t{:<20.0f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.0f}\t{:<20.0f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 1:
                print('{:<13s}\t{:<20.1f}\t{:<20.1f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.1f}\t{:<20.1f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 2:
                print('{:<13s}\t{:<20.2f}\t{:<20.2f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.2f}\t{:<20.2f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 3:
                print('{:<13s}\t{:<20.3f}\t{:<20.3f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.3f}\t{:<20.3f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 4:
                print('{:<13s}\t{:<20.4f}\t{:<20.4f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.4f}\t{:<20.4f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 5:
                print('{:<13s}\t{:<20.5f}\t{:<20.5f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.5f}\t{:<20.5f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 6:
                print('{:<13s}\t{:<20.6f}\t{:<20.6f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.6f}\t{:<20.6f}'.format('', it.P[j].y, it.W[j].y))

        print('\nPARAMETRY TRANSFORMACJI')
        print('a = {:<.10f}'.format(it.a))
        print('b = {:<.10f}'.format(it.b))
        print('c = {:<.10f} [m]'.format(it.c))
        print('d = {:<.10f} [m]'.format(it.d))
        print('Skala = {:<.10f}'.format(it.skala))
        print('Kąt skręcenia = {:<.10f} [grad]\n'.format(it.teta))
        print('PUNKTY TRANSFORMOWANE')
        if par == 'q':
            print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\t{:<13s}'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]', 'dx [mm]', 'dl [mm]', 'q'))
            print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]','dy [mm]', 'Mdl [mm]'))
        elif par == 'dl':
            print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]','dx [mm]', 'dl [mm]'))
            print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]'))
        if par == 'q':
            for j in range(len(it.pkt_potrans)):
                if dok == 0:
                    print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy),end='')
                elif dok == 1:
                    print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy),end='')
                elif dok == 2:
                    print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy),end='')
                elif dok == 3:
                    print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy),end='')
                elif dok == 4:
                    print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy),end='')
                elif dok == 5:
                    print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy),end='')
                elif dok == 6:
                    print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl, it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy),end='')
                if dok_bl ==0:
                    print('\t{:<10.0f}'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 1:
                    print('\t{:<10.1f}'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 2:
                    print('\t{:<10.2f}'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 4:
                    print('\t{:<10.3f}'.format(it.pkt_potrans[j].MP))
            print('\nIlośc punktów spełniających warunek q < q_max = {}'.format(it.lpq))
            print('Suma dl = {:<.4f}'.format(it.sumdl))
        else:
            for j in range(len(it.pkt_potrans)):
                if dok == 0:
                    print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 1:
                    print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 2:
                    print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 3:
                    print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 4:
                    print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 5:
                    print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 6:
                    print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X, it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
            print('\nIlośc punktów spełniających warunek dl < dl_max = {}'.format(it.lpdl))
            print('Suma dl = {:<.4f}'.format(it.sumdl))


# Raport z wyboru punktów stałych
def wybor_stalych_rap(tr, dok, dok_bl, par, parmax):
    print('*' * 78)
    print('{:^78}'.format('ITERACYJNY WYBÓR PUNKTÓW STAŁYCH NA PODSTWIE WYBRANEJ PARY'))
    print('*' * 78)
    for i, it in enumerate(tr):
        print('..' * 39)
        print('ITERACJA: {}'.format(i))
        print('PARAMETR STERUJĄCY: {}'.format(par))
        if par == 'q':
            print('q_max = {}'.format(parmax))
        else:
            print('dl_max = {}'.format(parmax))
        print('\nPUNKTY DOSTOSOWANIE')
        print('{:<13s}\t{:<20s}\t{:<20s}'.format('Nr_pkt', 'X_aktualne [m]', 'X_zerowe [m]'))
        print('{:<13s}\t{:<20s}\t{:<20s}'.format('', 'Y_aktualne [m]', 'Y_zerowe [m]'))
        for j in range(len(it.P)):
            if dok == 0:
                print('{:<13s}\t{:<20.0f}\t{:<20.0f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.0f}\t{:<20.0f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 1:
                print('{:<13s}\t{:<20.1f}\t{:<20.1f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.1f}\t{:<20.1f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 2:
                print('{:<13s}\t{:<20.2f}\t{:<20.2f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.2f}\t{:<20.2f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 3:
                print('{:<13s}\t{:<20.3f}\t{:<20.3f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.3f}\t{:<20.3f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 4:
                print('{:<13s}\t{:<20.4f}\t{:<20.4f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.4f}\t{:<20.4f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 5:
                print('{:<13s}\t{:<20.5f}\t{:<20.5f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.5f}\t{:<20.5f}'.format('', it.P[j].y, it.W[j].y))
            elif dok == 6:
                print('{:<13s}\t{:<20.6f}\t{:<20.6f}'.format(it.P[j].nr, it.P[j].x, it.W[j].x))
                print('{:<13s}\t{:<20.6f}\t{:<20.6f}'.format('', it.P[j].y, it.W[j].y))
        print('\nPARAMETRY TRANSFORMACJI')
        print('a = {:<.10f}'.format(it.a))
        print('b = {:<.10f}'.format(it.b))
        print('c = {:<.10f} [m]'.format(it.c))
        print('d = {:<.10f} [m]'.format(it.d))
        print('Skala = {:<.10f}'.format(it.skala))
        print('Kąt skręcenia = {:<.10f} [grad]\n'.format(it.teta))
        print('PUNKTY TRANSFORMOWANE')
        if par == 'q':
            print(
                '{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\t{:<13s}'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]','dx [mm]', 'dl [mm]', 'q'))
            print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]', 'Mdl [mm]'))
        elif par == 'dl':
            print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]','dx [mm]', 'dl [mm]'))
            print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]'))
        if par == 'q':
            for j in range(len(it.pkt_potrans)):
                if dok == 0:
                    print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy), end='')
                elif dok == 1:
                    print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy), end='')
                elif dok == 2:
                    print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy), end='')
                elif dok == 3:
                    print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy), end='')
                elif dok == 4:
                    print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy), end='')
                elif dok == 5:
                    print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy), end='')
                elif dok == 6:
                    print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl,it.pkt_potrans[j].q))
                    print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy), end='')

                if dok_bl == 0:
                    print('\t{:<10.0f}'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 1:
                    print('\t{:<10.1f}'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 2:
                    print('\t{:<10.2f}'.format(it.pkt_potrans[j].MP))
                elif dok_bl == 4:
                    print('\t{:<10.3f}'.format(it.pkt_potrans[j].MP))
            print('\nIlośc punktów spełniających warunek q < q_max = {}'.format(it.lpq))
            print('Suma dl = {:<.4f}'.format(it.sumdl))
        else:
            for j in range(len(it.pkt_potrans)):
                if dok == 0:
                    print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 1:
                    print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 2:
                    print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 3:
                    print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 4:
                    print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 5:
                    print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
                elif dok == 6:
                    print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}'.format(it.pkt_potrans[j].nr,it.pkt_potrans[j].x,it.pkt_potrans[j].X,it.pkt_potrans[j].dx,it.pkt_potrans[j].dl))
                    print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', it.pkt_potrans[j].y, it.pkt_potrans[j].Y, it.pkt_potrans[j].dy))
            print('\nIlośc punktów spełniających warunek dl < dl_max = {}'.format(it.lpdl))
            print('Suma dl = {:<.4f}'.format(it.sumdl))
            
#Podsumowanie wyników
def podsumowanie(tr, dok, dok_bl, par, parmax):
    print('*' * 78)
    print('{:^78}'.format('PODSUMOWANIE WYNIKÓW'))
    print('*' * 78)

    print('PARAMETR STERUJĄCY: {}'.format(par))
    if par == 'q':
        print('q_max = {}'.format(parmax))
    else:
        print('dl_max = {}'.format(parmax))
    print('\nPUNKTY DOSTOSOWANIE')
    print('{:<13s}\t{:<20s}\t{:<20s}'.format('Nr_pkt', 'X_aktualne [m]', 'X_zerowe [m]'))
    print('{:<13s}\t{:<20s}\t{:<20s}'.format('', 'Y_aktualne [m]', 'Y_zerowe [m]'))
    for j in range(len(tr.P)):
        if dok == 0:
            print('{:<13s}\t{:<20.0f}\t{:<20.0f}'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            print('{:<13s}\t{:<20.0f}\t{:<20.0f}'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 1:
            print('{:<13s}\t{:<20.1f}\t{:<20.1f}'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            print('{:<13s}\t{:<20.1f}\t{:<20.1f}'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 2:
            print('{:<13s}\t{:<20.2f}\t{:<20.2f}'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            print('{:<13s}\t{:<20.2f}\t{:<20.2f}'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 3:
            print('{:<13s}\t{:<20.3f}\t{:<20.3f}'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            print('{:<13s}\t{:<20.3f}\t{:<20.3f}'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 4:
            print('{:<13s}\t{:<20.4f}\t{:<20.4f}'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            print('{:<13s}\t{:<20.4f}\t{:<20.4f}'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 5:
            print('{:<13s}\t{:<20.5f}\t{:<20.5f}'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            print('{:<13s}\t{:<20.5f}\t{:<20.5f}'.format('', tr.P[j].y, tr.W[j].y))
        elif dok == 6:
            print('{:<13s}\t{:<20.6f}\t{:<20.6f}'.format(tr.P[j].nr, tr.P[j].x, tr.W[j].x))
            print('{:<13s}\t{:<20.6f}\t{:<20.6f}'.format('', tr.P[j].y, tr.W[j].y))
    print('\nPARAMETRY TRANSFORMACJI')
    print('a = {:<.10f}'.format(tr.a))
    print('b = {:<.10f}'.format(tr.b))
    print('c = {:<.10f} [m]'.format(tr.c))
    print('d = {:<.10f} [m]'.format(tr.d))
    print('Skala = {:<.10f}'.format(tr.skala))
    print('Kąt skręcenia = {:<.10f} [grad]\n'.format(tr.teta))
    print('PUNKTY STAŁE PO TRANSFORMACJI')
    pkt = copy.deepcopy(tr.pkt_potrans)
    stale =[]
    przemieszczone = []
    for i in pkt:
        tmp = f.szukaj(i.nr, tr.P)
        if tmp == 'brak':
            przemieszczone.append(i)
        else:
            stale.append(i)
    dl_sr = 0
    for i in stale:
        dl_sr += i.dl
    dl_sr = dl_sr / len(stale)
    if par == 'q':
        print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\t{:<13s}'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]','dx [mm]', 'dl [mm]', 'q'))
        print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]', 'Mdl [mm]'))
    elif par == 'dl':
        print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]','dx [mm]', 'dl [mm]'))
        print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]'))
    if par == 'q':
        for j in stale:
            if dok == 0:
                print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 1:
                print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 2:
                print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 3:
                print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 4:
                print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 5:
                print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 6:
                print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', j.y, j.Y, j.dy), end='')
            if dok_bl == 0:
                print('\t{:<10.0f}'.format(j.MP))
            elif dok_bl == 1:
                print('\t{:<10.1f}'.format(j.MP))
            elif dok_bl == 2:
                print('\t{:<10.2f}'.format(j.MP))
            elif dok_bl == 4:
                print('\t{:<10.3f}'.format(j.MP))
    else:
        for j in stale:
            if dok == 0:
                print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 1:
                print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 2:
                print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 3:
                print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}'.format(j.nr, j.x, j.X, j.dx, j.dl))
                print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', j.y, j.Y, j.dy))
            elif dok == 4:
                print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', j.y, j.Y, j.dy))
            elif dok == 5:
                print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', j.y, j.Y, j.dy))
            elif dok == 6:
                print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', j.y, j.Y, j.dy))
    print('\nPrzemieszczenie średnie na punktach stałych:')
    print('DL_ŚR = {:<.4f} [mm]\n'.format(dl_sr))
    print('PUNKTY PRZEMIESZCZONE')

    if par == 'q':
        print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}\t{:<13s}'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]','dx [mm]', 'dl [mm]', 'q'))
        print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}'.format('', 'Y_aktualne [m]', 'Y_wtórne [m]', 'dy [mm]', 'Mdl [mm]'))
    elif par == 'dl':
        print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t{:<13s}'.format('Nr_pkt', 'X_aktualne [m]', 'X_wtorne [m]','dx [mm]', 'dl [mm]'))
        print('{:<8s}\t{:<15s}\t{:<15s}\t{:<10s}\t'.format('', 'Y_aktualne [m]', 'Y_wtorne [m]', 'dy [mm]'))

    if par == 'q':
        for j in przemieszczone:
            if dok == 0:
                print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 1:
                print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 2:
                print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 3:
                print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 4:
                print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 5:
                print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', j.y, j.Y, j.dy), end='')
            elif dok == 6:
                print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl,j.q))
                print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', j.y, j.Y, j.dy), end='')

            if dok_bl == 0:
                print('\t{:<10.0f}'.format(j.MP))
            elif dok_bl == 1:
                print('\t{:<10.1f}'.format(j.MP))
            elif dok_bl == 2:
                print('\t{:<10.2f}'.format(j.MP))
            elif dok_bl == 4:
                print('\t{:<10.3f}'.format(j.MP))

    else:
        for j in przemieszczone:
            if dok == 0:
                print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}\t{:<13.0f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.0f}\t{:<15.0f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 1:
                print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}\t{:<13.0f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.1f}\t{:<15.1f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 2:
                print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}\t{:<13.0f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.2f}\t{:<15.2f}\t{:<10.0f}'.format('', j.y, j.Y, j.dy))
            elif dok == 3:
                print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}\t{:<13.1f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.3f}\t{:<15.3f}\t{:<10.1f}'.format('', j.y, j.Y, j.dy))
            elif dok == 4:
                print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}\t{:<13.2f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.4f}\t{:<15.4f}\t{:<10.2f}'.format('', j.y, j.Y, j.dy))
            elif dok == 5:
                print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}\t{:<13.3f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.5f}\t{:<15.5f}\t{:<10.3f}'.format('', j.y, j.Y, j.dy))
            elif dok == 6:
                print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}\t{:<13.4f}'.format(j.nr,j.x,j.X,j.dx,j.dl))
                print('{:<8s}\t{:<15.6f}\t{:<15.6f}\t{:<10.4f}'.format('', j.y, j.Y, j.dy))


#Ustawienie parametrów scieżek wejsciowych
def ust_sciezek(wejs, wyjs, wiersz):
    while   True:
        os.system('cls')
        print('')
        print('*' * 78)
        print('1.Katalog z danymi wejsciowymi: {}'.format(wejs))
        print('2.Katalog z danymi wyjsciowymi: {}'.format(wyjs))
        print('3.W pierwszym wierszu danych tytuł kolumny ( T/N ): {}'.format(wiersz))
        print('4.Powrót\n')
        tmp = input('Aby wybrać podaj odpowiednią cyfrę: ')
        if tmp == '1':
            os.system('cls')
            print('Podaj nazwę katalog z danymi wejsciowymi:')
            wejs = input()
        elif tmp == '2':
            os.system('cls')
            print('Podaj nazwę katalog z danymi wyjsciowymi:')
            wyjs = input()
        elif tmp == '3':
            os.system('cls')
            while True:
                wiersz = input('W pierwszym wierszu danych tytuł kolumny ( T/N ):').upper()
                if wiersz == 'T':
                    break
                elif wiersz == 'N':
                    break
        elif tmp == '4':
            break
    return wejs, wyjs, wiersz

#Ustalenie dokładności
def dokladnosc(dok, dok_bledow):
    while True:
        print('Aktualna dokadność współrzędnych [m]: {}'.format(dok))
        print('Aktualna dokadność błędów [mm]: {}'.format(dok_bledow))
        print('1.Zmiana dokładności')
        print('2.Powrót')
        tt = int(input('Wybierz opcję: '))
        if tt == 1:
            os.system("cls")
            while True:
                dok = int(input('Podaj dokładność współrzędnych w [m] od 0 do 6 miejsc po przecinku: '))
                if dok>=0 and dok <=6:
                    break
            while True:
                dok_bledow = int(input('Podaj dokładność błędów w [mm] od 0 do 4 miejsc po przecinku: '))
                if  dok_bledow>=0 and dok_bledow <=4:
                    break
        elif tt == 2:
            break
    return dok , dok_bledow

#ustalenie parametru decyzyjnego
def parametr_decyzyjny(parametr_sortowania, q_max, dl_max):
    while   True:
        print('')
        print('*' * 78)
        print('1.Parametr decyzyjny: {}'.format(parametr_sortowania))
        if parametr_sortowania == 'q':
            print('2.Q_MAX = {}'.format(q_max))
        else:
            print('2.DL_MAX = {}'.format(dl_max))
        print('3.Powrót')
        print('*' * 78)
        t = int(input('Wybierz opcje: '))
        if t == 1:
            os.system("cls")
            print('Jak parametr decyzyjny zastosować:\n1.Q_MAX\n2.DL_MAX')
            while True:
                tmp = input('Aby wybrać naciśnij 1 lub 2: ')
                if tmp == '1':
                    parametr_sortowania = 'q'
                    break
                elif tmp == '2':
                    parametr_sortowania = 'dl'
                    break
        elif t == 2:
            os.system("cls")
            if parametr_sortowania == 'q':
                print('Q_MAX = {}'.format(q_max))
                q_max = float(input('Podaj wartość Q_MAX: '))
            elif parametr_sortowania == 'dl':
                print('DL_MAX = {}'.format(dl_max))
                dl_max = float(input('Podaj wartość DL_MAX: '))
        elif t == 3:
            break
    return parametr_sortowania, q_max, dl_max

#Komunikat główny
def komunikat_glowny(wejs, wyjs, wiersz, dok, dok_bledow, parametr_sortowania, q_max, dl_max):
    while True:
        os.system("cls")
        print('*'*78)
        print('1.Ustalenie sciezek plików')
        print('2.Ustawienie dokładności wyświetlania')
        print('3.Wybór parametru decyzyjnego')
        print('4.START')

        print('*' * 78)
        t = int(input('Uruchom opcje: '))

        if t == 1:
            os.system("cls")
            wejs, wyjs, wiersz = ust_sciezek(wejs, wyjs, wiersz)
        elif t == 2:
            os.system("cls")
            dok, dok_bledow = dokladnosc(dok, dok_bledow)
        elif t == 3:
            os.system("cls")
            parametr_sortowania, q_max, dl_max = parametr_decyzyjny(parametr_sortowania, q_max, dl_max)
        elif t == 4:
            break
    return wejs, wyjs, wiersz, dok, dok_bledow, parametr_sortowania, q_max, dl_max