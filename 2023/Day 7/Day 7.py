from operator import attrgetter

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.calculateRank()
        self.cardvalues = [cardscores[c] for c in cards]
        self.jokercardvalues = [cardscores[c] if c != 'J' else 1 for c in cards]
        self.calculateRankWithJoker()

    def calculateRank(self):
        r = [self.cards.count(c) for c in self.cards]
        r.sort(reverse=True)

        self.rank = int(''.join([str(i) for i in r]))

    def calculateRankWithJoker(self):
        jokers = self.cards.count('J')

        r = [self.cards.count(c) if c != 'J' else 0 for c in self.cards]
        r.sort(reverse=True)

        highestcount = r[0]

        for c in range(highestcount):
            r[c] = highestcount+jokers
        for c in range(-1, -jokers-1, -1):
            r[c] = highestcount+jokers



        r.sort(reverse=True)

        self.jokerrank = int(''.join([str(i) for i in r]))

    def __repr__(self):
        return str((self.cards, self.jokerrank, self.bid))

cardscores = {'2': 2,
              '3': 3,
              '4': 4,
              '5': 5,
              '6': 6,
              '7': 7,
              '8': 8,
              '9': 9,
              'T': 10,
              'J': 11,
              'Q': 12,
              'K': 13,
              'A': 14}

file = open('input.txt').readlines()
data = [x.strip().split() for x in file]
hands = [Hand(c[0], c[1]) for c in data]
ans1 = ans2 = 0

hands.sort(key=attrgetter('rank', 'cardvalues'))
for rank, hand in enumerate(hands):
    ans1 += (rank+1) * hand.bid

hands.sort(key=attrgetter('jokerrank', 'jokercardvalues'))
for rank, hand in enumerate(hands):
    ans2 += (rank+1) * hand.bid

print(hands)



print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)

# 249275219 is too low