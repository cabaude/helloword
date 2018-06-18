def isPalin(t):
    t2 = ""

    for i in range(1, len(t)+1):
        t2 += t[len(t)-i]
    if t == t2:
        print(t + ' est un palindrome')
    else:
        print(t + ' n\'est pas un palindrome')

isPalin("kayak")
isPalin("radar")
isPalin("enzo")
isPalin("anna")


