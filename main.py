import random


while True:
    print("1. Roll the dice \n2. Exit")
    user_input = int(input("Enter your choice: "))
    if user_input == 1:
        print(f"{random.randint(1, 6)} \n\n")
    elif user_input == 2:
        break
    else:
        print("Invalid choice \n\n")
