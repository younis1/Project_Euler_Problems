import math
trinumber = 0
factors = 1
counter = 0
a = 0
while counter <502:
    counter = 0
    a += 1
    trinumber += a
    for factors in range (1,int(math.sqrt(trinumber)) + 2):
        if trinumber % factors == 0:
            counter += 2
print(trinumber)
