import math

def allPossibilities(coins):
    List1 = ["H","T"]
    for x in range(coins-1):
        List2 = []
        for x in List1:
                   List2.append(x+"H")
                   List2.append(x+"T")
        List1 = List2.copy()
    return List2

def probabilityXcoinsYheads(x,y,headChance=0.5):
    a = int(math.factorial(x)/math.factorial(y)/math.factorial(x-y))
    b = 2**x 
    c = a / b
    d = a*headChance**(y)*(1-headChance)**(x-y)
    return a,b,c,d

def probability(sequence,coinPickChance,headChance):
    p = []
    for x in range(len(coinPickChance)):
        p.append(coinPickChance[x])
        for y in sequence:
            if y == "H": p[x]*=headChance[x]
            else: p[x]*=(1-headChance[x])        
    return sum(p)
    


