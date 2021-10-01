file = open('input.txt').readlines()

data = [x.strip().split() for x in file]

ans1 = ans2 = 0

factorA = 16807
factorB = 48271

valueA = 512
valueB = 191

# # Test values
# valueA = 65
# valueB = 8921

divisor = 2147483647

# for _  in range(40000000):
#     valueA = (valueA * factorA) % divisor
#     valueB = (valueB * factorB) % divisor
    
#     if valueA%(2**16) == valueB%(2**16):
#         ans1 += 1

# Part 2
valueA = 512
valueB = 191

# # Test values
# valueA = 65
# valueB = 8921

for _ in range(5000000):
    valueA = (valueA * factorA) % divisor
    while valueA%4:
        valueA = (valueA * factorA) % divisor
        
    valueB = (valueB * factorB) % divisor
    while valueB % 8:
        valueB = (valueB * factorB) % divisor
        
    if valueA%(2**16) == valueB%(2**16):
        ans2 += 1

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)