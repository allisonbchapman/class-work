numbers = [1, 2, 3, 4]
def chop(t):
    del t[0]
    del t[-1]
    t2 = list()
    t3 = t2.append(t)
    print(t3)
chop(numbers)