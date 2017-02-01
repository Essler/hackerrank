#!/bin/python3

n,c = input().strip().split(' ')
n,c = [int(n),int(c)]
matchboxes = []
matchcount = 0

for crate_i in range(c):
    crate_t = [int(crate_temp) for crate_temp in input().strip().split(' ')]
    for matchbox in range(crate_t[0]):
        matchboxes.append(crate_t[1])

matchboxes = sorted(matchboxes, reverse=True)

for matchbox_i in range(n):
    matchcount += matchboxes[matchbox_i]

print(matchcount)
