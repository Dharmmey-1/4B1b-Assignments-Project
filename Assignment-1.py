get_data = input("Enter data here: ")

otu_num = get_data.split(" ")
otu_num[0] = int(otu_num[0])
otu_num[1] = int(otu_num[1])
otu_num[2] = int(otu_num[2])
otu_num[3] = int(otu_num[3])
otu_num[4] = int(otu_num[4])

print(otu_num)

#Using .sort
otu_num.sort()

print(f"the second highest is {otu_num[-2]}")

#Using Max
# real_max = max(otu_num)

# otu_num.remove(real_max)

# print(otu_num)

# find_secmax = max(otu_num)

# print(f"the second highest number is {find_secmax}")
