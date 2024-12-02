from day1 import *

similarityScore = 0
repeatCount = {}

for i in rightBank:
    repeatCount[i] = repeatCount.get(i, 0) + 1

for i in leftBank:
    count = repeatCount.get(i,0)
    if count != 0:
        similarityScore += (i * count)
print(f"The similarity score is: {similarityScore}")
