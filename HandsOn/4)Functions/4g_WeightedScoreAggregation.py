n = int(input("Enter number of elements:"))
score = []
weight = []
for _ in range(n):
    score.append(int(input("Enter the score:")))
for _ in range(n):
    weight.append(float(input("Enter the weights:")))
mul = list(map(lambda x,y: x*y,score,weight))
from functools import reduce
aggregate = reduce(lambda x, y: x + y, mul, 0)
print("The Weighted score is:", aggregate)
