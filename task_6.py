# Напишите программу банкомат.
#
#      Начальная сумма равна нулю
#      Допустимые действия: пополнить, снять, выйти
#      Сумма пополнения и снятия кратны 50 у.е.
#      Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#      После каждой третей операции пополнения или снятия начисляются проценты - 3%
#      Нельзя снять больше, чем на счёте
#      При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
#      Любое действие выводит сумму денег


balance = 0
put_counter = 0
take_counter = 0
MULTYPLICITY = 50
TAKE_PERCENT = 1.5
MIN_PERCENT = 30
MAX_PERCENT = 600
THIRD_OPER_PERCENT = 3
TAX_PERCENT = 10
MAX_BALANCE = 5000000


def work():
    global balance, put_counter, take_counter
    print("Доброе пожаловать в приложение банкомат!")
    while True:
        action = int(input("Выберите команду:\n"
                       "1 – пополнить баланс\n"
                       "2 – снять деньги\n"
                       "3 – выйти\n"))
        match action:
            case 1:
                pMoney = checkMult("Введите сумму пополнения: ")
                luxury_tax()
                balance = putMoney(pMoney)
                put_counter += 1
                if put_counter == 3:
                    thirdOper()
                    put_counter = 0
                print(f"Баланс карты: {balance} у.е")
            case 2:
                tMoney = checkMult("Введите сумму снятия: ")
                luxury_tax()
                tMoney = procMoney(tMoney)
                if tMoney <= balance:
                    balance = takeMoney(tMoney)
                    take_counter += 1
                    if take_counter == 3:
                        thirdOper()
                        take_counter = 0
                else:
                    print("На карте недостаточно денег для снятия")
                print(f"Баланс карты: {balance} у.е")
            case 3:
                print("Всего хорошего, до свидания!")
                print(f"Баланс карты: {balance} у.е")
                break
            case _:
                print("Что-то пошло нет так, введите цифру от 1 до 3")


# положить деньги
def putMoney(money):
    global balance
    balance += money
    return balance


# снять деньги
def takeMoney(money):
    global balance
    balance -= money
    return balance


# получаем деньги и чекаем на кратность 50
def checkMult(message):
    global balance
    while True:
        try:
            money = int(input(message))
            if money > 0 and money % MULTYPLICITY == 0:
                return money
            else:
                print("Сумма пополнения и снятия должна быть больше 0 и кратна 50, попробуйте ещё раз")
                print(f"Баланс карты: {balance} у.е")
        except ValueError:
            print("Ввод некорректен")


# начисление процента от суммы снятия 1.5%
def procMoney(money):
    prMoney = money / 100 * TAKE_PERCENT
    if prMoney < MIN_PERCENT:
        money += MIN_PERCENT
    elif prMoney > MAX_PERCENT:
        money += MAX_PERCENT
    else:
        money += prMoney
        print(money)
    return money


# начисление процента после каждой 3-ей операции
def thirdOper():
    global balance
    prMoney = balance / 100 * THIRD_OPER_PERCENT
    putMoney(prMoney)


# налог на роскошь
def luxury_tax(money):
    global balance
    if balance > MAX_BALANCE:
        prMoney = balance / 100 * TAX_PERCENT
        takeMoney(prMoney)


# старт
work()

