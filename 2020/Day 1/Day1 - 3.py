f = open('codes.txt')

numbers = [int(line.strip()) for line in f]

# for a in f:
#     numbers.append(int(a.strip()))

for i, a in enumerate(numbers):
    for j, b in enumerate(numbers[i:]):
        if a+b == 2020:
            print(a*b)
            
        
        for c in numbers[j:]:
            if a+b+c == 2020:
                print(a*b*c)
                break
                