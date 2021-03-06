# Write a program that takes in two input and returns true if they have something
# in common and false if they don't. 

otu_data = input("Enter first data here: ").lower()
drey_data = input("Enter second data here: ").lower()

if otu_data.find(" ") == -1 and drey_data.find(" ") == -1:
    if otu_data == drey_data:
        print(True)

    else:
        print(False)

elif otu_data.find(" ") == -1 and drey_data.find(" ") != -1:

    drey_data_set = set(drey_data.split(" "))

    drey_data_list = list(drey_data_set)
    
    if otu_data in drey_data_list:
        print(True)
    else:
        print(False)
elif otu_data.find(" ") != -1 and drey_data.find(" ") == -1:
    otu_data_set = set(otu_data.split(" "))
    otu_data_list = list(otu_data_set)

    if drey_data in otu_data_list:
        print(True)
        
    else:
        print(False)

else:
    otu_data_set = set(otu_data.split(" "))
    drey_data_set = set(drey_data.split(" "))

    if otu_data_set.isdisjoint(drey_data_set) == False:
        print(True)
              
    else:
        print(False)
