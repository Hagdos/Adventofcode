#! /usr/bin/env python

from urllib.request import Request, urlopen
import os
import webbrowser

# year = input('Year: ')
# day = input('Day: ')

year = 2023
day = 6

path = str(year) + '/Day ' + str(day)
url = 'https://adventofcode.com/' + str(year) + '/day/' + str(day)
inputurl = url + '/input'

if os.path.isdir(path):
    print('Folder already exists')
else:
    # Read input data from HTTP
    inputrequest = Request(inputurl)
    inputrequest.add_header('Cookie', 'session=53616c7465645f5fd1b146368a0b6a068fac2305df80be44e853f28e44defdf3b35cc7b49825406191bc263d8dab3b8370403074e32fe9e25b39a4496f974a0b')
    inputrequest.add_header('github.com/Hagdos/Adventofcode by yourname@example.com')
    puzzleInput = urlopen(inputrequest).read()

    # Write input data to input.txt
    os.makedirs(path)
    inputFile = open(path + '/input.txt', 'wb')
    inputFile.write(puzzleInput)
    inputFile.close()

    #Create python file
    pythonFile = open(path + '/Day ' + str(day) + '.py', 'w')
    pythonFile.write('file = open(\'input.txt\').readlines()\n\n')
    pythonFile.write('data = [x.strip().split() for x in file]\n\n')
    pythonFile.write('ans1 = ans2 = 0\n\n')
    pythonFile.write('print(data)\n\n')
    pythonFile.write('print(\'The answer to part 1: \', ans1)\n')
    pythonFile.write('print(\'The answer to part 2: \', ans2)\n')
    pythonFile.close()

    webbrowser.open(url)

# input('Done')
