def dense(sparse):
    dense = []
    for block in range(16):
        value = 0
        for element in range(16):
            value = value ^ sparse[block*16+element]

        dense.append('{:02x}'.format(value))
    return dense


lengths = open('Day 10/input.txt').read().strip().split(',')
lengths = [int(length) for length in lengths]
turns = 0
skip = 0
string = list(range(0, 256))

for length in lengths:
    # Flip the first part of the string
    part1 = string[:length]
    part1.reverse()
    string = part1 + string[length:]

    # Update the first position:
    jump = (length + skip) % len(string)
    string = string[jump:] + string[:jump]
    skip += 1

    # Calculate how far the string has turned:
    turns += jump

# Reverse back to position 0:
turns = turns % len(string)
string = string[-turns:] + string[:-turns]

ans1 = string[0] * string[1]

print('The answer to part 1: ', ans1)


# Part 2
lengths = open('Day 10/input.txt').read().strip()
lengths = [ord(char) for char in lengths] + [17, 31, 73, 47, 23]

turns = 0
skip = 0
string = list(range(0, 256))
for _ in range(64):
    for length in lengths:
        # Flip the first part of the string
        part1 = string[:length]
        part1.reverse()
        string = part1 + string[length:]

        # Update the first position:
        jump = (length + skip) % len(string)
        string = string[jump:] + string[:jump]
        skip += 1

        # Calculate how far the string has turned:
        turns += jump

# Reverse back to position 0:
turns = turns % len(string)
string = string[-turns:] + string[:-turns]

densehash = dense(string)

hash = ''.join(densehash)
print(hash)
print('The answer to part 2: ', hash)
