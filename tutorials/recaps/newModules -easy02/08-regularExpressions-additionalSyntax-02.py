import re

catOr = re.search(r'cat|dog', 'The cat is here') ## '|' stands for OR. very versatile
periodWild = re.findall(r'..at', 'The cat in the hat went splat.') ## '.' stands for an arbitrary value/wildcard, spaces mess it up
print(catOr)
print(periodWild)

beginsWith = re.findall(r'^\d', '1 is a number') ##the carrot represnents the expression starting w an \d==int
endsWith = re.findall(r'\d$', 'The number is 2')
print(beginsWith)
print(endsWith)

phrase = "there are 3 numbers 34 inside 5 this sentence"
pattern = r'[^\d]' ##removes numbers from above sentence
print(' '.join(re.findall(pattern, phrase)))

test_phrase = "This is a string! But it has punctuation. How can we remove it?"
patternExclusion = r'[^!.? ]+'
textExclusion = ' '.join(re.findall(patternExclusion, test_phrase))
print(textExclusion) ## more complex to read fast, uses brackets for exclusion

text = "Only find the hyphen-words in this sentence. But you do not know how long-ish these words are."
patternInclusion = r'[\w]+-[\w]+'
textInclusion = ' '.join(re.findall(patternInclusion, text))
print(textInclusion)

sent1 = "Hello, would you like some catfish?"
sent2 = "Hello, would yuou like to take a catnap?"
sent3 = "Hello, have you seen this caterpillar?"
multGroup = re.findall(r'cat(fish|nap|claw)', sent2)
print(multGroup)