import numpy as np
import time
from datetime import timedelta


def find(A, B):  # A,B tuples
    if unionfind.get(A) is None or unionfind.get(B) is None:
        return False
    return unionfind[A] == unionfind[B]


def union(A, B):  # A,B tuples
    # All the keys with value unionfind[A] must be updated to value unionfind[B]
    lakes = unionfind.keys()
    clusterA = unionfind[A]
    clusterB = unionfind[B]
    for key in lakes:
        if unionfind[key] == clusterA:
            unionfind[key] = clusterB


height = int(input("Give map height: "))  # x
length = int(input("Give map length: "))  # y

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

unionfind = dict()

lake_counter = 0
connections = 0  # number of times two lakes get connected
for i in range(1, height - 1):  # The edges are always zero
    for j in range(1, length - 1):
        if lake_map[i][j] == 1:
            if lake_map[i - 1][j] == 1 and lake_map[i][j - 1] == 1 and not find((i - 1, j), (i, j - 1)):
                union((i - 1, j), (i, j - 1))  # The lake that includes i-1,j gets the value of i,j-1
                unionfind[(i, j)] = unionfind.get((i, j - 1))
                connections += 1
            elif lake_map[i][j - 1] == 1:
                unionfind[(i, j)] = unionfind.get((i, j - 1))
            elif lake_map[i - 1][j] == 1:
                unionfind[(i, j)] = unionfind.get((i - 1, j))
            else:
                lake_counter += 1
                unionfind[(i, j)] = lake_counter


dic = dict()  # keys --> cluster, values --> size of cluster
for cluster in unionfind.values():
    if dic.get(cluster) is None:
        dic[cluster] = 1
    else:
        dic[cluster] = dic.get(cluster) + 1

sizes = list(dic.values())
sizes.sort()

# End of algorithmic steps
end_time = time.monotonic()
print("Time: ", timedelta(seconds=end_time - start_time))


print("Number of lakes", lake_counter - connections)
# If two lakes get connected then the total number of lakes
# decreases by 1
print("Sorted by size: ", sizes)
