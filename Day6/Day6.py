with open('Day6.txt') as f:
    correct_ans = 0
    data = []
    sentence=''
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
    #We create a list of lists for each group (each lines means someone has answered something)
    data = [x.splitlines() for x in data]

    #Part1
    for d in data:
        #We create a list for the answers
        correct_unique = []
        #We group all the answers in a single string
        var = [b for b in d]
        var = ''.join(var)
        #We count which letters appear and don't repeat it if they have already shown
        [correct_unique.append(x) for x in var if x not in correct_unique]
        #The number of unique answers of the group is the sum of the list 
        correct_ans += len(correct_unique)
    
    print(f'People have chosen {correct_ans} "yes" answers')
    #Part2
    correct_ans = 0
    correct_together = {}
    for d in data:
        #We create a list for the answers
        correct_unique = [b for b in d]
        #We group all the answers in a single string
        correct_unique = ''.join(correct_unique)
        #We count how many times each answer has appeared
        correct_together = {x : correct_unique.count(x) for x in set(correct_unique)}
        for c in correct_together:
            #If an answer has appear the len of d(which means the len(d) people have answered this) then is correct
            if correct_together[c] == len(d):
                correct_ans += 1
    
    print(f'People have chosen {correct_ans} "yes" answers')