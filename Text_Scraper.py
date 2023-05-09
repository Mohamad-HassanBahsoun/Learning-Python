# this is what we need to specify different patterns in strings and in texts
import re

text = 'A random String'
pattern = re.compile('[BACro]+')  #placing the square bracket allows you to search for those individual characters
                                  # you could also do re.compile([a-c])  this will go from a - c
result = pattern.search(text)     # search will match with the first result found
print(result)

text2 = ' Random String'
pattern = re.compile('[a-zA-Z]+')   # this will look for conssecutive letters (basically a word and match that)
result = pattern.search(text2)
print(result)

look_for_email = 'this is what we are going to have then insert mo_123-567.321@gmail.com and then we will ' \
                 'add more to make it fun and like wha if yourname@company.ca and then we kept going'

pattern = re.compile('[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+') # we do this to look for all the consec letters that are
result = pattern.search(look_for_email)                         # before the @ after the @ bef . and after .
print(result)

result = pattern.findall(look_for_email)  # findall will look for all occurances while search only looks for the first
print (result)
