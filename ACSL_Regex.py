# Aayush Dhiman
# Loudoun Tupooze
# Friday, April 15, 2016
# 5:00 PM
import re


def match_or_not(c, d):
    z = []
    for i in c:
        x = re.fullmatch(d, i)    # x is a Match Object
        if x:
            z.append(i)     # if its a match, add the match to a list
        else:
            z.append('NONE')    # otherwise, add 'NONE'
            print('z = ' + str(z))
        if len(z) > 1:      # if the length of z is greater that 1
            if 'NONE' in z:     # and there is 'NONE' in the list
                z.remove('NONE')    # remove the 'NONE'
    sol = ', '.join(z)      # converting z to string form
    return 'OUTPUT = ' + str(sol)     # returning z

a = input('Enter your list of inputs: ')
a = [i for i in a.split(', ')]

for i in range(5):
    b = input('Enter a regex: ')
    if b == '':
        b = '#'
    print(match_or_not(a, b))
