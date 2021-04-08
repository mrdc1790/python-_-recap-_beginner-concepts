## findall, search, split, sub <- all different functions of re
import re

txt = "The rain is in Spain"
x = re.findall("ai", txt)
y = re.search("ai", txt)
print(x)
print(y.span())