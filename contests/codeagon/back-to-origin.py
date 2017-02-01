#!/bin/python3

xTreasure,yTreasure = input().strip().split(' ')
xTreasure,yTreasure = [int(xTreasure),int(yTreasure)]
n = int(input().strip())
direction = []
village = [xTreasure,yTreasure]

for direction_i in range(n):
    direction_t = [int(direction_temp) for direction_temp in input().strip().split(' ')]
    direction.append(direction_t)
    village[0] = village[0] - direction_t[0]
    village[1] = village[1] - direction_t[1]
    
print(str(village[0]) + ' ' + str(village[1]))
