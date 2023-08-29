def validity_check(text):
    if text.isdigit():
        return True
    else:
        print("Ошибка! Можно вводить только числа.")
        return False


def operation_check():
    if operation == "+" or operation == "-" or operation == "/" or operation == "*":
        return True
    else:
        print("Ошибка! Можно вводить только +, -, *, /.")
        return False


text1 = input("Введите первое число: ")
while not validity_check(text1):
    text1 = input("Введите первое число: ")
operation = input("Выберите действие: ")
while not operation_check():
    operation = input("Выберите действие: ")

text2 = input("Введите второе число: ")
while not validity_check(text2):
    text2 = input("Введите второе число: ")

value1 = int(text1)
value2 = int(text2)
if operation == "+":
    result = value1 + value2
if operation == "-":
    result = value1 - value2
if operation == "*":
    result = value1 * value2
if operation == "/":
    try:
        result = value1 / value2
        print("Результат: " + str(int(result)))
    except ZeroDivisionError:
        print("На 0 делить нельзя")
