grades = [56, 45, 200, 30]

tuple_grades = (56, 45, 30, 32)
# tuples have const size

set_grades = {6, 45, 200, 29, 402, 35, 45}  # unordered & unique: repeated values not includes

# print(sum(grades) / len(grades))

print(set_grades)

grades.append(10)  # to add an  element at the and of grades
print(grades)

tuple_grades = tuple_grades + (150,)
print(tuple_grades)

print(tuple_grades[4])

# tuple can't be changed. Follow example doesn't work:

# tuple_grades[0] = 1
# print (tuple_grades)

# set not changeable as it has random order
# set_grades[0] = 1
# print (set_grades)

set_grades.add(100)
set_grades.add(100)
print(set_grades)