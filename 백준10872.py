import sys

def factorial(num):
    if num == 1:
        return num
    else: 
        return num * factorial(num-1)

a = int(sys.stdin.readline())
fac = factorial(a)

print(fac)
