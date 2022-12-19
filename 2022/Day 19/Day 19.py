import time as t

MATERIALNAMES = ('ore', 'clay', 'obsidian', 'geode')


def readInput(filename):
    file = open(filename).readlines()

    blueprints = []
    for blueprint in file:
        blueprint = blueprint.split()
        costs = {}
        for i, word in enumerate(blueprint):
            if word == 'robot':
                robot = blueprint[i-1]
                costs[robot] = {}
            elif word.isnumeric():
                material = blueprint[i+1].split('.')[0]
                costs[robot][material] = int(word)
        blueprints.append(costs)

    return blueprints


class State:
    def __init__(self, robots, material, time):
        self.robots = robots
        self.material = material
        self.time = time

        # self.score =

    def __repr__(self):
        return f'Time: {self.time} minutes\n' +\
               f'Robots:\n{self.robots}\nMaterial:\n{self.material}'

    def nextStates(self, blueprint):
        nextstates = []
        # Check if new robots can be made
        for robot in blueprint:
            costs = blueprint[robot]
            if all(costs[m] <= self.material[m] for m in costs):
                # Add a robot
                newrobots = self.robots.copy()
                newrobots[robot] += 1

                newmaterial = self.material.copy()
                for m in MATERIALNAMES:
                    # Add newly mined material
                    newmaterial[m] += self.robots[m]
                    # Subtract material used for new robot
                    if m in blueprint[robot]:
                        newmaterial[m] -= blueprint[robot][m]
                nextstates.append(State(newrobots, newmaterial, self.time+1))

        # Add newstate without new robots
        newmaterial = self.material.copy()
        for m in MATERIALNAMES:
            # Add newly mined material
            newmaterial[m] += self.robots[m]
        nextstates.append(State(self.robots, newmaterial, self.time+1))

        return nextstates

    def __gt__(self, state):
        # The current state is better when the timestamp is the same,
        # and it has more or equal robots and materials
        if self.time == state.time:
            rob = all([self.robots[r] >= state.robots[r] for r in self.robots])
            mat = all([self.material[m] >= state.material[m] for m in self.material])

            return rob and mat

        return False


blueprints = readInput('2022/Day 19/input.txt')
ans1 = ans2 = 0

for blueprint in blueprints[0:1]:
    robots = {m: 0 for m in MATERIALNAMES}
    material = {m: 0 for m in MATERIALNAMES}
    robots['ore'] = 1
    time = 0

    i = 0
    start = t.time()
    for _ in range(1):

        startState = State(robots, material, time)
        queue = [startState]
        visited = []

        maxgeodes = 0

        while queue:
            i += 1
            # print(i)
            state = queue.pop()
            # visited.append(state)

            # print(state)
            newstates = state.nextStates(blueprint)
            for n in newstates:
                if n.time >= 20:
                    maxgeodes = max(maxgeodes, n.material['geode'])
                # elif any(s > n for s in queue) or any(s > n for s in visited):
                #     pass
                else:
                    queue.append(n)

            # print(f'Queue length: {len(queue)}')

    print(i)
    print(t.time()-start)
    print(state)
    # # TODO: Create a queue with states; add states as they're generated.
    # Don't add states with time > 24. Instead; add the # of geodes to a maxnumber

    # print(startState)
    # print(startState.nextStates(blueprint))


print('The answer to part 1: ', maxgeodes)
print('The answer to part 2: ', ans2)

# possible optimizations;
# check previous states and skip ones that have the same amount of robots and same or less ores.
# E.g. create a clay robot in step 4 vs a clay robot in step 5.

# Use sets instead of dicts; defining the materialnames as constants
