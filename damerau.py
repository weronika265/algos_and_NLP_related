import numpy as np


def modlevenstein(word1, word2):
  pl_diac = {
    'a': 'ą',
    'ą': 'a',
    'c': 'ć',
    'ć': 'c',
    'e': 'ę',
    'ę': 'e',
    'l': 'ł',
    'ł': 'l',
    'n': 'ń',
    'ń': 'n',
    'o': 'ó',
    'ó': 'o',
    's': 'ś',
    'ś': 's',
    'z': 'ż',
    'ż': 'z',
    'ź': 'z',
  }

  pl_ort = {
    'ż': 'rz',
    'rz': 'sz',
    'sz': 'ż',
    'h': 'ch',
    'u': 'ó',
    's': 'z',
  }

  wynik = -1
  waga_ort = 0

  # 2) błędy ortograficzne - 0.5
  for i in range(1, len(word1)):
    for key, value in pl_ort.items():
      if word2[i - 1] == key and (word1[i - 1] + word1[i]) == value:
        word1 = word1[:i - 1] + key + word1[i + 1:]
        waga_ort += 0.5
      elif word1[i - 1] == key and (word2[i - 1] + word2[i]) == value:
        word2 = word2[:i - 1] + key + word2[i + 1:]
        waga_ort += 0.5
      elif word1[i - 1] == key and word2[i - 1] == value:
        word2 = word2[:i - 1] + key + word2[i:]
        waga_ort += 0.5
      elif word2[i - 1] == key and word1[i - 1] == value:
        word1 = word1[:i - 1] + key + word1[i:]
        waga_ort += 0.5

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
      # 1) brak/nadmiar znaków diakrytycznych - 0.2
      elif (word1[i - 1], word2[j - 1]) in pl_diac.items():
        waga = 0.2
      elif (word2[j - 1], word1[i - 1]) in pl_diac.items():
        waga = 0.2
      else:
        waga = 1
      arr[i, j] = min(arr[i - 1, j] + 1, arr[i, j - 1] + 1,
                      arr[i - 1, j - 1] + waga)
      # 3) zamianę sąsiednich znaków, tzw. czeskie błędy - 0.5
      if i > 1 and j > 1 and word1[i - 1] == word2[j - 2] and word1[
          i - 2] == word2[j - 1]:
        waga = 0.5
        arr[i, j] = min(arr[i, j], arr[i - 2, j - 2] + waga)
    # print(arr)
    wynik = arr[ax_0 - 1, ax_1 - 1] + waga_ort

  return round(wynik, 2)


###############################################

print(modlevenstein('pierze', 'pieże'))
print(modlevenstein('smiech', 'śmiech'))
print(modlevenstein('piora', 'piórą'))
print(modlevenstein('piura', 'pióra'))
print(modlevenstein('człowiek', 'cłzoiwek'))
print(modlevenstein('zrobić', 'rzobić'))
print(modlevenstein('zima', 'źima'))
print(modlevenstein('prosiłem', 'prsoilem'))
print(modlevenstein('ćwok', 'wciok'))

# wyniki:
# 0.5
# 0.2
# 0.4
# 0.5
# 1.0
# 0.5
# 0.2
# 0.7
# 2.2
