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
            
def startoflinkedlistdel():
    llin.removeFirstNode()
    print("Element deleted")
    llin.printLL()
    print("-------------------------------------")
    menufunction()
def indexoflinkedlistdel():
    index=int(input("Enter your index"))
    llin.removeAtIndex(index) 
    print("Element deleted")
    llin.printLL()
    print("-------------------------------------")
    menufunction()    
def endoflinkedlistdel():
    llin.removeLastNode()
    print("Element deleted")
    llin.printLL()
    print("-------------------------------------")
    menufunction()        

def deletefunction():
    print("1: Delete at the start of linked list")
    print("2: Delete at the given index of linked list")
    print("3: Delete at the end of linked list")
    inputfordelete=int(input("Enter your choice: "))
    if inputfordelete ==1:
        startoflinkedlistdel()
    elif inputfordelete ==2:
        indexoflinkedlistdel()
    elif inputfordelete==3:
        endoflinkedlistdel()
    else:
        print("Wrong Choie !!!")
        menufunction()      
    

def updatefunction():
    element=input("Enter your element: ")
    index=int(input("Enter your index at which you want to update: "))
    llin.updateNode(element,index)
    print("Element updated")
    llin.printLL()
    print("-------------------------------------")
    menufunction()     
            
def startoflinkedlist():
    element=input("Enter your element: ")
    llin.insertAtBegin(element)
    print("Element inserted")
    llin.printLL()
    print("-------------------------------------")
    menufunction()
def indexoflinkedlist():
    element=input("Enter your element: ")
    index=int(input("Enter your index: "))
    llin.insertAtIndex(element,index)
    print("Element inserted")
    llin.printLL()
    print("-------------------------------------") 
    menufunction()
def endoflinkedlist():
    element=input("Enter your element: ")
    llin.insertAtEnd(element) 
    print("Element inserted")
    llin.printLL()
    print("-------------------------------------")
    menufunction()      
                
            
def insertfunction():
    
    print("1: Insert at the start of linked list")
    print("2: Insert at the given index of linked list")
    print("3: Insert at the end of linked list")
    inputforinsert=int(input("Enter your choice: "))
    if inputforinsert ==1:
        startoflinkedlist()
    elif inputforinsert ==2:
        indexoflinkedlist()
    elif inputforinsert==3:
        endoflinkedlist()
    else:
        print("Wrong Choie !!!")
        menufunction()            
    
                
def menufunction():            
    print("------------------------------------Linked List------------------------------------")
    print("1: Insert into Linked List")
    print("2: Update elements in Linked List")
    print("3: Delete element from Linked List")
    print("4: Exit")
    userinput=int(input("Enter your choice: "))
    if userinput == 1:
        insertfunction()
    elif userinput ==2:
        updatefunction()
    elif userinput==3:
        deletefunction()
    elif userinput== 4:
        exit()   
    else:
        print("Wrong Input !!!") 
                    
llin=LinkedList()  
menufunction()                   