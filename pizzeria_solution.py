import sys
import numpy as np

line = sys.stdin.readline()
city = list(line.strip().split(" "))
city_size = int(city[0])
store_count = int(city[1])
matrix = np.zeros((city_size, city_size))

while store_count > 0:
    store_count -= 1
    line = sys.stdin.readline().strip()
    store = list(line.split(" "))
    col = int(store[0]) - 1
    row = city_size - int(store[1])
    R = int(store[2])
    for i in range(city_size):
        for j in range(city_size):
            if (abs(row - i) + abs(col - j)) <= R:
                matrix[i][j] += 1

maxVar = int(np.amax(matrix))
print(maxVar)
