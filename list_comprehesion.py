equal_list = [x for x in range(3)]
print(equal_list)

multiply_list = [x*5 for x in range(8)]
print(multiply_list)

print([n for n in range(10) if n % 2 == 0])

people = ["Kate", "Moris", "Margo"]
people_no_matter_capitalisation = [person.strip().lower() for person in people]
print(people_no_matter_capitalisation)
