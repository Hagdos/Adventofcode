import sys
sys.setrecursionlimit(int(1e6))

# Return the next n bits; and move the pointer n forward.
def readBits(b, n):
    global p
    a = b[p:p+n]
    p += n
    return(a)


def readPacket(b):
    global p
    global ans1
    
    V = int(readBits(b, 3), 2)
    ans1 += V
    ID = int(readBits(b, 3), 2)
    
    if ID == 4:
        lastgroup = 1
        binvalue = []
        while lastgroup == 1:
            lastgroup = int(readBits(b, 1))
            binvalue += readBits(b, 4)
        value = int(''.join(binvalue), 2)
        return value
    
    else:
        # First grab the subpackets
        values = []
        ltype = int(readBits(b, 1))
        # Lengthtype = length of bits
        if ltype == 0:
            length = int(readBits(b, 15), 2)
            end = p + length
            while p < end:
                values.append(readPacket(b))
        else:
            length = int(readBits(b, 11), 2)
            for _ in range(length):
                values.append(readPacket(b))

        # Then do the necessary calculation
        if ID == 0:     # Sum
            return sum(values)
        elif ID == 1:   # Product 
            a = 1
            for v in values:
                a *= v
            return a
        elif ID == 2:   # Minimum
            return min(values)
        elif ID == 3:   # Maximum
            return max(values)
        elif ID == 4:   # Return actual value
            raise ValueError("This should never happen")
            return None
        elif ID == 5:   # Greater than
            return int(values[0] > values [1])
        elif ID == 6:   # less than
            return int(values[0] < values [1])
        elif ID == 7:
            return int(values[0] == values [1])
                
        return values   

file = open('input.txt').read()
data = file.strip()
ans1 = ans2 = 0

# Turn hex into binary; padded zeroes at the end
binlen = len(data)*4
b = bin(int(data, 16))[2:].zfill(binlen)

# Read the main package
p = 0
ans2 = readPacket(b)


print('The answer to part 1: ', ans1)
print('The answer to part 2: ', ans2)
