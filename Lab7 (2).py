items=[7, 3, 14, 1, 21, 0, 0, 56]

class Queue:
    def __init__(self):
        self.items=[]
    def empty(self):
        return self.items==[]
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def __str__(self):
        temp="["
        for i in range(len(self.items)):
            if i==len(self.items)-1:
                temp+=str(items [i])
            else:
                temp+=str(items [i])+","
        temp+="]"
        return temp
    

class Stack:
    def __init__(self):
        self.items=[]
    def empty(self):
        return self.items==[]
    def push(self, item):
        self.items.insert(0, item)
    def pop(self):
        return self.items.pop(0)
    def peak(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        temp="["
        for i in range(len(self.items)):
            if i==len(self.items)-1:
                temp+=str(self.items[i])
            else:
                temp+=str(self.items[i])+","
        temp+="]"
        return temp

Q=Queue()
S=Stack()

for i in items:
    Q.enqueue(i)
    S.push(i)
print(Q)
print(S)
