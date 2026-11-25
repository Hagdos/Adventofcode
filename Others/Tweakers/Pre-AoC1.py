# Refers to https://gathering.tweakers.net/forum/list_message/84049348#84049348

def runSanta(initialgifts):
	streetlength = len(gifts)
	steps = 0
	taken = [0]*streetlength
	stack = 1
	while stack:
		stack = numberofgifts(steps, initialgifts, taken, streetlength)
		taken[steps%streetlength] += stack+1
		steps += stack+1
	
	return steps-1


def numberofgifts(steps, initialgifts, taken, streetlength):
	return initialgifts[steps%streetlength] - taken[steps%streetlength] + (steps // streetlength)

file = open('Others/Tweakers 27nov/input.txt').read()
gifts = [int(x) for x in file.strip().split(' ')]

print('The answer to part 1: ', runSanta(gifts))
print('The answer to part 2: ', runSanta([x * 2025 for x in gifts]))

