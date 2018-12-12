def chop(t):
    del t[-1]
    del t[0]

def middle(t):
    return t[1:len(t) - 1]
