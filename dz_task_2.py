# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
# Пример:
# Ввод:
# 1/2
# 1/3
# Вывод:
# 5/6 1/6


import math
import fractions

num1 = input("Введите первую дробь: ")
num2 = input("Введите вторую дробь: ")

num1_numerator = int(num1.split("/")[0])
num1_denominator = int(num1.split("/")[1])
num2_numerator = int(num2.split("/")[0])
num2_denominator = int(num2.split("/")[1])


# функция сокращения
def cut(num1:int, num2:int)->int:
    result = math.gcd(num1, num2)
    num1 = int(num1 / result)
    num2 = int(num2 / result)
    return num1, num2


# функция сложения
def sum(numer1, denom1, numer2, denom2: int) -> int:
    if denom1 == denom2:
        result1 = numer1 + numer2
        result2 = denom1
    else:
        result1 = numer1 * denom2 + numer2 * denom1
        result2 = denom1 * denom2
    result1, result2 = cut(result1, result2)
    return result1, result2


# функция умножения
def mult(numer1, denom1, numer2, denom2: int) -> int:
    result1 = numer1 * numer2
    result2 = denom1 * denom2
    result1, result2 = cut(result1, result2)
    return result1, result2


# вывод
resultSum1, resultSum2 = sum(num1_numerator, num1_denominator, num2_numerator, num2_denominator)
print("Cложение дробей: " + str(resultSum1) + '/' + str(resultSum2))

f1 = fractions.Fraction(num1_numerator, num1_denominator)
f2 = fractions.Fraction(num2_numerator, num2_denominator)

print("Проверка сложения: " + str(f1 + f2))

resultMult1, resultMult2 = mult(num1_numerator, num1_denominator, num2_numerator, num2_denominator)
print("Умножение дробей: " + str(resultMult1) + '/' + str(resultMult2))

print("Проверка умножения: " + str(f1 * f2))
