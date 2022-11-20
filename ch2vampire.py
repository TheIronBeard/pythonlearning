print('User name:')
name = input()

print('Age:')
age = input()

if name == name and int(age) > 12 and int(age) < 100:
    print('Hi, ' + str(name))

elif int(age) < 12:
    print('You are not ' + str(name))

elif int(age) > 300:
    print('Unlike you, ' + str(name) + ' is not an undead, immortal vampire')

elif int(age) > 100:
    print('You are not ' + str(name) + ', grannie.')
