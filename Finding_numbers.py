import re
Ex = open('Actual_Data.txt')
y = list()
sum=0
for h in Ex:
    h= h.rstrip()
    stuff = re.findall('\S[0-9]+\S', h) or re.findall('[0-9]+\S', h) or re.findall('\S[0-9]+', h) or re.findall('[0-9]+', h) or re.findall('\S([0-9]+)\S', h)
    for l in stuff:
        if l.startswith("y") or l.startswith("e"):
            ll= re.findall('[0-9]+', l)
            sum = sum + int( ll[0] )
            y.append(ll)
        else:
            sum = sum + int(l)
            y.append(l)

print(y,"Total value: ", len(y))
print("Total sum: ", sum)