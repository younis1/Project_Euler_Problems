import timeit
start = timeit.default_timer()
finaltotal = 0
startb = 0
for i in range(10,1000000000):
    total = 0
    for j in str(i):
        a = 0
        
        a = int(j)
        total += (a **5)
    if total == i:
        startb = 0
        startb = timeit.default_timer()
        finaltotal +=  total
        print("WOW NUMBER" , i)
    if startb > 1.0:
        break
stop = timeit.default_timer()
print(finaltotal)
print(stop - start)
