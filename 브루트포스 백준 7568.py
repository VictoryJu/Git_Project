
x = []
y = []
num = []
i=0
j=0
n=int(input())

for i in range(n):
    x[i] = int(input())
    y[i] = int(input())
    
for j in range(n):
    num1 = n
    for z in range(n):
        if x[j] > x[z] and y[j] > y[z]:
            num[j] = num1+0
        elif x[j] > x[z] and y[j] < y[z]:
            num[j] = num1-1
        elif x[j] < x[z] and y[j] > y[z]:
            num[j] = num1-1

i=0
for i in range(n):
    print(num[i])
