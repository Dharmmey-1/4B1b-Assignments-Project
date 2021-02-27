get_num = input("Enter number here ")
otu_num = int(get_num)

if (otu_num % 9 == 0) and (otu_num % 13 == 0) and (otu_num % 17 == 0) and (otu_num % 21 == 0):
    print(f"The integer {otu_num} is a multiple of 9, 13, 17 and 21")

elif (otu_num % 9 == 0) and (otu_num % 11 == 0):
    print(f"The integer {otu_num} is a multiple of 9 and 11")

elif (otu_num % 13 == 0) and (otu_num % 17 == 0):
    print(f"The integer {otu_num} is a multiple of 13 and 17")

elif (otu_num % 11 == 0):
    print(f"The {otu_num} is a multiple 11")

else:
    print(otu_num)
