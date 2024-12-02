leftBank, rightBank = [], []
totalDistance = 0

with open ('input/dayoneinput.txt') as f:
    for line in f:
        x = line.strip("\n").split()
        leftBank.append(int(x[0]))
        rightBank.append(int(x[1]))

leftBank = sorted(leftBank)
rightBank = sorted(rightBank)

if len(leftBank) != len(rightBank):
    raise ValueError("Lists must be of the same length")

for i, j in zip(leftBank, rightBank):
    totalDistance += abs(i-j)

print(f"The total distance is: {totalDistance}")


