temperatures = input("Give temperatures (e.g. 2 4 5 6 0 4) : ")
span = int(input("Give maximum span of days: "))
temperatures = [float(num) for num in temperatures.split()]

left = 0
right = 1
max_pos_diff = -1  # if this number never exceeds 0 this means there was no temperature increase
temp_len = len(temperatures)

if span <= 1:
    print("Span must be at least 2")
elif span == 2:  # if span is 2 then the days are always one after the other, so it is implemented differently
    for i in range(1, temp_len):
        diff = temperatures[i] - temperatures[i - 1]
        if diff > max_pos_diff:
            max_pos_diff = diff
else:
    while left != right:
        diff = temperatures[right] - temperatures[left]
        if diff > max_pos_diff:
            max_pos_diff = diff
        if right == temp_len - 1:  # through this the while loop will ultimately end
            left += 1  # right has reached the end and left is catching up until left = right
        elif left == right - 1:  # the pointers are side by side so the right one must go up
            right += 1
        elif left == right - span + 1:  # right - left has reached the maximum day - distance so left must go up
            # e.g. span = 3 so the two days must be at most 2 days apart
            left += 1
        elif temperatures[right] - temperatures[left + 1] >= temperatures[right + 1] - temperatures[left]:
            # this is where all the juice is at
            # the pointer that goes up is the one that makes the biggest increase in temperature in the next
            # comparison
            left += 1
        else:
            right += 1

if max_pos_diff <= 0:
    print("There was no increase in temperature")
else:
    print("Max temperature increase :", max_pos_diff, "degrees")
