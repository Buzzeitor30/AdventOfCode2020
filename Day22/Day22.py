input = [ x for x in open('Day22.txt').read().split('\n') if x != '']

player1 =  input.index('Player 1:')
player2 = input.index('Player 2:')

player1 = list(map(int,input[player1+1:player2]))
player2 = list(map(int,input[player2+1:]))

while player1 != [] and player2 != []:
    x = player1.pop(0)
    y = player2.pop(0)
    if x > y:
        player1.append(x)
        player1.append(y)
    else:
        player2.append(y)
        player2.append(x)

player2_score = sum([player2[x] * (len(player2) - x) for x in range(len(player2))])
player1_score = sum([player1[x] * (len(player1) - x) for x in range(len(player1))])
print(f'Player 1 score is {player1_score} and Player 2 score is {player2_score}')

player1 =  input.index('Player 1:')
player2 = input.index('Player 2:')

player1 = list(map(int,input[player1+1:player2]))
player2 = list(map(int,input[player2+1:]))


def recursive_carts(deckplayer1:list,deckplayer2:list,seendeck1:list,seendeck2):
    while deckplayer1 != [] and deckplayer2 != []:
        if deckplayer1 in seendeck1 or deckplayer2 in seendeck2:
            #Player 1 wins
            return "True"
        else:
            seendeck1.append(deckplayer1.copy())
            seendeck2.append(deckplayer2.copy())
            #Card player1
            x = deckplayer1.pop(0)
            #Card player2
            y =  deckplayer2.pop(0)
            winner = False
            if x <= len(deckplayer1) and y <= len(deckplayer2):
                #Which player wins?
                winner = recursive_carts(deckplayer1[:x],deckplayer2[:y],[],[])
            else:
                #Which player has won?
                winner = x > y
            if(winner):
                deckplayer1.append(x)
                deckplayer1.append(y)
            else:
                deckplayer2.append(y)
                deckplayer2.append(x)

    return deckplayer1 != []

recursive_carts(player1,player2,[],[])
player2 = sum([player2[x] * (len(player2) - x) for x in range(len(player2))])
player1 = sum([player1[x] * (len(player1) - x) for x in range(len(player1))])
print(f'Player1 score is {player1} and Player 2 score is {player2} in the Recursive Game')