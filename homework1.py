print(len("ЮркийТрамп"))  # Мне лень считать количество символов и я воспользовался шпорой из вводного курса

# Тут начало практического задания

example = "ЮркийТрамп"  # Не, ну реально, БорисХренПопадешь
print(example[0])  # Первый символ
print(example[-1])  # Последний символ через отрицательное значение, но мы то знаем, что символов 10, так что можно и иначе
print(example[5:10])  # 5 последних символов
print(example[::-1])  # Основной вариант для реверса
print(''.join(reversed("ЮркийТрамп")))  # А можно и так
print(example[1::2])  # Каждый второй символ
