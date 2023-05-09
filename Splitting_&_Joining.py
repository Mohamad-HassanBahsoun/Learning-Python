problems = 'broke, pale, short, nerdy'
print(problems)

list = problems.split(", ") # we use this to split the string, what goes between the bracket
                            # is a de-limmiter so it looks for where you want to split things up
                            # This creates a list
print(list)

joined = ' and '.join(list) # for joing the de-limmiter comes first
print(joined)
csv = ', '.join(list)
print(csv)