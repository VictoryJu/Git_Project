def factorial(num):
    if num == 1:
        return num
    else: 
        return num * factorial(num-1)

a = int(input())
fac = factorial(a)

print("값은 ",fac)
