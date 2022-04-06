import timeit
start = timeit.default_timer()
num = 0
snum = ''
high = 0
for i in range(100,1000):
    for j in range(100,1000):
       num = i * j
       snum = str(num)
       if snum == snum[::-1]and num > high:
           high = int(snum)
stop = timeit.default_timer()
print("Answer is ", high)
print("Time taken : ",stop - start)
 
