import re

f = open('Passports.txt')
x = f.read(-1)

Passports = re.split("\n\n", x)
Valid = 0

for p in Passports:

    if (re.search("byr", p) and
    re.search("iyr", p) and
    re.search("eyr", p) and
    re.search("hgt:([\d]+)(in|cm)", p) and
    re.search("hcl:#[0-9a-f]{6}(?: |$|\n)", p) and
    re.search("ecl:(?:amb|blu|brn|gry|grn|hzl|oth)(?: |$|\n)",p) and
    re.search("pid:[0-9]{9}(?: |$|\n)",p)):
        #print p
        
        byrs = re.search("byr", p).start()+4
        birthyear = int(p[byrs:byrs+4])
        iyrs = re.search("iyr", p).start()+4
        issueyear = int(p[iyrs:iyrs+4])
               
        if birthyear >= 1920 and birthyear <= 2002 and issueyear >=2010 and issueyear <= 2020:
            #print "Birthyear and Issueyear ok"
            
            eyrs = re.search("eyr", p).start()+4
            expyear = int(p[eyrs:eyrs+4]) 
            if expyear >= 2020 and expyear <= 2030:
                #print "Expiration year ok"
                

                height = re.findall("hgt:([\d]+)(in|cm)",p)
                #print height
                unit = height[0][1]
                length = int(height[0][0])
                
                if (unit == "cm" and length >= 150 and length <= 193) or (unit == "in" and length >=59 and length <= 76):
                    #print p
                    #print "Height is okay"
                    a = 1
                    Valid += 1
                    
                    
        #print "\n"

    
print Valid



