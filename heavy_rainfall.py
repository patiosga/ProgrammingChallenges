heights = input("Give height (e.g. 2 4 5 6 0 4) : ")
heights = [int(num) for num in heights.split()]

n = len(heights)
left_max = [0 for i in range(n)]
right_max = [0 for j in range(n)]

left_max[0] = heights[0]
right_max[n-1] = heights[n-1]

for i in range(1, n):
    if heights[i] == 0:
        left_max[i] = 0
    else:
        left_max[i] = max(left_max[i-1], heights[i])

for i in range(n-2, -1, -1):
    if heights[i] == 0:
        right_max[i] = 0
    else:
        right_max[i] = max(heights[i], right_max[i + 1])

total = 0
for i in range(1, n-1):
    total += min(left_max[i], right_max[i]) - heights[i]
    print(total, end=' ')

