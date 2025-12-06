#! /usr/bin/env python

from urllib.request import Request, urlopen
import os
import webbrowser

# year = input('Year: ')
# day = input('Day: ')

year = 2025
day = 6

path = str(year) + '/Day ' + str(day)
url = 'https://adventofcode.com/' + str(year) + '/day/' + str(day)
inputurl = url + '/input'

if os.path.isdir(path):
    print('Folder already exists')
else:
    # Read input data from HTTP
    inputrequest = Request(inputurl)
    inputrequest.add_header('Cookie', 'session=')
    inputrequest.add_header('User-Agent', 'github.com/Hagdos/Adventofcode by tomkooyman@gmail.com')
    puzzleInput = urlopen(inputrequest).read()

    # Write input data to input.txt
    os.makedirs(path)
    inputFile = open(path + '/input.txt', 'wb')
    inputFile.write(puzzleInput)
    inputFile.close()

    #Create python file
    pythonFile = open(path + '/Day ' + str(day) + '.py', 'w')
    pythonFile.write('file = open(\'input.txt\').readlines()\n\n')
    pythonFile.write('data = [x.strip().split() for x in file]\n')
    pythonFile.write('print(data)\n')
    pythonFile.write('ans1 = ans2 = 0\n\n')
    pythonFile.write('print(\'The answer to part 1: \', ans1)\n')
    pythonFile.write('print(\'The answer to part 2: \', ans2)\n')
    pythonFile.close()

    webbrowser.open(url)

# input('Done')
