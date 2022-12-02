file = open('2022/Day 2/input.txt').readlines()

rps_dict = {'A': 0,  # Rock
            'B': 1,  # Paper
            'C': 2,  # Scissors
            'X': 0,
            'Y': 1,
            'Z': 2,
            }

games = [[rps_dict[char] for char in line.strip().split()] for line in file]
print(games)
points = 0
for game in games:
    result = (game[1]-game[0]) % 3
    if result == 1:
        points += 6
    elif result == 0:
        points += 3
    else:
        assert result == 2
    points += game[1]+1

print('The answer to part 1: ', points)

# Part 2
# X means you need to lose, Y means you need to end the round in a draw,
# and Z means you need to win. Good luck!"
points = 0
for game in games:
    # Points for lose/draw/win are determined by the second character
    points += game[1] * 3
    if game[1] == 0:  # lose
        points += (game[0]-1) % 3 + 1
    elif game[1] == 1:  # draw
        points += game[0] + 1
    else:
        points += (game[0]+1) % 3 + 1

print('The answer to part 2: ', points)
