import math,function,timeit
start = timeit.default_timer()
count = 0
c = 0
p = 0
l = []
high = 0
acc = 0
for a in range(10,1001):
    for b in range(1,a):
        c = math.sqrt((b **2 ) + (a **2))
        p = a + b + c
        if int(p) == p and p < 1000:
            l.append(p)
num = function.howmanycommon(l)
for i in l:
    if l.count(i) == num:
        print("Answer is ",i)
        break
stop = timeit.default_timer()
print("Time Taken : ", stop - start)
