
# first style output ***
def firstStyle(num):
    for i in range(1, num+1):
        x = ''
        y = '*'
        for j in range(i):
            x = x + y
        print(x)


# second style output ***
def secondStyle(num):
    T = []
    for i in range(1, num+1):
        x = ''
        y = '* '
        for j in range(i):
            x = x + y
        T.append(x)
    for i in range(0, len(T)):
        space = ''
        for j in range(len(T)-i):
            space = space + ' '
        print(space, T[i])

# Pascak funtion


def pascal(num):
    p = [1]
    sss = num

    for i in range(num):
        pl = p + [1]
        for j in range(len(p)-1):
            pl[j+1] = p[j] + p[j+1]

        space = ''
        for a in range(sss, -1, -1):
            space += ' '

        pp = ''
        for r in range(0, len(p)):
            pp += str(p[r]) + ' '
        print(space, pp)
        sss -= 1
        p = pl


number = int(input('number:  '))
print('_____________________/Style 1\_____________________\n')
firstStyle(number)
print('_____________________/Style 2\_____________________\n')
secondStyle(number)
print('_____________________/Pascale\_____________________\n')
pascal(number)
