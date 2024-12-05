import re
totalsum = 0
with open('input/daythreeinput.txt') as f:
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", f.read())
for match in matches:
    x, y = map(int, match)
    totalsum+=x*y
print(totalsum)