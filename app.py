# Importing Methods To Be Used In The Program
from Engine import Pages

user_choice = input("Select one of the options,\n1. Login \n2. Registor \n")

while user_choice != '1' and user_choice != '2' and user_choice != 'exit' and user_choice != 'stop' and user_choice != 'quit':
    user_choice = input("\nNot What We Expected, Kindly try again: ")


if user_choice == '1':
    Pages.log_in()
elif user_choice == '2':
    Pages.registor()
elif user_choice == 'exit' or 'stop' or 'quit':
    exit()
else:
    print("exit")

