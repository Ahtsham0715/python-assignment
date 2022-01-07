
my_items = [3,4,5,10,7]
print(my_items)
user_choice = input("Press 1 for Addition of list items\nPress 2 for Multiplication of list items\nPress 0 to exit program\n...")

total_prodcut = 1

if user_choice == '0':
    exit()
elif user_choice == '1':
    print(sum(my_items))
elif user_choice == '2':
    for item in my_items:
        total_prodcut = total_prodcut * item
    print(total_prodcut)    