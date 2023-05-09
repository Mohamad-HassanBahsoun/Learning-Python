# Something that holds multiple things (like an array)

l1 = [100,20,46,41,5]
l2 = [1,"Hello", 2.5, True,l1]  # more than one data type is allowed
print(l1)
print(l2)
print(l2[3])

names = ["john", "mary","moses"]
print(names)
names.append("gary") # appends adds to the end of the list
print(names)
names.insert(1,"harry") # insert will place it where you like, the number specifies the position it will now be in
print(names)
names.remove("gary") # this will remove from the this, and all are case sensitive
print(names)
names.reverse() # this will reverse the order
print(names)
names.sort() # sort puts things in order
print(names)
l1.sort()
print(l1)

for i in range(len(names)):  # wea re iterating over the list goiing over it one by one 
    print((names[i]))

