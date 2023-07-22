# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX_DIV = 16

num = int(input("Введите число: "))

process_num = num
res = ''

while process_num > 0:
    process_num, digit = divmod(process_num, HEX_DIV)
    if digit < 10:
        res = str(digit) + res
    else:
        match digit:
            case 10:
                res = 'a' + res
            case 11:
                res = 'b' + res
            case 12:
                res = 'c' + res
            case 13:
                res = 'd' + res
            case 14:
                res = 'e' + res
            case 15:
                res = 'f' + res

print(f"""Число {num} в шестнадцатеричном представлении = {res}. Проверка черех hex = {hex(num)}.""")