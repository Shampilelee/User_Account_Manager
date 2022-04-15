# This Is The Data_Base Section 
'''
    [ BE CAREFUL WHAT YOU DO HERE ]
    [ ONE MISTAKE MAY AFFACT THE WHOLE PROGRAM ]
'''


# Create New Data_Base Here,
'''
    Where Data Will Be Writen To.
    Use These Variables Well, 
    Since They Both Refer To Different Databases.
'''
# Write Into Database With These Variables
write_user_name = open("User_Name.txt", "a")
write_user_paswd = open("User_Paswd.txt", "a")


# Create And Make Database Readable Here.
user_name_db = open("User_Name.txt", "r")
user_paswd_db = open("User_Paswd.txt", "r")


# Read Data From The Database Here.
'''
    Read Data With These Variables, 
    They Both Refer To Different Databases 
    Be Careful With The Names
'''
read_user_name = user_name_db.readlines()
read_user_paswd = user_paswd_db.readlines()

