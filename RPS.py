import random

plays = {1:'Rock',2:'Paper',3:'Scissor'}
lose = 0
win = 0
#userPlay = input('Enter Rock, Paper, Scisscor \n')
def game():
    global win
    global lose
    compPlay = random.randint(1,3)
    userPlay = 0
    compPlay = plays[compPlay]
    while userPlay != 'Rock' or userPlay != 'Paper' or userPlay != 'Scissor':
        userPlay = input('Enter Rock, Paper, Sciscor \n')
        if userPlay == 'Rock' or userPlay == 'Paper' or userPlay == 'Scissor':
            break
    print('You chose',userPlay, 'and computer chose',compPlay)

    if compPlay == userPlay:
        print('Tie!')
    elif compPlay == 'Rock' and userPlay == 'Paper': 
        print('Paper covers rock, you win!')
        win = win + 1
    elif compPlay == 'Paper' and userPlay == 'Rock': 
        print('Paper covers rock, you lose!')
        lose = lose + 1
    elif compPlay == 'Paper' and userPlay == 'Scissor': 
        print('Sciscor cuts paper, you win!')
        win = win + 1
    elif compPlay == 'Scissor' and userPlay == 'Paper': 
        print('Sciscor cuts paper, you lose!')
        lose = lose + 1
    elif compPlay == 'Scissor' and userPlay == 'Rock': 
        print('Rock smashes sciscor, you win!')
        win = win + 1
    elif compPlay == 'Rock' and userPlay == 'Scissor': 
        print('Rock smashes sciscor, you lose!')
        lose = lose + 1

def playGame():
    while True:        
        game()    
        play = input('Play again? Yes/See Score/End \n')
        if play == 'Yes':
            pass
        elif play == 'See Score':
            print('You won', win,'times and lost',lose,'times')
            pass)
        else:
            print('Thanks for playing')
            break
playGame()
print('Loop is done')
