import timeit
start = timeit.default_timer()
n = 100
i = 0
answer = 0
total = 1
counter = 0
while i != 99:
    answer = (n -i)
    i += 1
    total *= answer
for j in str(total):
    counter += int(j)
stop = timeit.default_timer()
print(counter)
print(stop - start)
