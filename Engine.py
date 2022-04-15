# We've Imported Variables To Be Used Later In The Program, From The 'db.py' File
from db import read_user_name, read_user_paswd
from db import write_user_name, write_user_paswd

class Pages:
    
    # We Register New Users Here
    def registor():

        register_user_name = input('\nEnter the username of your choice: ')
        # Checking If The Username, Already Exist In The Database
        while (register_user_name + '\n' in read_user_name):
             register_user_name = input('\nSorry, the username is taken kindly try another username: ')
         

        register_user_password = input('\nEnter the password: ')
        # Checking If The Password, Already Exist In The Database  
        while (register_user_password + '\n' in read_user_paswd):
            register_user_password = input('\nSorry, the password is taken, kindly try another password: ')
 

        '''
            We had problems with the 'readlines()' which returns a String list,
            So we had to put the '\n' and front and back, to stop any lackages
            Or error in the program.
        '''
        write_user_name.write(f'\n{register_user_name}\n')
        write_user_paswd.write(f'\n{register_user_password}\n')

        print("---------------------------------------")
        print(" || You're Successfully Registered || ")
        print("---------------------------------------")





    # The Login Section
    '''
        We Make Sure Only Registered Users, 
        Should Access The Whole Program With Their Login Details,
        We Also Added '\n' To The 'login_user_name' Below, To Prevent 
        The Program From Blocking Registered Users, From Accessing 
        The Whole Program, And Their Personal Data.
    '''
    def log_in():

        # User Name
        login_user_name = input('\nEnter your username: ')
        while not(login_user_name + '\n' in read_user_name) or login_user_name == "":
             login_user_name = input('\nSorry, the username is not known kindly try again: ')
         

        # User Password
        login_user_password = input('\nEnter your password: ')
        while not(login_user_password + '\n' in read_user_paswd) or login_user_password == "":
            login_user_password = input('\nSorry, the password is not known, kindly try again: ')

           
        print('\n || Login Is Successful ||')

