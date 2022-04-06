import math,time
START = time.time()
THRESHOLD = 1000000
FIRST_NUMBER = 10
MAX_N = 100
over_million_counter = 0
for i in range(FIRST_NUMBER, MAX_N + 1):
    j = 1
    if (math.comb(i, i//2) > THRESHOLD): # Check if the 'max' combination is over million
        while j <= i//2:
            if math.comb(i,j) > THRESHOLD:
                over_million_counter += 2*(i//2 - j + 1)
                if i%2 == 0:  # Because we would have counted mid value twice
                    over_million_counter -= 1
                j = i//2 + 1 # To terminate while
            j += 1
            
print("Answer is:", over_million_counter)
END = time.time()
print("Time taken:", END - START)
