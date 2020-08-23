#만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다.
# 3명 기준 0번이랑 1 2 비교 1번이랑 0 2 비교 2번이랑 0 3 비교
i=0
W = []
H = []
rank = [1]*100
n = int(input())

for i in range(n):
    W.append(int(input()))
    H.append(int(input()))

for i in range(n):
    
    for j in range(n):
        if W[i] < W[j] and H[i] < H[j]:
            rank[i] = rank[i]+1
        
        
        
for i in range(n):
    print(rank[i])
            