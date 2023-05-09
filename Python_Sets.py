# Lists have [], tuples have (), sets have {}
# you cannot have duplicates in a set,
# They might not print in the order of their placement, is random

s = {'banana', 'apple'}
s.add('rasberry')   # this is how you can add to the set
s.add(4)            # you can have different data types within one set
s.add('apple')      # this is a duplicate so it was not added to the set
print(s)


# here we have a list with many duplicates, so we made the list into a set to remove the duplicates
# then we turned it back into a list
l = [1,2,2,3,3,3,4,4,4,4,4,5,5]
s2 = set(l)
print(s2)
l2 = list(s2)
print(l2)
print('----------------------------------------------------')

library1 = {'Harry Potter', 'Hunger Games', 'Lord of the Rings'}
library2 = {'Harry Potter', 'Romeo and Juliet'}

allBooks = library1.union(library2)  # union is how you bring together two sets
print(allBooks)
atBothLibraries = library1.intersection(library2)  # intersection tells us what is present in both sets
print(atBothLibraries)
diff = library1.difference(library2)   # this tells you what in lib1 is different that lib2
print(diff)

