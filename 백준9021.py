import sys

class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self,Str):
        self.stack.append(Str)
    
    def pop(self):
        St = self.stack.pop()
        return St


N = int(input())
s = Stack()

for i in range(N):
    s.push(list(map(str,sys.stdin.readline().rstrip().split(' '))))

for j in range(N):
    result = s.pop()
    if result == '(':
        count = count + 1
    elif result == ')':
        count2 = count2 + 1

sub = count - count2

if sub == 0:
    print("Yes")
else:
    print("NO")
