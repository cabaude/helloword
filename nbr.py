def is_prime(n):
    var = 0
    for i in range(1, n+1):
        var1 = input('donnez un nombre : ')
        if int(var1) > var:
            var = int(var1)
    return var


print(is_prime(10))


