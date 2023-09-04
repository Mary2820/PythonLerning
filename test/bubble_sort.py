import random


def fill_array():
    elements_count_string = input('Введите количество элементов ')
    elements_count = int(elements_count_string)

    number = random.randint(0, 50)
    numbers = [number]
    elements_count_massive = len(numbers)

    while elements_count_massive < elements_count:
        number = random.randint(0, 50)
        numbers.append(number)
        elements_count_massive = len(numbers)

    return numbers


def sort_array(array):
    lenght = len(array)
    index = 0
    iteration = 1
    while iteration < lenght:
        if array[index] > array[index+1]:
            a = array[index]
            array[index] = array[index+1]
            array[index+1] = a

        if index >= lenght - 2:
            iteration = iteration + 1
            index = 0
        else:
            index = index + 1

    return array


filled_array = fill_array()
print(filled_array)

print(sort_array(filled_array))
