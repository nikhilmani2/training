class Queue:
    def __init__(self):
        self.elements=[]
    def enqueue(self,element):
        self.elements.append(element)
    def dequeue(self):
        if not self.empty():
            return self.elements.pop(0)
        else:
            return "Queue is empty"
    def empty(self):
        return len(self.elements)==0
    def size(self):
        return len(self.elements)
    
q1=Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
print(q1.size())
print("-------------dequeing------------")
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print("Size: " + str(q1.size()))
print(q1.dequeue())


        
                