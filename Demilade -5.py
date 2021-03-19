# A program that returns the multiplication value of user input
user_int = input("Enter numbers: ")
num_list = user_int.split(" ")
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
count = 1    
for numbers in num_list:
    count *= number  
    
print(count)       
