def unik(word):
  w = word.lower()
  dict = {}
  uniq = []

  for l in w:
    if l in dict:
      dict[l] += 1
    else:
      dict[l] = 1

  for l in dict:
    if dict[l] == 1:
      uniq.append(l)

  if len(uniq) == 0:
    return -1
  else:
    return w.find(uniq[0])


print(unik('Marmolada'))
print(unik('mamba'))
print(unik('xxx'))