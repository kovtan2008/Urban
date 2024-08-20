#  Организация программы
my_string = input("Знаешь сколько здесь символов?")
count = len(my_string)
print("Хорошо, в твоем ответе было", count, "символа")

# Работа с методами строк

print(my_string.lower())
print(my_string.upper())
print(my_string.replace(" ", ""))
print(my_string[0])
print(my_string[-1])


#  Организация программы
my_string = input("Хочешь узнать сколько в этом тексте символов? ")
count = len("Хочешь узнать сколько в этом тексте символов?")
if my_string.lower() != "да":
    print('Ну, как хочешь, тебе же хуже...')
    quit()
if my_string.lower() != "нет":
    print("Хорошо, в том тексте было", count, "символов")

# Работа с методами строк

my_string = "Хочешь узнать сколько в этом тексте символов?"  # Почему мне заново пришлось присваивать переменную???
print(my_string.lower())
print(my_string.upper())
print(my_string.replace(" ", ""))
print(my_string[0])
print(my_string[-1])
