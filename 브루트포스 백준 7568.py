
x = []
y = []
rank = []

n=int(input())

for i in range(0,n):    
    x,y = map(int,input().split())
    

for j in range(n):
    num1 = n
    for z in range(n):
        if x[j] > x[z] and y[j] > y[z]:
            rank[j] = num1+0
        elif x[j] > x[z] and y[j] < y[z]:
            rank[j] = num1-1
        elif x[j] < x[z] and y[j] > y[z]:
            rank[j] = num1-1

i=0
for i in range(n):
    print(rank[i])
