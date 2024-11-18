grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
grades_sr = []

i = 0
for _ in grades[i]:
    result = sum(grades[i]) / len(grades[i])
    grades_sr.append(result)

    i += 1

itog = {students: grades_sr for students, grades_sr in zip(students, grades_sr)}
print(itog)