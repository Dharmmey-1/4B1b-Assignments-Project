# Write the program that tells the number of times you have a substring in a parent string.

first_entry = input("Enter parentstring here: ")
second_entry = input("Enter substring here: ")

#Using .count
count_substring = first_entry.count(second_entry)

print(f"The number of times {second_entry} appears in {first_entry} is {count_substring} ")

# Using for loop
first_entry = input("Enter parentstring here: ")
second_entry = input("Enter substring here: ")

count = 0 

for d in range(len(first_entry)):
  if second_entry == first_entry[d : d + len(second_entry)]:
    count += 1
  
  else:
    pass
  
print(f"{second_entry} is in {first_entry} {count} times")
  
    
   
