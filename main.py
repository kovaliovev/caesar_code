ru_alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
en_alpha = 'abcdefghijklmnopqrstuvwxyz'


def ru_encode(step, text):
    result = list()
    tlist = list()
    tlist.extend(text)
    for i in range(len(tlist)):
        if tlist[i].isalpha() is False:
            result.append(tlist[i])
        elif tlist[i] in ru_alpha:
            result.append(ru_alpha[(ru_alpha.find(tlist[i]) + step) % 32])
        elif tlist[i] not in ru_alpha:
            result.append(ru_alpha[(ru_alpha.find(tlist[i].lower()) + step) % 32].upper())
    return ''.join(result)


def ru_decode(step, text):
    result = list()
    tlist = list()
    tlist.extend(text)
    for i in range(len(tlist)):
        if tlist[i].isalpha() is False:
            result.append(tlist[i])
        elif tlist[i] in ru_alpha:
            result.append(ru_alpha[(ru_alpha.find(tlist[i]) - step) % 32])
        elif tlist[i] not in ru_alpha:
            result.append(ru_alpha[(ru_alpha.find(tlist[i].lower()) - step) % 32].upper())
    return ''.join(result)


def en_encode(step, text):
    result = list()
    tlist = list()
    tlist.extend(text)
    for i in range(len(tlist)):
        if tlist[i].isalpha() is False:
            result.append(tlist[i])
        elif tlist[i] in en_alpha:
            result.append(en_alpha[(en_alpha.find(tlist[i]) + step) % 26])
        elif tlist[i] not in en_alpha:
            result.append(en_alpha[(en_alpha.find(tlist[i].lower()) + step) % 26].upper())
    return ''.join(result)


def en_decode(step, text):
    result = list()
    tlist = list()
    tlist.extend(text)
    for i in range(len(tlist)):
        if tlist[i].isalpha() is False:
            result.append(tlist[i])
        elif tlist[i] in en_alpha:
            result.append(en_alpha[(en_alpha.find(tlist[i]) - step) % 26])
        elif tlist[i] not in en_alpha:
            result.append(en_alpha[(en_alpha.find(tlist[i].lower()) - step) % 26].upper())
    return ''.join(result)


print('Вас приветствует (Де)Шифратор Цезаря!')
action = input('Какая операция вам нужна? (шифр/дешифр) \n').lower()
language = input('На каком языке ваш текст? (англ/рус) \n').lower()
step = int(input('Какой шаг сдвига вам нужен/у вас имееться? (число) \n'))
text = input('Введите текст для обработки: \n')

if action == 'шифр' and language == 'англ':
    print('Результат:')
    print(en_encode(step, text))
elif action == 'шифр' and language == 'рус':
    print('Результат:')
    print(ru_encode(step, text))
elif action == 'дешифр' and language == 'англ':
    print('Результат:')
    print(en_decode(step, text))
elif action == 'дешифр' and language == 'рус':
    print('Результат:')
    print(ru_decode(step, text))

print(input('Для завершения работы введите любое значение \n'))
