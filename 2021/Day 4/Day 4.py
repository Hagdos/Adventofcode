
# Bingocard class; with rows and oolumns
class Card():
    def __init__(self, numbers):
        self.rows = numbers
        self.columns = [list(x) for x in zip(*numbers)]
        self.won = False

    # Remove the number from all rows and columns
    def removeNumber(self, number):
        for r in self.rows+self.columns:
            if number in r:
                r.remove(number)
        return self.checkCard()
        
    # Check all rows and columns to see if they're empty. 
    # Empty row or column means the card has wone
    def checkCard(self):
        for r in self.rows+self.columns:
            if not r:
                return(self.answer())
        return None
                
    # Run if the card has won; return the sum of all remaining values
    # and set to won
    # If it already won before; ignore this answer
    def answer(self):
        if self.won == False:
            self.won = True
            a = 0
            for r in self.rows:
                for c in r:
                    a += int(c)
                    
            return(a)
        else:
            return None

file = open('input.txt').readlines()
data = [x.strip().split() for x in file]
ans1 = ans2 = 0

# Numbers that are drawn
callnumbers = data[0][0].split(',')
cards = []
numbers = None

# Read all other lines
for line in data[1:]:
    # At an empty line; create a new bingocard from the previous lines
    if line == []: 
        if numbers:
            cards.append(Card(numbers))
        numbers = []
    # At a non-empty line; add this line to the next card
    else:
        numbers.append(line)
        
# Add the last card to the stack
cards.append(Card(numbers))


points = []
# Check every number in the draw list
for n in callnumbers:
    # Remove cards that have already won from the stack of cards
    cards = [c for c in cards if not c.won]
        
    # Remove the drawn number from all cards
    for c in cards:
        s = c.removeNumber(n)
        if s: # If a card has won; append the points to the list
            points.append(s*int(n))

# Correct answers are the first and last card to win
print('The answer to part 1: ', points[0])
print('The answer to part 2: ', points[-1])
