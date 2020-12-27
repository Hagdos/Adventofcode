cups1 = cups[-9:]
  
end = []

for _ in range(cycles-3):
    end.append(cups[0])
    cups = cups[4:] + cups[1:4] 

# print(cups+end)  

print(time.time()-start)


for i, c  in enumerate(cups):
    assert ans1[i] == c



# list1 = cups[:-9:4]
# del cups[:-9:4]

# print(cups[10:] + cups1 + list1)

