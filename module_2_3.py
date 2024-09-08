my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
print('Список', my_list)
print('Положительные числа:')

while count < len(my_list):
    number = my_list[count]
    count = count + 1
    if number == 0:
        continue
    elif number < 0:
        print('Отрицательное значение:', number)
        break
    elif count == len(my_list):
        print(number)
        print('Конец')
    else:
        print(number)
