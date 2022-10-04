# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.
alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

shift = int(input('Шаг шифровки: '))
message = input("Сообщение для ДЕшифровки: ").upper()
lang = input('Выберите язык RU/EU: ')

def caesar_cipher(step, text, language):
    result = ''
    if language == 'RU':
        for i in text:
            space = alfavit_RU.find(i)
            new_space = space + step
            if i in alfavit_RU:
                result += alfavit_RU[new_space]
            else:
                result += i
        return result

    else:
        for i in text:
            space = alfavit_EU.find(i)
            new_space = space + step
            if i in alfavit_EU:
                result += alfavit_EU[new_space]
            else:
                result += i

        return result

def caesar_decipher(step, text, language):
    result = ''
    if language == 'RU':
        for i in text:
            space = alfavit_RU.find(i)
            new_space = space - step
            if i in alfavit_RU:
                result += alfavit_RU[new_space]
            else:
                result += i
        return result

    else:
        for i in text:
            space = alfavit_EU.find(i)
            new_space = space - step
            if i in alfavit_EU:
                result += alfavit_EU[new_space]
            else:
                result += i

        return result

file = open("Salatcesar.txt", "a", encoding="utf-8")
chiphet_text = caesar_cipher(shift, message, lang)
file.write(chiphet_text + '\n')

chiphet_text = caesar_decipher(shift, chiphet_text, lang)
file.write(chiphet_text + '\n')
file.close()
