list1 = [1,2,3,4,5]                           # if there are not the same number of items the shorter list takes priority
list2 = ['one','two','three','four','five']   # and will cut off the excess items

zipped = list(zip(list1,list2))
print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)

for (l1,l2) in zip(list1,list2):
    print(l1)
    print(l2)


items = ["Apple","Banana", "Orange"]
counts = [3,4,1]
prices = [.30,0.99,.55]

sentences = []
for (items,counts,prices) in zip(items,counts,prices):
    items,counts, prices = str(items), str(counts), str(prices)
    sentence = 'I bought '+ counts +' '+ items + 's for '+ prices + ' cents.'
    sentences.append(sentence)
print(sentences)

