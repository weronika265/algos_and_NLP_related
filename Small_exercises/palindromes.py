def palindrom(word):
  w = word.lower()
  if w == w[::-1]:
    return True
  return False


print(palindrom('Ala'))
print(palindrom('mleko'))
print(palindrom('AViva'))
