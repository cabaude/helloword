def isIndex(n):
    t = [3, 5, 0, 4, 4, 7]
    t2 = []
    for i in range(0, len(t)):
        if n == t[i]:
            t2.append(i)
    print(t2)


isIndex(5)


