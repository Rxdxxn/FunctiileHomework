import math
 
def friends(a,b):
    sum1 = 1
    sum2 = 1
    i = 2
    while(i * i <= a):
        if (a % i == 0):
            sum1 = (sum1 + i +math.floor(a / i))
        i += 1
    j = 2
    while(j * j <= b):
        if (b % j == 0):
            sum2 = (sum2 + i +math.floor(b / j))
        j += 1
        if sum1==sum2:
            return print("n) PRIETENI")
        else:
            return print("n) NU SUNT PRIETENI") 

r= int(input('a: '))
t= int(input('b: '))
friends(r,t)