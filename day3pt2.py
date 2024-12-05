import re
totalsum = 0
enabled = True
with open('input/daythreeinput.txt') as f:
    for line in f:
        commands = re.findall(r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)", line)
        for do_dont, x, y in commands:
            if do_dont == "do()":
                enabled = True
            elif do_dont == "don't()":
                enabled = False
            elif enabled and x and y:
                totalsum+=int(x)*int(y)
print(totalsum)