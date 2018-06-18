

def isIn(n):
    t = [3, 5, 0, 4]
    var = False
    for i in range(0, len(t)):
        if n == t[i]:
            var = True
    if var == True:
        print('présent')
    else:
        print('pas présent')

isIn(2)


