spam = 42 == 42
print(spam)

print('What is your name?')
name = input()
if name == 'Matthew':
    print('Hello, ' + str(name))
else:
    print('Access denied')
    exit()

print('Please enter your password.')
password = input()
#if name == str(name):


if password == 'swordfish' and name == 'Matthew':
    print('Access granted')
else:
    print('Wrong password.')