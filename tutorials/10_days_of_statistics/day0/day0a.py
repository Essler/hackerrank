import sys
import statistics

count = sys.stdin.readline()
values = list(map(int, sys.stdin.readline().split()))

print(statistics.mean(values))
print(statistics.median(values))
print(statistics.mode(values))
