from z3 import Int, Solver

hail = [[int(i) for i in l.replace('@',',').split(',')]
                for l in open('input.txt')]

rocklocation = [Int('x'), Int('y'), Int('z')]
rockspeed = [Int('dx'), Int('dy'), Int('dz')]
time = [Int('t1'), Int('t2'), Int('t3')]

s = Solver()

# s.add(rocklocation[0] == hail[0][0] + (hail[0][3]-rockspeed[0]) * time[0],
#       rocklocation[1] == hail[0][1] + (hail[0][4]-rockspeed[1]) * time[0],
#       rocklocation[2] == hail[0][2] + (hail[0][5]-rockspeed[2]) * time[0],

#       rocklocation[0] == hail[1][0] + (hail[1][3]-rockspeed[0]) * time[1],
#       rocklocation[1] == hail[1][1] + (hail[1][4]-rockspeed[1]) * time[1],
#       rocklocation[2] == hail[1][2] + (hail[1][5]-rockspeed[2]) * time[1],

#       rocklocation[0] == hail[2][0] + (hail[2][3]-rockspeed[0]) * time[2],
#       rocklocation[1] == hail[2][1] + (hail[2][4]-rockspeed[1]) * time[2],
#       rocklocation[2] == hail[2][2] + (hail[2][5]-rockspeed[2]) * time[2],
#     )

[[s.add(rocklocation[i] == hail[j][i] + (hail[j][i+3]-rockspeed[i]) * time[j]) for j in range(3)] for i in range(3)]

print(s.check())
a = s.model()

print(sum([a[rocklocation[i]].as_long() for i in range(3)]))


# s = z3.Solver()
# s.add(*[rock[d] + rock[d+3] * t == hail[d] + hail[d+3] * t
#         for t, hail in zip(time, hail) for d in range(3)])
# s.check()

# print(s.model().eval(sum(rock[:3])))