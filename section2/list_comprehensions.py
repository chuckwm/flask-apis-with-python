my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]
multiply_list = [x * 3 for x in range(5)]
even_numbers = [ x for x in range(-5, 15) if x % 2 == 0]
print(even_numbers)

people_you_know = [ "Rolf", " John", "anna", "GREG"]
normalized_people = [person.strip().capitalize() for person in people_you_know]
print(normalized_people)
