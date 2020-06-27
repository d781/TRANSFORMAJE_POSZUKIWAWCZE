from funkcje import *
from komunikaty import *
if __name__ == '__main__':
    wiersze = 1
    sciezka_wejscie = 'dane_wejsciowe/'
    sciezka_wyjscie = 'dane wyjsciowe/'

    #Import danych z pliku
    epoka0 = wczytaj(sciezka_wejscie + 'p1_współrzędnde',wiersze)
    epoka1 = wczytaj(sciezka_wejscie + 'p2_współrzędnde', wiersze)
    for ep in epoka0:
        for i, id in enumerate(ep):
            if i != 0:
                ep[i] = float(id)
    for ep in epoka1:
        for i, id in enumerate(ep):
            if i != 0:
                ep[i] = float(id)

    X, m0, covX, covO, teta, skala = parametry_Helmert([epoka1[3],epoka1[1],epoka1[2]],epoka0)
    aktualny = wspolrzedne_Helmert(X, epoka1)
    roznice = roznica_uklady(epoka0,aktualny)

    print("epoka 0")
    printt(epoka0)
    print("\nepoka 1")
    printt(epoka1)
    print("\naktualny")
    printt(aktualny)
    print('\nRoznica')
    disp(roznice)