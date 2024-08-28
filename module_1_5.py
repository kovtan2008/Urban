immutable_var = 1, "Food", True, 1.5
print(immutable_var)
# immutable_var[0] = 2 # в кортеже нет списка, все остальные элементы не изменяемые
mutable_list = ([15, 32, 'Letter', 'Flood'])
mutable_list[0] = [22]
mutable_list[1] = [88]
mutable_list[2] = ['Home']
mutable_list[3] = ['Take']
print(mutable_list)
