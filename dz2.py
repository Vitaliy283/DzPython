# Задача 2. Найдите сумму цифр трёхзначного числа.

print("Введите трёхзначное значное число: ")
num = int(input())
if num >= 100 and num <= 999:
     print(num//100 + num//10%10 + num%10)
else:
     print("Введено не трёхзначное число")