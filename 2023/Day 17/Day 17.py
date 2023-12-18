import heapq

class State:
    def __init__(self, location, score, lastdirection, directioncount):
        self.location = location
        self.r, self.c = location
        self.score = score
        self.idealscore = self.idealscore()
        self.lastdirection = lastdirection
        self.directioncount = directioncount

    def idealscore(self):
        global endpoint
        return self.score + self.distance(self.location, endpoint)

    def distance(self, point, endpoint):
        return endpoint[0] - point[0] + endpoint[1] - point[1] # Manhattan distance, assuming cost 1 for each point

    def nextSteps(self, city, minsteps, maxsteps):
        nextsteps = []

        if self.directioncount < minsteps:
            dr, dc = self.lastdirection
            if 0 <= self.r+dr <= endpoint[0] and 0 <= self.c+dc <= endpoint[1]:
                nextsteps.append(State((self.r+dr, self.c+dc), self.score+city[self.r+dr][self.c+dc], self.lastdirection, self.directioncount+1))
            return nextsteps

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # If not reversed:
            if (dr, dc) == (-self.lastdirection[0], -self.lastdirection[1]):
                continue
            # If not longer than allowed
            if (dr, dc) == self.lastdirection:
                newdirectioncount = self.directioncount + 1
                if newdirectioncount <= maxsteps:
                    if 0 <= self.r+dr <= endpoint[0] and 0 <= self.c+dc <= endpoint[1]:
                        nextsteps.append(State((self.r+dr, self.c+dc), self.score+city[self.r+dr][self.c+dc], (dr, dc), newdirectioncount))
            else:
                newdirectioncount = minsteps
                if 0 <= self.r+dr*minsteps <= endpoint[0] and 0 <= self.c+dc*minsteps <= endpoint[1]:
                    newscore = self.score
                    for i in range(1, minsteps+1):
                        newscore += city[self.r+dr*i][self.c+dc*i]
                    nextsteps.append(State((self.r+dr*minsteps, self.c+dc*minsteps), newscore, (dr, dc), newdirectioncount))


        return nextsteps

    def __repr__(self):
        return f"Location: {self.location}, Score: {self.score}, Direction = {self.lastdirection}, Directioncount = {self.directioncount}"

    def __lt__(self, other):
        return self.idealscore < other.idealscore


def solve(city, startState, minsteps, maxsteps):

    seen = {(0, 0): [startState]}
    priorityHeap = [startState]
    heapq.heapify(priorityHeap)

    while priorityHeap:
        nextstate = heapq.heappop(priorityHeap)

        if nextstate.location == endpoint:
            return nextstate.score

        newstates = nextstate.nextSteps(city, minsteps, maxsteps)

        for s in newstates:
            if s.location not in seen:
                seen[s.location] = [s]
                heapq.heappush(priorityHeap, s)
            else:
                if all([s.score < os.score or s.directioncount < os.directioncount or s.lastdirection != os.lastdirection for os in seen[s.location]]):
                        seen[s.location].append(s)
                        heapq.heappush(priorityHeap, s)

    return None

file = open('input.txt').readlines()
ans1 = ans2 = 0

city = [[int(i) for i in line.strip()] for line in file]

endpoint = (len(city)-1, len(city[-1])-1)

startState = State(location=(0, 0), score=0, lastdirection=(0, 0), directioncount=100)


print('The answer to part 1: ', solve(city, startState, 1, 3))
print('The answer to part 2: ', solve(city, startState, 4, 10))