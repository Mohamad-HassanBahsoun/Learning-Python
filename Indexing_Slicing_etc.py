digits = [0,1,2,3,4,5,6,7,8,9]

print(digits[0])  # this is indexing, printing only what that 'position' holds
print(digits[0:3]) # the ':' will allow you to start and end where you like

name = "First Last"
print(name[:5])
print(name[6:])

print(digits[:10:2]) # this is striding the last number indicates how big the jump is btw each number

for i in range(len(digits)):
    print(digits[0:i])

# This way does work but we dont want to use -2 or +3 so we do the following
# for i in range(len(digits)-2):
#     print(digits[i:i+3])


window_size = 7
for i in range(len(digits)-(window_size-1)):    # this is more efficient because it allows you to change
    print(digits[i:i+window_size])              # the window size to what you like while giving good results
