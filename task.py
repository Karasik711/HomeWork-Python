# Задача 1: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Введите трехзначное число: ')
a = int(input())
c1 = a % 10
c2 = a % 100 // 10
c3 = a // 100
print('Сумма введенного трехзначного числа:', c1+c2+c3)