## Assignment 2
enter_num = input("Enter your number: ")
enter_num = int(enter_num)

if (enter_num % 9==0) and (enter_num % 13==0) and (enter_num % 17==0) and (enter_num % 21==0):
  print("Your number is a multiple of 9, 13, 17 and 21")

elif (enter_num % 9 ==0) and (enter_num % 11==0):
  print("Your number is a multiple of 9 and 11")

elif (enter_num % 13==0) and (enter_num % 17==0):
    print("Your number is a multiple of 13 and 17")

elif (enter_num % 11==0):
    print("Your number is a multiple of 11")

else:
  print(enter_num)