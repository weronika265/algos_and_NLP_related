import numpy as np


def f(a, b):
    '''
  Funkcja oblicza najdluzszy wspolny podciag napisow.
  a, b: napisy do porownania
  Zwraca dlugosc najdluzszego wspolnego podciagu napisow a i b.
  '''
    LCS_len = -1

    # wymiary tablicy w pionie i poziomie
    ax_0 = len(a) + 1
    ax_1 = len(b) + 1

    arr_shape = (ax_0, ax_1)
    arr = np.zeros(arr_shape)

    # obliczanie dlugosci najdluzszego wspolnego podciagu
    for i in range(1, ax_0):
        for j in range(1, ax_1):
            if a[i - 1] == b[j - 1]:
                arr[i, j] = arr[i - 1, j - 1] + 1
            else:
                arr[i, j] = max(arr[i - 1, j], arr[i, j - 1])
        LCS_len = arr[ax_0 - 1, ax_1 - 1]

    return int(LCS_len)


def LCS(a, b):
    '''
  Funkcja oblicza podobienstwo napisow.
  a, b: napisy do porownania
  Zwraca wartosc podobienstwa napisow a i b.
  '''
    LCS_val = 1 - (f(a, b) / max(len(a), len(b)))
    # return round(LCS_val, 4)
    return LCS_val


print(LCS('pies', 'pies'))
print(LCS('granat', 'granit'))
print(LCS('orczyk', 'oracz'))
print(LCS('marka', 'ariada'))
print(LCS('kot', 'pies'))
