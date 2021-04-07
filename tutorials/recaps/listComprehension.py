mystring = 'hello'

## mylist = []
## for letter in mystring:
##    mylist.append(letter)

mylist = [letter for letter in mystring]

for letter in mylist:
    print(letter,end="")