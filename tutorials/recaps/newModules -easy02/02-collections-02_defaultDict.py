from collections import defaultdict

d = defaultdict(lambda: 0) ## way to not break program if wrong key is inputted
d['correct'] = 100
print(d['correct'])
print(d['WRONG KEY!'])