from random import randint
count = int(input('Введите количество элементов массива: '))
array = list()
for i in range(count):
    array.append(randint(1, 100))
print(*array)
number = int(input('Введите искомое число: '))
result = array[0]
for i in range(1, count):
    if abs(number-array[i]) < abs(number-result):
        result = array[i]
print(f'Самый близкий по величине элемент к числу {number}: {result}')
