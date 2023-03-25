import re
import numpy as np
from tabulate import tabulate
# from sklearn import preprocessing
# import pandas as pd


def n_grams(file, n):
  '''
    Funkcja pobiera nazwę pliku i jaki ma byc n-gram
    Analizuje i przetwarza tekst, liczy wystąpienia n-gramów
    Zapisuje do listy liczbę powtórzeń gramów
    Zmienia listy na tablicę i normalizuje dane
    Zwraca tablicę ze znormalizowanymi danymi
  '''
  with open(file, 'r') as f:
    grams = []
    freq = {}
    for line in f:
      line = line.lower()
      line = re.sub(r'[^a-ząćęłńóśżź ]', '', line)
      # z otrzymanych liter tworz n-gramy
      grams += [
        line[i:i + n] for i in range(len(line) - n + 1)
        if line[i:i + n] != '  '
      ]  # + 1, żeby dodało ostatni człon
    # Dla kolejnych gramów...
    for gram in grams:
      # ...Jeśli gram powtórzony
      if gram in freq:
        freq[gram] += 1
      # ...Jeśli gram nowy
      else:
        freq[gram] = 1
    # Sortowanie po częstości występowania gramu
    freq_desc = dict(
      sorted(freq.items(), key=lambda items: items[1], reverse=True))
    # Zostaw tylko wartości dla gramów
    grams_lst = [value for key, value in freq_desc.items()]
    grams_lst = np.array(grams_lst)
    # Normalizacja
    # grams_lst_norm = (grams_lst - grams_lst.min()) / (grams_lst.max() - grams_lst.min())
    grams_lst_norm = (grams_lst - np.min(grams_lst)) / (np.max(grams_lst) -
                                                        np.min(grams_lst))
    # normalized_arr = sklearn.preprocessing.normalize([grams_lst])
    return grams_lst_norm


def euklides(grams_x, grams_y):
  '''
    Funkcja pobiera gramy plików do porównania
    Wykonuje obliczenia dla wzoru euklidesowego
    Zwraca wynik obliczeń
  '''
  # elems = [((x - y)**2 for x, y in zip(grams_x, grams_y))]
  elems_sub = np.subtract(grams_x, grams_y)
  elems_pow = np.power(elems_sub, 2)
  elems_sum = np.sum(elems_pow)
  euklides_val = np.sqrt(elems_sum)

  return euklides_val


def taxi(grams_x, grams_y):
  '''
    Funkcja pobiera gramy plików do porównania
    Wykonuje obliczenia dla wzoru taksówkowego
    Zwraca wynik obliczeń
  '''
  # elems = [abs(x - y) for x, y in zip(grams_x, grams_y)]
  elems_sub = np.subtract(grams_x, grams_y)
  elems_abs = np.absolute(elems_sub)
  taxi_val = np.sum(elems_abs)

  return taxi_val


def maximum(grams_x, grams_y):
  '''
    Funkcja pobiera gramy plików do porównania
    Wykonuje obliczenia dla wzoru maksimum
    Zwraca wynik obliczeń
  '''
  # elems = [abs(x - y) for x, y in zip(grams_x, grams_y)]
  elems_sub = np.subtract(grams_x, grams_y)
  elems_abs = np.absolute(elems_sub)
  max_val = np.max(elems_abs)

  return max_val


def cosinus(grams_x, grams_y):
  '''
    Funkcja pobiera gramy plików do porównania
    Wykonuje obliczenia dla wzoru cosinusowego
    Zwraca wynik obliczeń
  '''
  # elems = [x * y for x, y in zip(grams_x, grams_y)]
  # cos_val = 1 - (sum(elems) / (len(grams_x) * len(grams_y)))
  elems_mult = np.multiply(grams_x, grams_y)
  elems_sum = np.sum(elems_mult)
  div_len = grams_x.size * grams_y.size
  cos_val = 1 - (elems_sum / div_len)

  return cos_val


