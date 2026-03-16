from random import randint

numbers = [1,2,3,]

new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = 'Angela'
new_name = [letter for letter in name]
print(new_name)

range_list = [num*2 for num in range(1,5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

new_names = [name.upper() for name in names if len(name) > 5]
print(new_names)

