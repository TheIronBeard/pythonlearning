# This is a Rock, Paper, Scissors game.
import random, sys

print('Rock, Paper, Scissors: The Virtual Game')

# These variables keep track of the score.
wins = 0
losses = 0
ties = 0

while True: #  main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    
    while True: #player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        
        if playerMove == 'q':
            sys.exit() #quit progam
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #break out of player input loop
        print('Type one of r, p, s, or q')

    # Display player choice
    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's':
        print('Scissors versus...')

    # Computer player input
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scrissors')

    # Display and record the win/loss/tie
    if playerMove == computerMove:
        print('It is a tie.')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print("You win!")
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose...')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose...')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose...')
        losses = losses + 1


    
