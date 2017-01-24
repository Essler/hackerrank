import sys

count = map(int, sys.stdin.readline())
values = map(int, sys.stdin.readline().split())
weights =  map(int, sys.stdin.readline().split())

weightedTotal = 0
weight = 0

for v,w in zip(values,weights):
    weightedTotal += v * w
    weight += w

print("%.1f" %(weightedTotal / weight))
