def checksum(bins):
    check = 0
    for i, b in enumerate(bins):
        check += i**16*b
    return check


bins = [4,	1,	15,	12,	0,	9,	9,	5,	5,	8,	7,	3,	14,	5,	12,	3]

prevbins = [checksum(bins)]
cycles = 0
while cycles < 10000:
    cycles += 1
    # Pick the bin with the most blocks and empty it
    highestIndex = bins.index(max(bins))
    blocks = bins[highestIndex]
    bins[highestIndex] = 0

    # Add blocks to all bins (multiples of length(bins))
    increase = blocks // len(bins)
    bins = [i + increase for i in bins]

    # Add the other blocks to the right of the bins
    leftover = blocks % len(bins)
    for index in range(highestIndex+1, highestIndex+leftover+1):
        bins[index % len(bins)] += 1

    # print(bins, prevbins)
    # Check if this bin setup has been before,
    # and add the current bin setup to the list
    if checksum(bins) in prevbins:
        print('The answer to part 1:', cycles)
        print('The answer to part 2:', cycles - prevbins.index(checksum(bins)))
        break
    else:
        prevbins.append(checksum(bins))


print(bins)
