# phone_book = {'Denis': 9772630100, 'Max': 9160539600}
# phone_book['Denis'] = 9104677700
# phone_book['Anton'] = 88005553535
# del phone_book['Max']
# phone_book.update({'Sasha': 9190030405,
#                    'Alex': 9205657890})
# print(phone_book.get('Kall','Такого ключа нет'))
# phone_book.pop('Anton')
# print(phone_book)
# print(phone_book.keys())
# print(phone_book.values())
# print(phone_book.items())

# set_ = {1, 2, 3, 4, 1, 2, 3, 4}
# print(set_)


# Словари

my_dict = {'Алексей': 1990,
           'Иван': 1991,
           'Роман': 1992,
           'Дмитрий': 1993}
print(my_dict.get('Иван'))
print(my_dict.get('Сергей', 'Такого имени нет в списке'))
my_dict.update({'Кирилл': 1998,
                'Стас': 2001})
my_dict.pop('Иван')
print(my_dict)

# Множества

my_set = {1, 2, 3, 1, 2, 3, 'Один', 'Один', 'Тор', 'Тор', 'Локи', 'Локи', 1.2, 1.2, 1.3, 1.3}
print(my_set)
my_set.update({5,6,5,6, 'Макрон'})
print(my_set)
my_set.remove('Локи')
print(my_set)