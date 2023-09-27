class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
            
    def insertAtBegin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return    
        else:
            new_node.next=self.head
            self.head=new_node
            
    def insertAtIndex(self,data,index):
        new_node=Node(data)
        current_node=self.head 
        position=0
        if position==index:
            self.insertAtBegin(data)
        else:
            while(current_node !=None and position +1 !=index):
                position +=1
                current_node=current_node.next
                if current_node != None:
                    new_node.next=current_node.next 
                    current_node.next = new_node
                else:
                    print("Index is not present")
                    
    def insertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node=current_node.next  
        current_node.next = new_node
        
    def updateNode(self,val,index):
        current_node=self.head
        position=0
        if position == index:
            current_node.data=val
        else:
            while(current_node != None and position != index):
                position+=1
                current_node=current_node.next
            if current_node !=None:
                current_node.data=val
            else:
                print("Index is not present")   
                
    def removeLastNode(self):
        if self.head is None:
            return
        current_node=self.head
        while(current_node.next.next):
            current_node=current_node.next
        current_node.next=None 
        
    def removeFirstNode(self):
        if(self.head == None):
            return
        self.head=self.head.next
        
    def removeAtIndex(self,index):
        if self.head == None:
            return
        current_node=self.head
        position=0
        if(position == index):
            self.removeFirstNode()
        else:
            while(current_node != None and position+1 != index) :
                position+=1
                current_node = current_node.next
            if current_node != None :
                current_node.next=current_node.next.next 
            else:
                print("Index is not present")   
                
    def removeNode(self,data):
        current_node=self.head
        if current_node.data ==data:
            self.head=current_node.next
            return
        try:
            while(current_node!=None and current_node.next.data !=data):
                current_node = current_node.next
            if current_node==None:
                return
            current_node.next=current_node.next.next
        except:
            print("Data is not present")    
                        
                
    def sizeOfLL(self):
        size=0
        if (self.head):
            current_node=self.head
            while(current_node):
                size+=1
                current_node=current_node.next
            return size
        else:
            return 0    
                                
    def printLL(self):
        current_node=self.head
        while(current_node):
            print(current_node.data)
            current_node=current_node.next 

ll=LinkedList()
ll.insertAtEnd('a')
ll.insertAtBegin('b')
ll.insertAtBegin('c')
ll.insertAtEnd('o')
ll.insertAtIndex('z',2)
ll.updateNode('p',4)
print(ll.sizeOfLL())
ll.removeLastNode()
ll.removeFirstNode()
ll.removeAtIndex(1)
print(ll.sizeOfLL())
ll.removeNode('b')
ll.removeNode('z')
ll.printLL()                                        
                           