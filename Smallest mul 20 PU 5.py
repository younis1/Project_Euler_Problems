import timeit
start = timeit.default_timer()
a = 20
b = 0
while b <=20:
    for i in range (1,21):
        if a % i == 0:
            b += 1 
        else :
            a = a + 20
            b = 0
print ("Answer is : ", a)
stop = timeit.default_timer()
print("Time taken : ", stop - start)
