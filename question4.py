def find_me(list_name, item_to_be_serched):
    for item in list_name:
        if item_to_be_serched == item:
            return True
    return False

my_list = ['shami', 'sami', 'usman', 'fawad', 'hamza', 'usama', 'mujtaba']

if find_me(my_list, 'sami'):
    print('Item found in list')
else:
    print('Item not found in list')
        