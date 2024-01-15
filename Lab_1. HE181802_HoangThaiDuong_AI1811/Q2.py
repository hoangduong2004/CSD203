print('''
Name: Hoàng Thái Dương
ID: HE181802
Class: AI1811
''')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly_LinkedList:
    def __init__(self):
        self.head = None


    #1. def addToHead(x) - add a node with value x at the head of a list.
        
    def addToHead(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    
    #2. def addToTail(x) - add a node with value x  at the tail of  a list.
        
    def addToTail(self, x):
        new = Node(x)  
        if self.head is None:  
            self.head = new 
        else:  
            cur = self.head  
            while cur.next:  
                cur = cur.next
            cur.next = new


    #3. def addAfter(p, x) - add a node with value x  after the node p.
            
    def addAfter(self, p, x):
        new = Node(x)
        cur = self.head
        while cur is not None:
            if cur.data == p:
                break
            cur = cur.next
        if cur is None:
            print("The node is not in the list")
        else:
            new.next = cur.next
            cur.next = new


    #4. def traverse() - traverse from head to tail and dislay info of all nodes in the list.
            
    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()


    #5. def deleteFromHead() - delete the head and return its info.
        
    def deleteFromHead(self):
        if self.head is None:
            print("The list is empty")
        else:
            cur = self.head
            self.head = self.head.next
            return cur.data


    #6. def deleteFromTail() - delete the tail and return its info.    
    
    def deleteFromTail(self):
        if self.head is None:
            print("The list is empty")
        else:
            cur = self.head
            if cur.next is None:
                self.head = None
                return cur.data
            else:
                while cur.next.next is not None:
                    cur = cur.next
                cur1 = cur.next
                cur.next = None
                return cur1.data


    #7. def deleteAter(p) - delete the node after the node  p  and return its info.
    
    def deleteAfter(self, p):
        cur = self.head
        while cur is not None:
            if cur.data == p:
                break
            cur = cur.next
        if cur is None:
            print("The node is not present in the list")
        elif cur.next is None:
            print("It is the last node")
        else:
            cur1 = cur.next 
            cur.next = cur.next.next
            return cur1.data



    
# Test case:
# Linked list
lk = Singly_LinkedList()

# Test addToHead
lk.addToHead(1)
lk.addToHead(9)
lk.addToHead(10)
print("List sau khi thêm vào đầu: ", end = ' ')
lk.traverse()  # Output: 10 9 1

# Test addToTail
lk.addToTail(2)
lk.addToTail(3)
print("List sau khi thêm vào cuối: ", end = ' ')
lk.traverse()  # Output: 10 9 1 2 3

# Test addAfter
lk.addAfter(2, 4)
print("Chuỗi sau khi thêm 4 vào sau 2: ", end = ' ')
lk.traverse()  # Output: 10 9 1 2 4 3

# Test deleteFromHead
cur = lk.deleteFromHead()
print("Node bị xóa: ", cur, " List sau khi xóa node đầu: ", end = ' ')
lk.traverse()  # Output: 9 1 2 4 3 

# Test deleteFromTail
cur1 = lk.deleteFromTail() 
print("Node bị xóa: ", cur1, " List sau khi bị xóa node cuối: ", end = ' ')
lk.traverse() # Output: 9 1 2 4

# Test deleteAfter
cur2 = lk.deleteAfter(1)
print("Node bị xóa: ", cur2, " List sau khi bị xóa node: ", end = ' ') 
lk.traverse() # Output: 9 2 4

