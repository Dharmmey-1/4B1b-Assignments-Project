# A program that checks for the multiple of 9 13 17 21 11 19
user_integer =  int(input("Please an integer: "))

if (user_integer % 9 == 0) and (user_integer % 13 == 0) and (user_integer % 17 == 0) and (user_integer % 21 == 0):
    print("Your integer is a multiple of 9, 13, 17, and 21") 


 elif (user_integer % 9 == 0) and (user_integer % 11 == 0 ):
    print("Your integer is a multiple of 9 and 11 ")


 elif (user_integer % 13 == 0) and (user_integer % 17 == 0):
    print("Your integer is a multiple of 13 and 17") 


 elif (user_integer % 17 == 0 ) and (user_integer % 19 == 0) :
    print("Your integer is a multiple  17 and 21")


 elif (user_integer % 11 == 0):
    print("Your integer is a a multiple of 9")   

 else:
    print(user_integer)
