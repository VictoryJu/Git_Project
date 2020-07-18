"""
push X: 정수 X를 스택에 넣는 연산이다.

pop: 스택에서 가장 위에 있는 정수를 빼고, 
그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

size: 스택에 들어있는 정수의 개수를 출력한다.

empty: 스택이 비어있으면 1, 아니면 0을 출력한다.

top: 스택의 가장 위에 있는 정수를 출력한다. 
만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

"""

class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self,X):
        self.stack.append(X)

    def pop(self):
        if len(self.stack) != 0 :
            num = self.stack.pop()    
            print(num)
        else:
            print(-1)     

    def size(self):
        print(len(self.stack))
    
    def top(self):
        if len(self.stack) != 0:
            num = self.stack.pop()
            print(num)
            self.stack.append(num)
        else:
            print(-1)
    
    def empty(self):
        if len(self.stack) != 0:
            print(0)
        else:
            print(1)

    def show(self):
        print(self.stack)

s = Stack()
i=0
num = int(input())

for i in range(num):
    choice = input()

    if choice == 'top':
        s.top()
    elif choice == 'empty':
        s.empty()
    elif choice == 'size':
        s.size()
    elif choice == 'pop':
        s.pop()
    elif choice == 'push':
        X = input()
        s.push(X)
