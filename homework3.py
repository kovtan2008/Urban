# 1st try
name = "Александр"
print(name)
age = 34
print(age)
new_age = '35'
age = new_age
print(age)
is_student = name != "" and age == '35'
print(is_student)

# 2nd try
name = "Александр"
print(name)
age = 34
print(age)
new_age = 35
buf = age
age = new_age
new_age = buf
print(age)
is_student = name == "Александр" and age == 35
print(is_student)

#3rd try
name = "Александр"
print(name)
age = 34
print(age)
new_age=35
age, new_age = new_age, age
print(age)
is_student = age != name
print(is_student)