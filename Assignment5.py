# Write a program that takes in two integers, multiply them and return the result.

data = input("Enter integers here: ")
data_list = data.split(" ")
print(data_list)

for trick in range(len(data_list)):
    data_list[trick] = int(data_list[trick])


multiply = 1

for trick in data_list:
    multiply *= trick 

print(multiply)
