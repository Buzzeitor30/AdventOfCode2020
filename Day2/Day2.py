import re
min_n = 0
max_n = 0
char = 0
correct = 0
with open('Day2.txt') as f:
    data = f.read().splitlines()
    
    for word in data:
        temp = re.findall(r'\d+', word)
        res = list(map(int, temp))
        min_n = res[0]
        max_n = res[1]

        temp = word.find(':')
        char = word[temp-1]
        
        sentence = word[temp+2:]
        occur = sentence.count(char)

        if min_n <= occur <= max_n:
            correct += 1
    
    print("There are " + str(correct) + " words")
    correct = 0
    for word in data:
        temp = re.findall(r'\d+', word)
        res = list(map(int, temp))
        min_n = res[0]
        max_n = res[1]

        temp = word.find(':')
        char = word[temp-1]
        sentence = word[temp+2:]
        if (sentence[min_n - 1] == char and sentence[max_n - 1] != char) or (sentence[min_n - 1] != char and sentence[max_n - 1] == char):
            correct += 1
    print(correct)

    