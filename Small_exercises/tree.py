def tree(l, w):
  n = 1
  for i in range(l):
    print(('*' * n).center(l * w, ' '))
    m = n
    for j in range(w - 1):
      m += 2
      print(('*' * m).center(l * w, ' '))
    n += 2

  for i in range(3):
    print(('***').center(l * w, ' '))


tree(3, 4)