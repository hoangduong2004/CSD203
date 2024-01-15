print('''
Name: Hoàng Thái Dương
ID: HE181802
Class: AI1811
''')


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_LinkedList:
    def __init__(self):
        self.head = None

    #1. def addToHead(x) - add a node with value x at the head of a list.

    def addToHead(self, x):
        new = Node(x)
        new.next = self.head
        if self.head is not None:
            self.head.prev = new
        self.head = new

    #2. def addToTail(x) - add a node with value x  at the tail of  a list.

    def addToTail(self, x):
        new = Node(x)
        if self.head is None:
            self.head = new
        else:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = new
            new.prev = tail

    
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
            new.prev = cur
            if cur.next is not None:
                cur.next.prev = new
            cur.next = new

    
    #4. def traverse() - traverse from head to tail and dislay info of all nodes in the list.

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end = ' ')
            cur = cur.next
        print()
    
    #5. def deleteFromHead() - delete the head and return its info.

    def deleteFromHead(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return temp
        
    
    #6. def deleteFromTail() - delete the tail and return its info. 

    def deleteFromTail(self):
        if self.head is None:
            return None
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            temp = cur.data
            cur.prev.next = None
            return temp
        

    #7. def deleteAter(p) - delete the node after the node  p  and return its info.

    def deleteAfter(self, p):
        cur = self.head
        while cur is not None:
            if cur.data == p:
                break
            cur = cur.next
        if cur is None or cur.next is None:
            print("The node is not in the list")
        else:
            temp = cur.next.data
            cur.next = cur.next.next
            if cur.next is not None:
                cur.next.prev = cur
            return temp
        

    #8. def del(x) - delele the first node whose info is equal to x.

    def del_Node_equal(self, x):
        cur = self.head
        while cur is not None:
            if cur.data == x:
                break
            cur = cur.next
        if cur is None:
            print("The node is not in the list")
        else:
            if cur.prev is not None:
                cur.prev.next = cur.next
            if cur.next is not None:
                cur.next.prev = cur.prev
            if cur == self.head:
                self.head = cur.next

    
    #9. def search(x) - search and return the reference to the first node having info x.  

    def search(self, x):
        cur = self.head
        while cur is not None:
            if cur.data == x:
                return cur
            cur = cur.next
        return None
    

    #10. def count() - count and return number of nodes in the list. 

    def count(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count
    

    #11. def del(i) - delete an i-th node on the list. Besure that such a node exists.

    def delete_node(self, i):
        count = 0
        cur = self.head
        while cur is not None:
            if count == i:
                break
            count += 1
            cur = cur.next
        if cur is None:
            print("The node is not in the list")
        else:
            if cur.prev is not None:
                cur.prev.next = cur.next
            if cur.next is not None:
                cur.next.prev = cur.prev
            if cur == self.head:
                self.head = cur.next


    #12. def sort() - sort the list by ascending order of info. 
    
    def sort(self):
        if self.head is None:
            return
        cur = self.head
        while cur.next is not None:
            next = cur.next
            while next is not None:
                if cur.data > next.data:
                    temp = cur.data
                    cur.data = next.data
                    next.data = temp
                next = next.next
            cur = cur.next

    #13. def del(p) - delete node p if it exists in the list.

    def del_p(self, p):
        if p is None or self.head is None:
            return
        if p == self.head:
            self.head = p.next
        if p.next is not None:
            p.next.prev = p.prev
        if p.prev is not None:
            p.prev.next = p.next


    #14. def toArray() - create and return array containing info of all nodes in the list.

    def toArray(self):
        arr = []
        cur = self.head
        while cur is not None:
            arr.append(cur.data)
            cur = cur.next
        return arr
    
# Test case:
# Linked list
lk = Doubly_LinkedList()

# Test addToHead
lk.addToHead(7)
lk.addToHead(9)
lk.addToHead(8)
print("List sau khi thêm vào đầu: ", end = ' ')
lk.traverse()  # Output: 8 9 7

# Test addToTail
lk.addToTail(2)
lk.addToTail(3)
print("List sau khi thêm vào cuối: ", end = ' ')
lk.traverse()  # Output: 8 9 7 2 3

# Test addAfter
lk.addAfter(9, 10)
print("Chuỗi sau khi thêm 10 vào sau 9 : ", end = ' ')
lk.traverse()  # Output: 8 9 10 7 2 3

# Test deleteFromHead
cur = lk.deleteFromHead()
print("Node bị xóa: ", cur, " List sau khi xóa node đầu: ", end = ' ')
lk.traverse()  # Output: 9 10 7 2 3 

# Test deleteFromTail
cur1 = lk.deleteFromTail() 
print("Node bị xóa: ", cur1, " List sau khi bị xóa node cuối: ", end = ' ')
lk.traverse() # Output: 9 10 7 2

# Test deleteAfter
cur2 = lk.deleteAfter(10)
print("Node bị xóa: ", cur2, " List sau khi bị xóa node sau node 10: ", end = ' ') 
lk.traverse() # Output: 9 10 2

# Test del_Node_equal()
cur3 = lk.del_Node_equal(3)
print("Node bị xóa: ", cur3, " List sau khi bị xóa node có data = 3: ", end = ' ') 
lk.traverse() # Output: 9 10 2

# Test search()
x = 10
print('The node có info:', x)
print(lk.search(x))

# Test count()
print("Số phần tử của list: ",lk.count())


# Test delete_node()
i = 2
lk.delete_node(i)
print("List sau khi xóa node thứ", i,": ", end = ' ')
lk.traverse()

# Test sort()
lk.addToHead(6)
lk.addToHead(5)
lk.addToHead(2)
lk.sort()
print("List mới sau khi sắp xếp: ", end = ' ')
lk.traverse() 

# Test toArray()
print("Chuyển list này thành array: ",lk.toArray())