def zera(lst):
  new_lst = []
  zeroes = 0
  lst_len = len(lst)
  for i in range(lst_len):
    if lst[i] == 0:
      zeroes += 1
    else:
      new_lst.append(lst[i])

  for i in range(zeroes):
    new_lst.append(0)

  print(new_lst)


zera([1, 0, 2, 0, 3, 4])
zera([1, 7, 0, 0, 9, 9, 3])
