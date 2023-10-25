def bellman_ford(first, second):
    first_len = len(first)
    second_len = len(second)
    opt = [[0 for j in range(second_len + 1)] for i in range(first_len + 1)]  # first is space
    # by default because of the problem specifics
    opt[0] = [i for i in range(second_len + 1)]
    for i in range(first_len + 1):
        opt[i][0] = i
    for i in range(1, first_len + 1):
        for j in range(1, second_len + 1):
            if first[i - 1] == second[j - 1]:
                opt[i][j] = opt[i - 1][j - 1]
            else:
                opt[i][j] = min(opt[i - 1][j], opt[i - 1][j - 1], opt[i][j - 1]) + 1
    # print(opt)
    return opt[first_len][second_len]


# INPUT
associations = input("Give words associations (10 numbers corresponding to words in the newspaper) : ")
associations = [int(num) - 1 for num in associations.split()]  # 10 in total
code_words = input("Code words (10 in total) : ")  # 10 in total
code_words = code_words.split()
paper_words = input("Newspaper words (at least 10): ")  # must be n words
paper_words = paper_words.split()

# OUTPUT PHONE NUMBER
output = []
# print(code_words, paper_words, associations)
for k in range(10):
    output.append(bellman_ford(code_words[k], paper_words[associations[k]]))

print(output)
