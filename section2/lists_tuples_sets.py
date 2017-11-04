grades = [77, 80, 90, 95, 100]
tuple_grades = (77, 80, 90, 95, 100) # immutable
set_grades = { 77, 80, 90, 95, 100, 100 } # unique and unordered

set_grades.add(60)
set_grades.add(60)

#print(set_grades)

## Set Operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9,11}

print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
print(your_lottery_numbers.difference(winning_numbers))
print({1, 2, 3, 4}.difference({1, 2}))

my_tuple = (10, )
print(type(my_tuple))
