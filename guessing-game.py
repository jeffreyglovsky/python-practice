import random 

a = random.randint(1,9)
while True:  
    try:  
        b = input('Guess a number 1-9! \n')
        b= int(b)
        break
    except:
        print('It needs to be a number \n')
        b = input
        
guess = 1
while b != a:
    if b>9:
        b = int(input("You're higher than 9! \n"))
    elif b<1:
        b= int(input("You're lower than 1! \n"))
    elif b>a:
        b = int(input('Too High, guess lower \n'))
    else:
        b = int(input('Too Low, guess higher \n'))
    guess = guess + 1

print('It took',guess,'guesses!')
    
