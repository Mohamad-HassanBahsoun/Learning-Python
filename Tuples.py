# a tuple is a list with constraints
l = [1,2,3]

t = (1,2,3)

# tuples use () not []
# you can still index, and have multiple data types, but the main difference
# is that you cant change or add anything to it, it is unchangable
credit_card1 = (123456789, "Mo", 123)
credit_card2 = (123456789, "Jo", 123)
credit_cards = [credit_card1,credit_card2]
print(credit_cards)

person1 = ("Nancy Pants", 25, 'Pizza')

(name, age,favFood) = person1   # this is called unpacking; you also dont need the ()
print(name)                     # structured access
print(age)
print(favFood)
print()

person2 = ("Joe Job", 20, 'Pasta')
people = [person1,person2]

for name,age,favFood in people:
    print(name)
    print(age)
    print(favFood)
    print()







