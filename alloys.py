# returns True if alloy1 dominates alloy2, where alloy1 and 2 are 3-elements tuples
def dominates(alloy1, alloy2):
    return alloy1[1] > alloy2[1] and alloy1[2] > alloy2[2]


n = int(input("Give number of alloys: "))
print("Each entry has the structure: [ID] [Flexibility] [Conductivity]")
alloys = []
for i in range(n):
    temp = input()
    temp = temp.split()
    temp = (temp[0], float(temp[1]), float(temp[2]))  # ID, flex, cond
    alloys.append(temp)

alloys.sort(reverse=True, key=lambda x: x[2])  # sort points by conductivity from highest to lowest
# print(alloys)

dominant_ids = []
temp_dominant = alloys[0]
dominant_ids.append(alloys[0][0])  # the one with the highest conductivity is definitely a dominant
for i in range(1, len(alloys)):
    if not dominates(temp_dominant, alloys[i]):
        temp_dominant = alloys[i]  # change the last dominant for later comparisons
        dominant_ids.append(alloys[i][0])

alphabetical_order_ids = sorted(dominant_ids)  # sorted for list of strings
print(alphabetical_order_ids)
