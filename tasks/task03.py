ticket = input("Введите шестизначный номер билета: ")
lst = [int(i) for i in str(ticket)]
a = lst[0] + lst[1] + lst[2]
b = lst[3] + lst[4] + lst[5]
if a == b:
  print("Yes")
else:
  print("No")