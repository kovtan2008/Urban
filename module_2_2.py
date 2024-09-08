print(f'Давай немножко в цифры! ')
from time import sleep
sleep(0.8)
enter = input('Согласен? ')
if enter.lower() != 'да':
    print('Пока!')
    quit()
if enter.lower() != 'нет':
    from time import sleep
    sleep(1)
    print('Окей! Ю вонна плэй? Лэтс плэй!')
a = input('Введи первое число ')
b = input('Введи второе число ')
c = input('Введи третье число ')
if a == b and a == c and b == c:
    print('Все', 3, 'числа равны между собой')
elif a == b or a == c or b == c:
    print('Вот тут ты ввел только', 2, 'одинаковых числа')
elif a != b and a != c and b != c:
    print('Тут вообще', 0, 'одинаковых чисел, в следующий раз старайся лучше!')
