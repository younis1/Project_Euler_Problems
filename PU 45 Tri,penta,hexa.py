import timeit,function
start = timeit.default_timer
x = 0
a = 40755
while x == 0:
    a += 1
    if a in function.hexagonal(a):
        print(a, " is hexagonal")
        if a in function.pentagonal(a):
            if a in function.triangular(a):
                print("Answer is ",a)
                x += 1
stop = timeit.default_timer()
print("Time taken ", stop - start)
                
