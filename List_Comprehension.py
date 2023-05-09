names = ['John','Amy','Mo','Schmidt']

l = []
for person in names:
    l.append(person)

print(l)

# this is list comprehension making our code short and simple and it can do so much more


print([person for person in names])

print([person+ ' dumped me' for person in names])

num = [1,2,3,4,5]
print([i*2 for i in num])



movies_with_ratings = {'interstellar': 9, 'dark knight': 8, '50 shades': 3, '50 shades darker': 2}
l =[]
for movie in movies_with_ratings:
    if movies_with_ratings[movie]> 6:
        l.append(movie)
print(l)

print([movie for movie in movies_with_ratings if movies_with_ratings[movie]<6])