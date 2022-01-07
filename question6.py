my_list = ['hello', 1, 2, 5, 'world', 250, 23.0]

###########     copy()        ##############

my_list_copy = my_list.copy()
print(my_list_copy)

###########     insert()        ##############

my_list.insert(2, 'python')

print(my_list)

###########     append()        ##############

my_list.append('dart')
print(my_list)

###########     extend()        ##############

second_list = [12, 888, 'php', 'c++', 'java']

my_list.extend(second_list)
print(my_list)

###########     sort()        ##############

my_list.sort(key=lambda x: str(x))
print(my_list)

###########     pop()        ##############

poped_item = my_list.pop(2)

print('poped item', poped_item)
print(my_list)

###########     clear()        ##############

my_list.clear()
print(my_list)

###########     sum()        ##############

numbers_list = [10, 5, 23, 15, 11 ,3]

print(sum(numbers_list))

###########     min()        ##############

print(min(numbers_list))

###########     max()        ##############

print(max(numbers_list))