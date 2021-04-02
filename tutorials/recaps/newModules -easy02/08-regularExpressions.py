## regex (regular expressions) allows us to search 
## for general patterns in text data!

import re

## '\d' represents arbitrary digits, format MUST be exact to what is wanted
r"(\d{3})-\d{3}-\d{4}"

text = "The agent's phone number is 408-555-1234. My phone number is 248-207-9262. Call soon!"
pattern = 'phone number'
match = re.search(pattern,text)
print(match)
matches = re.findall(pattern, text)
print(matches)

for match1 in re.finditer(pattern, text):
    print(match1.group())