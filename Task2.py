# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

list_numbers = [1,1,1,1,2,2,2,3,3,3,4]

def get_unique_numbers(arr_numbers):
    unique_list = []
    for i in arr_numbers:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

print(get_unique_numbers(list_numbers))