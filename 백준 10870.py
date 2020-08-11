def Fibo(num):
    if num>=2:
        result = (num-1)+(num-2)
        return result + Fibo(num-1)
    elif num == 1:
        return 1
    else:
        return 0

sum = int(input())

print(Fibo(sum))