# Assignment 4
data = input("Enter user profile: ")
data_list = data.split(" ")
# print(data_list)
if len(data_list) % 2 != 0:
    ask = input(f"Do you want to add a value for {data_list[-1]}, Type y for Yes or n for No: ").lower()
    if ask == "y":
      enter_value = input("Enter a value: ")
      data_list.append(enter_value)
    else:
      data_list.remove(data_list[-1])

for data in range(len(data_list)):
  if data_list[data].isnumeric() == True:
    data_list[data] = int(data_list[data])
  else:
    index_pnt = data_list[data].find(".")
    if data_list[data][:index_pnt].isnumeric() == True:
      data_list[data] = float(data_list[data])
    else:
      pass

paired_list = []
for d in range(0, len(data_list), 2):
  paired_list.append((data_list[d], data_list[d + 1]))
dict_list = dict(paired_list)

print(dict_list)