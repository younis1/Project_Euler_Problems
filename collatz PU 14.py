import timeit
start= timeit.default_timer()
counter = 0
number = 0
high = 0
highunm = 0
for i in range(1,1000001):
    counter = 0
    number = i 
    while number > 1:
        if number % 2 == 0:
            number = number /2
            counter += 1
        else: 
            number = (3* number) + 1
            counter += 1
    if high < counter :
        high = counter
        highnum = i
stop = timeit.default_timer()
print("Answer is ", highnum)
print("Time taken : ",stop - start)
