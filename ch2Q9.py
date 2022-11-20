# Problem 9: Write code that prints 'Hello' if 1 is stored in spam, prints 'Howdy' if 2 is stored in spam, and prints 'Greetings!' if anything else is stored in spam.
import sys

while True:
    print('Please choose a value between 1 and 3 or (q)uit to exit the program')
    spam = input()

    if spam == 'q':
        sys.exit()
        continue
    elif spam == '1':
        print('Hello')
        continue
    elif spam == '2':
        print('Howdy')
        continue
    elif spam != 'q' or '1' or '2':
        print('Greetings!')
