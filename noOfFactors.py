import math
n = int(input())
v = math.sqrt(n)
i = 1
while(i<=v):
    if(n%i == 0):
        print(i)
        if(n//i != i):
            print(n//i)
    i += 1