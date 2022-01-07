list_of_num = []

while True:
    user_input = input("Enter any number\nPress 'q' to exit\n")
    if user_input == 'q':
        break
    elif user_input.isdigit():
        list_of_num.append(int(user_input))
    else:
        print('Invalid input\n\n')
        
print(list_of_num)