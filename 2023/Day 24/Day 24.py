class Hailstone():
    def __init__(self, inputstring):
        coords, speeds = inputstring.strip().split(' @ ')

        self.coords = [int(i) for i in coords.split(', ')]
        self.speeds = [int(i) for i in speeds.split(', ')]

    def clash1(self, other):
        x1, y1, z1 = self.coords
        x2, y2, z2 = other.coords

        vx1, vy1, vz1 = self.speeds
        vx2, vy2, vz2 = other.speeds

        d1 = vy1/vx1
        d2 = vy2/vx2

        divisor = (1 - d2/d1)
        if divisor == 0:
            return False

        y = (y2 - d2*x2 + d2*(x1-1/d1*y1))/divisor
        x = (x2 - 1/d2*y2 + 1/d2*(y1-d1*x1))/(1-d1/d2)

        # Check if they will cross in the future:
        t1 = (y-y1)/vy1
        t2 = (y-y2)/vy2

        if t1>=0 and t2>=0:
            if 200000000000000 <= x <= 400000000000000 and \
                200000000000000 <= y <= 400000000000000:
                    return True


    def __repr__(self):
        return f"Coords: {self.coords}, speed: {self.speeds}"


class Rock:
    def __init__(self, speeds):
        self.speeds = speeds


    def calcCoords(self, stone1, stone2):

        x1, y1, z1 = stone1.coords
        x2, y2, z2 = stone2.coords

        vxs, vys, vzs = self.speeds
        vx1, vy1, vz1 = stone1.speeds
        vx2, vy2, vz2 = stone2.speeds

        if vys == vy1 or vys == vy2:
            ys = y2
            return None
            # (same for xs and x/y2)

        An = (vy2-vys)
        Ad = (vxs-vx2)
        Bn = (vx1-vxs)
        Bd = (vys-vy1)

        numerator = y2*Ad*Bd + An*(x2*Bd-x1*Bd-Bn*y1)
        denominator = 1*Ad*Bd-An*Bn

        if denominator == 0:
            return None

        ys = numerator/denominator
        xs = x1 + (y1-ys)/(vys-vy1)*(vx1-vxs)

        return (xs, ys)

    def calcZ(self, stone1):
        x1, y1, z1 = stone1.coords
        ys = self.ys

        vxs, vys, vzs = self.speeds
        vx1, vy1, vz1 = stone1.speeds
        vzs = self.vzs

        if vys == vy1:
            return None

        zs = z1 + (y1-ys)/(vys-vy1)*(vz1-vzs)
        return zs

    def checkZ(self, hailstones):
        zs = None
        for s1 in hailstones:
            if not zs:
                zs = self.calcZ(s1)
            else:
                newz = self.calcZ(s1)
                if newz and newz != zs:
                    return False
        assert zs != None
        self.zs = zs

        return True

    def checkSpeeds(self, hailstones):
        coords = None
        for s1 in hailstones:
            for s2 in hailstones:
                if not coords:
                    coords = self.calcCoords(s1, s2)
                else:
                    c = self.calcCoords(s1, s2)
                    if c and c!=coords:
                        return False
        assert coords != None

        self.xs, self.ys = coords
        return True


def findStartingPoint(hailstones):
    for vx in range(-300, 300):
        for vy in range(-300, 300):
            r = Rock([vx, vy, 2])
            if r.checkSpeeds(hailstones):

                for vz in range(-300, 300):
                    r.vzs = vz
                    if r.checkZ(hailstones):

                        return r
    return None


file = open('input.txt').readlines()
ans1 = ans2 = 0

hailstones = []

for line in file:
    s = Hailstone(line)
    for s1 in hailstones:
        if s.clash1(s1):
            ans1 += 1
    hailstones.append(s)

r = findStartingPoint(hailstones)

print('The answer to part 1: ', ans1)
print('The answer to part 2: ', int(r.xs + r.ys + r.zs))
