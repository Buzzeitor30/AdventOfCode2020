import re
#Solution
correct = 0
sentence = ''
#Where the file will be stored
data = []
#Missing cid is fine. NOTE: THIS IS THE SOLUTION FOR SECOND PART
fields = [r"byr:\b(19[2-9][0-9]|200[0-2])\b",
r'iyr:\b(201[0-9]|2020)\b',
r'eyr:\b(202[0-9]|2030)\b',
r'hgt:\b((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)\b',
r'hcl:#\b[a-f0-9]{6}\b',
r'ecl:\b(amb|blu|brn|gry|grn|hzl|oth)\b',
r'pid:\b[0-9]{9}\b']
pattern = 0
with open('day4.txt') as f:
    #We read every line in the file
    words = f.readlines()
    for w in words:
        #If the line is blank we have found a passport
        if w.isspace():
            data.append(sentence)
            sentence = ''
        else:
            sentence +=w
    #Due to the fact that the file doesn't end with an empty line we have to add the last one        
    data.append(sentence)
    #Remove \n from passports to make it more clear
    data = [x.replace('\n',' ') for x in data]

    #We loop through each passport
    for i in data:
        #We loop through patterns
        for f in fields:
            #Check if the pattern is present in the passport
            if re.search(f,i):
                pattern += 1
        #If all properties are present, then we will have matched the full list
        if pattern == len(fields):
            correct += 1
        pattern = 0
    print(correct)