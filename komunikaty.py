def printt(lista):
    for i in lista:
        print(i)
def printtt(lista):
    for i in lista:
        print('{:<s}\t{:<.7f}\t{:<.7f}\t{:<.7f}\t{:<.7f}\t{:<.7f}'.format(i.nr, i.x, i.y, i.mx, i.my, i.mp))

def disp(lista):
    i= ['Nr', 'Xzer', 'Yzer', 'mp zer[mm]', 'X akt', 'Y akt', 'mp akt[mm]', 'dx [mm]', 'dy [mm]', 'dl[mm]', 'ml', 'q']
    print('{:<5s}{:<10s}{:<10s}{:<12s}{:<10s}{:<10s}{:<10s}{:<10s}{:<10s}{:<10s}{:<10s}{:<10s}'.format( i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11] ))
    for i in lista:
        print('{:<5s}{:<10.4f}{:<10.4f}{:<12.3f}{:<10.4f}{:<10.4f}{:<10.3f}{:<10.3f}{:<10.3f}{:<10.3f}{:<10.3f}{:<10.3f}'.format(
            i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]
        ))
