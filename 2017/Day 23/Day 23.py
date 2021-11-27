import computer

# def isPrime(n):
#     for i in range(2, (n**0.5)+1):
        
def listprimes(end):
    nonprimes = set()
    for i in range(2, int(end**0.5)+1):
        if i not in nonprimes:
            np = i**2
            while np < end+1:
                nonprimes.add(np)
                np += i

    return nonprimes
                
        

file = open('input.txt').readlines()

instructions = [x.strip().split() for x in file]

# Create list of registernames (letters)
registernames = set()
for line in instructions:
    if line[1].isalpha():
        registernames.add(line[1])

# Part 1
comp = computer.Computer(registernames, instructions)
print('The answer to part 1:', comp.run1(1e5)[0])

# Part 2
# Reverse engineered the code: It adds one to reg h for every value b
# that is not a prime. b is ranged from start to end; with a stepsize of 17

start = 107900
end = 124900
ans2 = 0

nonprimes = listprimes(124900+100)

for b in range(start, end+1, 17):
    if b in nonprimes:
        ans2 += 1
        
print('The answer to part 2:', ans2)

# # Biggest loop:
# f = 1
# d = 2

#  	# Loop 2: If any d exists for which b%d == 0; with d between 2 and b; f = 0 
#  	# In other words; if b is not a prime number, f = 0
#  	while d - b > 0:
# 		e = 2

# 		# Smallest loop:
# 		# if any e exists for which d*e == b -> b%d == 0
# 		while e - b > 0:
#  			if d * e == b:
# 				f = 0
#  			e += 1

# 		d += 1

#  	if f = 0:
# 		h += 1
 	
#  	if  b-c != 0
# 		b += 17