

# import random


# creating a standard list

nlist = [23, 65, 12, 87, 98, 12, 99, 101, 21, 28]
found = False # found is a boolean variable


# comprehension list

#nlist = [random.randrange(1, 100) for x in range(500)]


# ask user for search term
searchTerm = int(input("Enter a search term: "))

# create loop to search through each data element

for item in nlist:
    if searchTerm == item:
        found = True
       

# sets some conditions for what happens to the found variable
if found == True:
    print("Found data item")

else:
    print("Not found data item")
