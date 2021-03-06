# Find the second highest number from the numbers given by the user 

get_data = input("Enter data here: ")

otu_num = get_data.split(" ")
print(otu_num)

# Using for loop
for d in rang(len(otu_num)):
  otu_num[d] = int(otu_num[d])
  
print(otu_num)

otu_num.sort()
print(f"The second largest number is {otu_num[-2]}")

#Using Max
# real_max = max(otu_num)

# otu_num.remove(real_max)

# print(otu_num)

# find_secmax = max(otu_num)

# print(f"the second highest number is {find_secmax}")

