# Write a program that takes in data from the user, pairs them and returns the data in dictionary format.
# If there's a key without value, ask the user what action to take on that key. 

data = input("Enter user data here: ")
data_list = data.split(" ")
# print(data_list)

if len(data_list) % 2 != 0:
    inquire = input(f"Do you want to add value for {data_list[-1]}, type y for Yes or n for No: ").lower()

    if inquire == "y":
        enter_value = input("Enter a value: ")
        data_list.append(enter_value)

    else:
         data_list.remove(data_list[-1])

for kite in range(len(data_list)):
    if data_list[kite].isnumeric() == True:
        data_list[kite] = int(data_list[kite])

    else:
        pass

paired_list = []
for b in range(0, len(data_list), 2):
    paired_list.append((data_list[b], data_list[b + 1]))
dict_list = dict(paired_list)

print(dict_list)








