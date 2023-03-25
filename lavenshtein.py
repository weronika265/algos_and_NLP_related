import numpy as np


def levenshtein(word1, word2):
  '''
  Funkcja oblicza roznice miedzy wyrazami (minimalna liczbe modyfikacji do uzyskania tego samego wyrazu).
  word1, word2: wyrazy do porownania
  Zwraca roznice miedzy wyrazami.
  '''
  wynik = -1
  waga = 0

  # wymiary tablicy w pionie i poziomie
  ax_0 = len(word1) + 1
  ax_1 = len(word2) + 1

  # inicjalizacja tablicy zerami i przypisanie indeksow dla pierwszej kolumny i wiersza
  arr_shape = (ax_0, ax_1)
  arr = np.zeros(arr_shape)
  for i in range(ax_0):
    arr[i][0] = i
  for i in range(ax_1):
    arr[0][i] = i

  # obliczanie roznicy
  for i in range(1, ax_0):
    for j in range(1, ax_1):
      if word1[i - 1] == word2[j - 1]:
        waga = 0
      else:
        waga = 1
      arr[i, j] = min(arr[i - 1, j] + 1, arr[i, j - 1] + 1,
                      arr[i - 1, j - 1] + waga)
    wynik = arr[ax_0 - 1, ax_1 - 1]

  return int(wynik)


###############################################

print(levenshtein('pies', 'pies'))
print(levenshtein('granat', 'granit'))
print(levenshtein('orczyk', 'oracz'))
print(levenshtein('marka', 'ariada'))

# wynik:
# 0
# 1
# 3
# 4
