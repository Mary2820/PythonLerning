num_1 = 28 # глобальная переменная
num_2 = 33 # глобальная переменная
def summ():
    result = num_1 + num_2
    print(result)

def sub():
    num_1 = 66 #локальная переменная
    result = num_1 - num_2
    print(result)

summ()
sub()