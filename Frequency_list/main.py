import csv
import re


def freq_lst(file):
  '''
  Program obliczajacy czestlotliwoscc wystapien slow
  Pobiera nazwe analizowanego pliku
  Przetwarza otrzymany tekst, tworzy slownik wystapien wyrazow
  Zwraca plik .csv z lista wystapien slow posortowanych malejaco
  '''
  with open(file, 'r', encoding='utf-8') as f:
    words = dict()
    # dla każdej linii tekstu zmniejsz litery, wyczysc niepotrzebne znaki i podziel tekst na wyrazy
    for line in f:
      line = line.lower()
      line = re.sub(r'[^a-ząćęłńóśżź ]', '', line).split(' ')
      # jesli slowo juz sie powtorzylo dodaj nowe wystapienie, wpp nowy wyraz
      for word in line:
        # !pomijaj puste slowo 🤷‍♂️
        if word == '':
          continue
        if word in words:
          words[word] += 1
        else:
          words[word] = 1

    # sortuj wyrazy malejaca po wartosci (liczbie wystapien)
    words_desc = dict(
      sorted(words.items(), key=lambda items: items[1], reverse=True))
    # utwórz nagłówki kolumn: "pozycja | wyraz | liczba_wystapien" i zapisz wyniki do pliku, w odpowiednich kolumnach
    with open('wynik2.csv', 'w+', encoding='utf-8') as output:
      headers = ['pozycja', 'wyraz', 'liczba_wystapien']
      filewriter = csv.DictWriter(output, fieldnames=headers)
      filewriter.writeheader()
      for i, (w, rep) in enumerate(words_desc.items()):
        filewriter.writerow({
          'pozycja': f'{i + 1}',
          'wyraz': f'{w}',
          'liczba_wystapien': f'{rep}'
        })


freq_lst('wiki.txt')
