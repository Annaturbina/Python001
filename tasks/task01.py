numbers = input("Введите трехзначное число: ")
lst = [int(i) for i in str(numbers)]
print("Сумма цифр в числе =",lst[0] + lst[1] + lst[2])