def calculate(file_grams_search, file_grams):
  '''
    Funkcja pobiera gramy dla pliku szukanego i do porównania
    Oblicza podane wzory
    Zwraca listę wyników dla poszczególnych wzorów
  '''
  #
  file_grams_search_new = np.zeros_like(file_grams)
  i = 0
  for i in range(len(file_grams_search)):
    file_grams_search_new[i] = file_grams_search[i]
  #

  euklides_r = euklides(file_grams, file_grams_search_new)
  taxi_r = taxi(file_grams, file_grams_search_new)
  maximum_r = maximum(file_grams, file_grams_search_new)
  cosinus_r = cosinus(file_grams, file_grams_search_new)

  return [euklides_r, taxi_r, maximum_r, cosinus_r]


def merge_texts_file(files_array):
  '''
    Funkcja pobiera zestawy plików
    Łączy je w jeden o nazwie język + _merge
  '''
  file_name = files_array[0][0:3]
  with open(file_name + '_merge.txt', 'w+') as merge_file:
    for file in files_array:
      with open('teksty/' + file, 'r') as f:
        merge_file.write(f.read())


# Zestawy plików w tym samum języku
files_pol = ['pol1.txt', 'pol2.txt', 'pol3.txt']
files_eng = ['eng1.txt', 'eng2.txt', 'eng3.txt', 'eng4.txt']
files_ger = ['ger1.txt', 'ger2.txt', 'ger3.txt', 'ger4.txt']
files_ita = ['ita1.txt', 'ita2.txt']
files_fin = ['fin1.txt', 'fin2.txt']
files_spa = ['spa1.txt', 'spa2.txt']

# Połączenie plików w jeden
pol = merge_texts_file(files_pol)
eng = merge_texts_file(files_eng)
ger = merge_texts_file(files_ger)
ita = merge_texts_file(files_ita)
fin = merge_texts_file(files_fin)
spa = merge_texts_file(files_spa)

# Dzielenie na gramy
s_grams = n_grams('szukany_tekst.txt', 2)
s_same_grams = n_grams('szukany_tekst.txt', 2)

pol_grams = n_grams('pol_merge.txt', 2)
eng_grams = n_grams('eng_merge.txt', 2)
ger_grams = n_grams('ger_merge.txt', 2)
ita_grams = n_grams('ita_merge.txt', 2)
fin_grams = n_grams('fin_merge.txt', 2)
spa_grams = n_grams('spa_merge.txt', 2)

# Obliczanie wzorów
pol_comp = calculate(s_grams, pol_grams)
eng_comp = calculate(s_grams, eng_grams)
ger_comp = calculate(s_grams, ger_grams)
ita_comp = calculate(s_grams, ita_grams)
fin_comp = calculate(s_grams, fin_grams)
spa_comp = calculate(s_grams, spa_grams)

# Wypisywanie do tabeli
data = [['pl', pol_comp[0], pol_comp[1], pol_comp[2], pol_comp[3]],
        ['en', eng_comp[0], eng_comp[1], eng_comp[2], eng_comp[3]],
        ['de', ger_comp[0], ger_comp[1], ger_comp[2], ger_comp[3]],
        ['it', ita_comp[0], ita_comp[1], ita_comp[2], ita_comp[3]],
        ['fin', fin_comp[0], fin_comp[1], fin_comp[2], fin_comp[3]],
        ['spa', spa_comp[0], spa_comp[1], spa_comp[2], spa_comp[3]]]
col_names = ['unigramy', 'euklidesowa', 'taksowkowa', 'max', 'kosinusowa']
print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))

# Jaki jezyk
stats = {
  'pol':sum(pol_comp),
  'eng':sum(eng_comp),
  'ger':sum(ger_comp),
  'ita':sum(ita_comp),
  'fin':sum(fin_comp),
  'spa':sum(spa_comp),
}
lang = max(stats, key=stats.get)
print(lang)