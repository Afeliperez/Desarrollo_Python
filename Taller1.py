import re
Ex = open('Ejemplo1.txt')
y = list()
m=0
for h in Ex:
    h= h.rstrip()
    stuff = re.findall('\S[0-9]+\S', h) or re.findall('[0-9]+\S', h) or re.findall('\S[0-9]+', h) or re.findall('[0-9]+', h) or re.findall('\S([0-9]+)\S', h)
    print(":", h)
    print("stuff:",stuff)
    for l in stuff:
        if l.startswith("y") or l.startswith("e"):
            ll= re.findall('[0-9]+', l)
            print(ll)
            m = m + int( ll[0] )
            print(m)
            y.append(ll)
        else:
            m = m + int(l)
            print(m)
            y.append(l)

print(y)
print(len(y))
print(m)

