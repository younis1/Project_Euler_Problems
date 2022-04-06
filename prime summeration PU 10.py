import math 
number = 5
count = 0
answer = 5
while number < 2000000:
    for i in range(2,(int((math.sqrt(number)) + 2))):
        count = 0
        if number % i == 0:
            count += 1
            break
    if count == 1:
        number += 2
        
    if count == 0:
        answer += number
        number += 2
print(answer)
