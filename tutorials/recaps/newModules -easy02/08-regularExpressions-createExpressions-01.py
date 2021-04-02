## https://www.debuggex.com/cheatsheet/regex/python
## https://www.shortcutfoo.com/app/dojos/python-regex/cheatsheet
## ^^ pattern cheat sheets - regex
import re

text = "The agent's phone number is 408-555-1234. Call soon!"
for match1 in re.finditer(r'\d{3}-\d{3}-\d{4}', text):
    print(match1.group())

## QUANTIFIERS OF THE ABOVE
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
phone1_AreaCode = results.group(1)
print(phone1_AreaCode)