import time as t
import math
from queue import PriorityQueue

MATERIALNAMES = ('ore', 'clay', 'obsidian', 'geode')


def readInput(filename):
    file = open(filename).readlines()

    blueprints = []
    maxbots = []
    for blueprint in file:
        blueprint = blueprint.split()
        costs = {}
        maxcosts = {m: 0 for m in MATERIALNAMES}
        for i, word in enumerate(blueprint):
            if word == 'robot':
                robot = blueprint[i-1]
                costs[robot] = {}
            elif word.isnumeric():
                material = blueprint[i+1].split('.')[0]
                costs[robot][material] = int(word)
                maxcosts[material] = max(maxcosts[material], int(word))
        blueprints.append(costs)
        maxcosts['geode'] = 25 # No limit on the amount of geodebots
        # maxcosts['clay'] = maxcosts['clay']//2+3
        maxbots.append(maxcosts)

    return blueprints, maxbots


class State:
    def __init__(self, robots, material, time, endtime):
        self.robots = robots
        self.material = material
        self.time = time

        timeleft = endtime - time
        score = material['geode'] + robots['geode'] * timeleft + \
                timeleft * (timeleft-1)//2
        self.score = -score

    def __repr__(self):
        return f'Time: {self.time} minutes\n' +\
               f'Robots:\n{self.robots}\nMaterial:\n{self.material}\n'

    def nextStates(self, blueprint, maxbots, endtime):
        nextstates = []
        # Check if new robots can be made
        for robot in blueprint:
            if self.robots[robot] < maxbots[robot]: # Limit bots to maximum needed

                timeneeded = self.calcTime(robot)

                if timeneeded:
                    newtime = self.time+timeneeded
                    if newtime < endtime:
                        newrobots = self.robots.copy()
                        newrobots[robot] += 1
                        newmaterial = self.material.copy()
                        newmaterial[robot] -= 1 #Subtract one; because it takes a minute to create the robot

                        for m in MATERIALNAMES:
                            # Add newly mined material
                            newmaterial[m] += self.robots[m] * timeneeded
                            # Subtract material used for new robot
                            if m in blueprint[robot]:
                                newmaterial[m] -= blueprint[robot][m]
                        nextstates.append(State(newrobots, newmaterial, newtime, endtime))
                    else:
                        newtime = endtime
                        newrobots = self.robots.copy()
                        newmaterial = self.material.copy()
                        newmaterial['geode'] += self.robots['geode'] * (newtime - self.time)
                        nextstates.append(State(newrobots, newmaterial, newtime, endtime))

        return nextstates

    def calcTime(self, robot):
        timeneeded = 0
        possible = True
        for m in MATERIALNAMES:
            if m in blueprint[robot]:
                # Check how much time we need before we can buy this robot
                if self.robots[m]:
                    dt = math.ceil((blueprint[robot][m]-self.material[m])/self.robots[m])
                    timeneeded = max(timeneeded, dt)
                else:
                    # Skip this robot if we don't have the robots needed
                    possible = False
        if possible:
            return timeneeded
        else:
            return False


    def __gt__(self, other):
        return self.score > other.score


def createStart(endtime):
    robots = {m: 0 for m in MATERIALNAMES}
    material = {m: 0 for m in MATERIALNAMES}
    robots['ore'] = 1
    time = 0


    return State(robots, material, time, endtime)

blueprints, maxbots = readInput('input.txt')
ans1 = 0
ans2 = 1
nblueprints = 30
endtime = 24
# Part 2
# endtime = 32
# nblueprints = 3

for ID, (blueprint, maxbot) in enumerate(zip(blueprints[:nblueprints], maxbots[:nblueprints])):
    start = t.time()

    startState = createStart(endtime)
    queue = PriorityQueue()
    queue.put(startState)
    maxgeodes = 0

    while not queue.empty():
        # queue.sort()
        # index = queue.index(max(queue))
        state = queue.get()

        if state.time >= endtime:
            maxgeodes = state.material['geode']
            print('Found!')
            break

        newstates = state.nextStates(blueprint, maxbot, endtime)
        for n in newstates:
            # if n.time >= endtime:
            #     if n.material['geode'] > maxgeodes:
            #         maxgeodes = max(maxgeodes, n.material['geode'])
            #         bestState = n
            #         queu = []
            #         print('Found!')
            #         break
            # else:
            queue.put(n)

    print(f'Time: {t.time()-start:.2f} seconds')
    print(maxgeodes)

    quality = (ID+1)*maxgeodes
    ans1 += quality
    ans2 *= maxgeodes


print('The answer to part 1: ', ans1) # 1192
print('The answer to part 2: ', ans2)
