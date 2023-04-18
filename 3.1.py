from random import randint
count = int(input('Введите количество элементов массива: '))
array = list()
for i in range(count):
    array.append(randint(1, 10))
print(*array)
number = int(input('Введите искомое число: '))
print(f'число {number} встречается в массиве {array.count(number)} раз(а)')
