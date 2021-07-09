import re
import time

data = open('input.txt').read().strip()
deData = ''
length = 0

marker = re.compile(r'^\(([0-9]*)x([0-9]*)\)')

start = time.time()

match = marker.search(data)
while(match):
    nchars = int(match.groups()[0])
    repetition = int(match.groups()[1])
    
    # Take the relevant characters from the data
    characters = data[match.end():match.end()+nchars]
    # Remove the marker and the characters from the data
    data = data[match.end()+nchars:]
    
    #Add the data to the decompressed data
    deData += characters * repetition
    length += len(characters) * repetition
    
    #Do the next search
    match = marker.search(data)
    
print('The answer to part 1:', len(deData))


# =============================================================================
# Part 2
# =============================================================================
data = open('input.txt').read().strip()
def findLength(string):  
    match = marker.search(string)
    if match:
        length = 0
        while(match):
            nchars = int(match.groups()[0])
            repetition = int(match.groups()[1])
            # Take the relevant characters from the data
            characters = string[match.end():match.end()+nchars]
            # Remove the marker and the characters from the data
            string = string[match.end()+nchars:]
            
            #Add the length of string belonging to this marker
            length += findLength(characters)*repetition
            #Find the next match
            match = marker.search(string)
        return length
    
    else:
        return(len(string))


print('The answer to part 2:', findLength(data))