#! /usr/bin/env python

from urllib.request import Request, urlopen
import os

year = input('Year: ')
day = input('Day: ')

path = str(year) + '/Day ' + str(day)
url = 'https://adventofcode.com/' + str(year) + '/day/' + str(day) + '/input'

if os.path.isdir(path):
    print('Folder already exists')
else:
    # Read input data from HTTP
    inputrequest = Request(url)
    inputrequest.add_header('Cookie', 'session=53616c7465645f5f88f0086678489a3b1cc3eb6b191b9140bc4956a0bbb5a8181524dcff350e62f74979bfa8f0a145f9')
    puzzleInput = urlopen(inputrequest).read()
    
    # Write input data to input.txt
    os.mkdir(path)
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
        
# input('Done')
