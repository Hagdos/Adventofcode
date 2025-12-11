import pyperclip

def find_paths(start, end, cache):
    if start == end:
        return 1
    
    if start in cache:
        return cache[start]

    paths = sum(find_paths(s, end, cache) for s in connections[start])
    cache[start] = paths

    return paths

file = open('2025/Day 11/input.txt').readlines()

connections = {x.split(': ')[0]: x.split(': ')[1].split() for x in file}
connections['out'] = []
ans1 = ans2 = 0

# ans1 = find_paths('you', 'out', {})
# ans2 = (find_paths('svr', 'fft', {}) * find_paths('fft', 'dac', {}) * find_paths('dac', 'out', {}) + 
#         find_paths('svr', 'dac', {}) * find_paths('dac', 'fft', {}) * find_paths('fft', 'out', {}))

ans3 = find_paths_2('svr', 'out', set(), {})

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
print('The answer to part 2: ', ans3)
pyperclip.copy(ans2)

# 5701208 is too low