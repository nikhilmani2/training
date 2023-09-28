class stack:
    def __init__(self):
        self.stack1=[]
    def push(self,x):
        self.stack1.append(x)
    def pop(self):
        if not self.empty():
            return self.stack1.pop()
        else:
            return "Stack is empty !!!" 
    def empty(self):
        return len(self.stack1)==0
    
    def length(self):
        return len(self.stack1)
    
samplestack=stack()
samplestack.push(1)
samplestack.push(2)
samplestack.push(3)
samplestack.push(4)
samplestack.push(5)
print(samplestack.empty())  
print(samplestack.length())
samplestack.pop()
samplestack.pop()
print(samplestack.empty())         
print(samplestack.length())

            