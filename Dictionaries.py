# Dictionaries are good for super organized data, being really fast
# key:value
# plug in the key to provide the associated value
groceries = {'bananas':5, 'oranges':3}

print(groceries['bananas'])
print(groceries.get('oranges')) # get does not give you an error when you look for something and it is not found

contacts = {'Amy':[647, 'amy@gmail.com', 'blue'],
            'John':[289,'johnny@gmail.com', 'red'],
            'Mo':{'phone':905,'email': 'moes@gmail.com','favCol':'orange'},
            'Betsy': [416,'B@gmail.com', 'gray']
            }
print(contacts['Mo'])


print(list(groceries.items()))           # this will give you key value pairs in the dictionary
print(tuple(groceries.keys()))           # this will give you the keys in the dictionary
print(set(groceries.values()))           # this will give you the values in the dictionary
# the use of tuple,list,and set uses casting


print(groceries)
groceries.pop('bananas') # pop is used to remove items from the dictionary,
                         # if you were to prin this statement it would retrive the value then remove it
print(groceries)

# using dict.popitem will remove the last item of the dictionary
groceries['bananas']=4
groceries['apples'] = 2 # this is how we add to a dictionary
print(groceries)
groceries.popitem()
print(groceries)


print()
print(groceries)
groceries.clear() #this will clear the dictionary leaving it empty
print(groceries) 







