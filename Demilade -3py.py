# A program that checks if there are common values from two seperate user input

user_data_1 = input("Enter data: ").lower()
user_data_2 = input("Enter data: ").lower()
white_space = user_data_1.find(" ")
white_space2 = user_data_2.find(" ")


if (white_space == -1) and (white_space2 == -1):
    if user_data_1 == user_data_2:
        print("True")
    else:
        print("False")   

elif (white_space == -1) and (white_space2 != -1):
    user_data_set = set(user_data_2.split(" "))
    if user_data_1 in user_data_set:
        print(True)
    else:
        print(False)

elif (white_space != -1) and (white_space == -1):
    user_data_set = set(user_data_1.split(" "))
    if user_data_2 in user_data_set:
        print(True)
    else:
        print(False) 

else:
    user_data_set = set(white_space.split(" "))
    user_data_2_set = set(user_data_2.split(" "))

    if user_data_set.isdisjoint(user_data_set) == False:
        print(True)
    else:
        print(False)    
