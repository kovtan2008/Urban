# 1st try
a = 12
b = 1.5
c = "Python,"
d = b / a
print(c,'всего задач:',a,'затрачено часов:',b,'среднее время выполнения',d,'часа')

# 2nd try

bs = "всего задач: затрачено часов: среднее время выполнения часа" # Либо разбиваем на bs1, bs2,bs3...
print(len(bs))

print(c + bs[0:12] + str(a) + bs[12:30] + str(b) + bs[29:55] + str(d) + bs[54:]) # да, надо было разбивать XD

# 3rd try
task = 12
hours = 1.5
name = 'Python'
work_time = task / hours # 8.0

print(f"Курс: {name}, всего задач:{task}, затрачено часов: {hours}, среднее время выполнения {work_time}")
