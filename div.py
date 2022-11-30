import math
def zero(n):
    b=len(str(n))
    return (n/int(math.pow(10,b-1)))
n=int(input())
print("%.2f"%zero(n))
