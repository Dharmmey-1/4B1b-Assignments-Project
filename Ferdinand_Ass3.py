# Assignment 3
# To check if two entires have similar data
first_entry = input("Enter first data: ").lower()
second_entry = input("Enter second data: ").lower()

if first_entry.find(" ") == -1 and second_entry.find(" ") == -1:
  if first_entry == second_entry:
    print(True)
  else:
    print(False)
elif first_entry.find(" ") == -1 and second_entry.find(" ") != -1:
  second_set_data = set(second_entry.split(" "))
  if first_entry in second_set_data:
    print(True)
  else:
    print(False)
elif first_entry.find(" ") != -1 and second_entry.find(" ") == -1:
  first_set_data = set(first_entry.split(" "))
  if second_entry in first_set_data:
    print(True)
  else:
    print(False)
else:
  first_set_data = set(first_entry.split(" "))
  second_set_data = set(second_entry.split(" "))
  if first_set_data.isdisjoint(second_set_data) == False:
    print(True)
  else:
    print(False)