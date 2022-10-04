# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

user_num = int(input("Введите число: "))
factors = []
factor = 2
save_num = user_num
while factor * factor <= user_num:
        if user_num % factor == 0:
            factors.append(factor)
            user_num//=factor
        else:
            factor += 1
factors.append(user_num)

print(factors)