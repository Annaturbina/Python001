n = int(input("Введи значение n: "))
m = int(input("Введи значение m: "))
k = int(input("Введи значение k: "))
if k < n*m and (k % n == 0 or k % m == 0):
  print("Yes")
else:
  print("No")