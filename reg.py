import re

txt = "The rain the spain"
x = re.search("^the.*spain$", txt)

print(x)
