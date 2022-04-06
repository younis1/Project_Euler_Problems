b = 2
a= 4
c = 2
while b < 10001:
    for c in range (2,a):
        if a % c == 0:
            a += 1
        else:
            a += 1
            b += 1
            c = 2
print (a)
