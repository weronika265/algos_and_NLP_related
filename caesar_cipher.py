# słownik konwersji polskich liter na odpowiedniki bez znaków diakrytycznych
pl_chars = {
  'ą': 'a',
  'ć': 'c',
  'ę': 'e',
  'ł': 'l',
  'ń': 'n',
  'ó': 'o',
  'ś': 's',
  'ż': 'z',
  'ź': 'z',
}


def caesar(str, shift):
  """
  Funkcja odszyfrowujaca i zaszyfrowujaca szyfrem cezara
  pobiera napis i przesuniecie kodu
  zmienia litery, zostawia znaki. Usuwa znaki diakrytyczne dla polskich znaków przez ich konwersją
  zwraca odszyfrowany napis
  """
  c_str = ''

  for c in str:
    # jesli litera ma polski znak diakrytyczny, usun taki znak...
    if c.lower() in pl_chars:
      c_help = pl_chars[c.lower()]
      # ...dla dużej litery
      if c.isupper():
        c_str += c_help.upper()
      # ...dla malej litery
      else:
        c_str += c_help.lower()
    # przesuniecie dla duzych liter
    elif c.isupper():
      c_str += chr((ord(c) - 65 + shift) % 26 + 65)
    # przesuniecie dla malych liter
    elif c.islower():
      c_str += chr((ord(c) - 97 + shift) % 26 + 97)
    # inne znaki
    else:
      c_str += c
  return c_str


# dekodowanie
text = 'DOD PD NRWD L SLHVHŁD'
print(caesar(text, -3))

# kodowanie
text2 = 'ALA MA KOTA I PIESELA'
print(caesar(text2, 3))

print('\n -------- \n')

# brute force
# for i in range(-26, 27):
#   print(f'shift: {i}:', caesar(text, i))
