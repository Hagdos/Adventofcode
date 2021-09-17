file = open('input.txt').readlines()

ans1 = 0
part2 = True

for line in file:
    line = line.split()

    double = False
    for n, word1 in enumerate(line):
        for word2 in line[n+1:]:
            if word1 == word2:
                double = True
                break
            if part2 is True:
                if len(word1) == len(word2):
                    anagram = True
                    for letter in word1:
                        if word1.count(letter) != word2.count(letter):
                            anagram = False
                            break
                    if anagram is True:
                        double = True
            if double is True:
                break

    if double is False:
        ans1 += 1

print('The answer to part 1:', ans1)
