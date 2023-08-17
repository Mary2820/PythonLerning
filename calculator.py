a = int(input("Введите первое число: "))
b = input("Выберите действие: ")
c = int(input("Введите второе число: "))

if b == "+":
    result = int(a + c)
if b == "-":
    result = int(a - c)
if b == "*":
    result = int(a * c)
if b == "/":
        try:
            result = int(a / c)
        except ZeroDivisionError:
            result = 0
            print("На 0 делить нельзя")
print("Результат: " + str(result))



