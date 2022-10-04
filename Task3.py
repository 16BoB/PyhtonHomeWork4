# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

text_file = "students.txt"
list_student = []
with open(text_file, "r", encoding='utf-8') as data:
    for i in data: 
        if '5' in i:  
            i = i.upper()
        list_student.append(i.replace('\n', ''))

with open(text_file, "w", encoding='utf-8') as data:
    for i in list_student:
        data.write(i + '\n')