grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_1 = sorted(students)

numb_1 = grades[0]
numb_2 = grades[1]
numb_3 = grades[2]
numb_4 = grades[3]
numb_5 = grades[4]

av_1 = sum(numb_1)/len(numb_1)
av_2 = sum(numb_2)/len(numb_2)
av_3 = sum(numb_3)/len(numb_3)
av_4 = sum(numb_4)/len(numb_4)
av_5 = sum(numb_5)/len(numb_5)

grades[0]=av_1
grades[1]=av_2
grades[2]=av_3
grades[3]=av_4
grades[4]=av_5

gpa = input("Хотите узнать средний балл ученика? ")
if gpa.lower() != "да":
    print('Тогда закройте эту программу!')
    quit()
if gpa.lower() != "нет":
    print("Хорошо, средний балл сдудентов:",students_1[0],':',grades[0],students_1[1],':',grades[1],students_1[2],':',grades[2],students_1[3],':',grades[3],students_1[4],':',grades[4])
