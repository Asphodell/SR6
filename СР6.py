array = []
count = 0
try:
    n = int(input('Введите количество элементов в массиве: '))
    for i in range(n):
        array.append(int(input('Введите элемент массива: ')))
    delta = int(input('Введите DELTA: '))
except ValueError:
    print('Ошибка, введите целое число')
else:
    for j in range(len(array) - 1):
        for l in range(len(array) - j - 1):
            if array[l] > array[l + 1]:
                array[l], array[l + 1] = array[l + 1], array[l]
    for k in range(len(array)):
        if array[k] - array[0] == delta:
            count += 1
    print('Количество чисел, отличающихся от наименьшего элемента на DELTA - ', count)