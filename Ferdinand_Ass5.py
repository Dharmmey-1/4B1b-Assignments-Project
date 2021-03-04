# multiply all the entires entered from a user
enter_entries = input("Enter your entries: ")
list_entries = enter_entries.split(" ")

for num in range(len(list_entries)):
  list_entries[num] = int(list_entries[num])

multiply = 1
# print(list_entries)
for num in list_entries:
  multiply *= num

print(multiply)