def hamm_dist(str1, str2):
  '''
    Funkcja pobiera dwa napisy (lub konwertuje je na napisy)
    Porownuje kolejne znaki w napisach o tej samej dlugosci
    Wypisuje roznice miedzy napisami
  '''
  # Licznik roznicy w napisach
  count = 0

  # Zmiana na napis, jesli dane sa innego typu
  if type(str1) != str:
    str1 = str(str1)
  if type(str2) != str:
    str2 = str(str2)

  # Jesli napisy sa tej samej dlugosci...
  if len(str1) == len(str2):
    for i in range(len(str1)):
      # ...Zliczaj roznice w kolejnych znakach w napisach
      if str1[i] != str2[i]:
        count += 1
  print(f'{str1}\n{str1}\n{count}')


w1 = 'pies'
w2 = 'pies'
hamm_dist(w1, w2)

print('---')

w3 = 'granat'
w4 = 'granit'
hamm_dist(w3, w4)

print('---')

w5 = 1011101
w6 = 1001001
hamm_dist(w5, w6)
