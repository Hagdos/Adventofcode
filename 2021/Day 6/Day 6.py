file = open('input.txt').read()
fish = [int(x) for x in file.strip().split(',')]

# Create a LUT with the amount of fish of each age
d = {i:0 for i in range(7)}
for i in fish:
    d[i] += 1

age = 0
oneahead = 0
twoahead = 0

for l in range(256):
    
    p = d[age]              # Current amount of fish that spawn new fish
    
    d[age] += oneahead      # Amount of fish with this age added is the value 
    oneahead = twoahead     # from two steps ago (age is 9 on a 7 loop cycle)
    twoahead = p
    
    # Loop over all the ages; back to 0 after age 6 (cycle of 7)
    age = (age + 1)%7
    
    # After 82 loops; the onehead/twoahead have been added to the values too
    if l == 81:             
        print('The answer to part 1 is:', sum(d.values()))

# Add the two interim-values to the final answer as well
print('The answer to part 2 is:', sum(d.values())+oneahead + twoahead)
