import math

def is_prime(n):
    tab = []
    for i in range(1, n+1):
        racine=int(math.sqrt(i))
        var = True
        if i==0:
            var = False
        elif i==2:
            var = True
        elif i%2==0:
            var = False
        else:
            for j in range(3,racine+1):
                if i%j==0:
                    var = False

        if var:
            tab.append(i)

    return tab


print(is_prime(100))