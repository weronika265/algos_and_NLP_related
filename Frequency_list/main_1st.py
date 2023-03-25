import re


def freq_lst(file):
  '''
  Program obliczajacy czestlotliwoscc wystapien slow
  Pobiera nazwe analizowanego pliku
  Przetwarza otrzymany tekst, tworzy slownik wystapien wyrazow
  Zwraca plik .csv z lista wystapien slow posortowanych malejaco
  '''
  output = open('wynik.csv', 'w+')
  with open(file, 'r') as f:
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
    # zapisz wyniki do pliku w formacie "pozycja slowo powtorzenie"
    for i, (w, rep) in enumerate(words_desc.items()):
      str = f'{i + 1} {w} {rep}\n'
      output.writelines(str)


freq_lst('wiki.txt')
