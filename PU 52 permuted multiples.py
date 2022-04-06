import timeit
start = timeit.default_timer() 
l = []
a = 125873
realcounter = 0
acc = 2
al = []
b = 0
while realcounter != 5 :
    if len(str(int(a))) == len(str(int(a) * 6 )):
        l.clear()
        a += 1
        for i in str(a):
            l.append(i)
        acc = 2
        b = 0
        realcounter = 0
        while acc < 7:
            count = 0
            for q in str(a * acc ):
                if q not in l:
                    b = 1
                    break
                else:
                    count += 1
            if b == 1:
                break
            if len(l) == count:
                acc += 1
                realcounter += 1                
    else:
        a += 1
print("Answer is ",a)
stop = timeit.default_timer()
print("Time taken ", stop - start)
