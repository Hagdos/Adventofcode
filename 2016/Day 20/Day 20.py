file = open('input.txt')

blocks = []

for line in file:
    start, stop = line.strip().split('-')
    blocks.append((int(start), int(stop)))

blocks.sort()
end = 0
for start, stop in blocks:
    if start <= end + 1:
        if stop >= end:
            end = stop
    else:
        break

print("The answer to part 1:", end+1)

end = 0
openblocks = []
for start, stop in blocks:
    if start <= end + 1:
        if stop >= end:
            end = stop
    else:
        startopen = end+1
        stopopen = start-1
        end = stop
        openblocks.append((startopen, stopopen))

answer = 0
for start, stop in openblocks:
    answer += stop - start + 1

print('The answer to part 2:', answer)
