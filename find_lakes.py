import numpy as np
import time
from datetime import timedelta


def find(A, B):  # A,B tuples
    if clusters.get(A) is None or clusters.get(B) is None:  # at least one lake has not been encountered
        return False
    return clusters.get(A) == clusters.get(B)
    # if the two lakes are marked with the same cluster code then they are
    # already in the same lake


def union(A, B):  # A,B tuples
    # All the keys with value unionfind[A] must be updated to value unionfind[B]
    clusterA = clusters.get(A)
    clusterB = clusters.get(B)
    for coordinate in unionfind[clusterB]:  # unionfind[i] is a set of tuples (coordinates)
        clusters[coordinate] = clusterA
    unionfind[clusterA] = unionfind[clusterA].union(unionfind[clusterB])
    unionfind[clusterB] = set()
    # replace old cluster of B elements with an empty set because it was united with the cluster of A.
    # It is not deleted because it messes up the cluster alignment


print("Map must be at least 3x3")
height = int(input("Give map height: "))  # x
length = int(input("Give map length: "))  # y

clusters = dict()  # key: coordinate, value: position of lake set in sets of lakes --> faster union
unionfind = []  # list of sets

user_input = input("Do you want a randomly generated map? [y/n]: ")
while user_input != 'y' and user_input != 'n':
    user_input = input("Do you want a randomly generated map? [y/n]: ")

if user_input == 'y':
    lake_map = np.random.randint(low=0, high=2, size=(height, length))
    # randomized matrix height x length with 0s or 1s
    lake_map[0] = np.zeros(length)
    lake_map[height - 1] = np.zeros(length)  # cleaning out edges
    for i in range(1, height-1):
        lake_map[i][0] = lake_map[i][length - 1] = 0
    print("Your map:\n", lake_map)
else:
    print("Give your own map:")
    print("e.g\n", "000\n", "010\n", "000")
    lake_map = [[0 for i in range(length)] for j in range(height)]
    for i in range(height):
        line = input()
        lake_map[i] = [int(num) for num in list(line)]

# Record running time of the algorithm
start_time = time.monotonic()

# unionfind = dict()

lake_counter = -1
connections = 0  # number of times two lakes get connected
for i in range(1, height - 1):  # The edges are always zero
    for j in range(1, length - 1):
        if lake_map[i][j] == 1:
            if lake_map[i - 1][j] == 1 and lake_map[i][j - 1] == 1 and not find((i - 1, j), (i, j - 1)):
                union((i - 1, j), (i, j - 1))  # The lake that includes i-1,j gets the value of i,j-1
                clusters[(i, j)] = clusters.get((i - 1, j))  # (i, j) is marked with the correct set position
                unionfind[clusters[(i, j)]].add((i, j))  # (i, j) is added to the correct set of water tiles
                connections += 1
            elif lake_map[i][j - 1] == 1:
                clusters[(i, j)] = clusters.get((i, j - 1))
                unionfind[clusters[(i, j)]].add((i, j))
            elif lake_map[i - 1][j] == 1:
                clusters[(i, j)] = clusters.get((i - 1, j))
                unionfind[clusters[(i, j)]].add((i, j))
            else:
                lake_counter += 1
                clusters[(i, j)] = lake_counter  # new cluster
                unionfind.append({(i, j)})  # append new set of water tiles


sizes = [len(lake_set) for lake_set in unionfind]
sizes = [lake for lake in sizes if lake != 0]  # clean out all empty sets created in unions
sizes.sort()

# End of algorithmic steps
end_time = time.monotonic()
print("Time: ", timedelta(seconds=end_time - start_time))


print("Number of lakes", lake_counter + 1 - connections)
# If two lakes get connected then the total number of lakes
# decreases by 1
# Also add 1 because the lake counter begins form -1 for implementation purposes
print("Sorted by size: ", sizes)
