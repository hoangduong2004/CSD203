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


    #8. def del(x) - delele the first node whose info is equal to x.     
    
    def delete(self, x):
        if self.head is None:
            print("The list is empty")
        elif self.head.data == x:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None and cur.next.data != x:
                cur = cur.next
            if cur.next is None:
                print("The node is not in the list")
            else:
                cur.next = cur.next.next


    #9. def search(x) - search and return the reference to the first node having info x.   
    
    def search(self, x):
            cur = self.head
            while cur is not None:
                if cur.data == x:
                    return cur
                cur = cur.next
            return 'There is no node having info ',x
    

    #10. def count() - count and return number of nodes in the list.    
    
    def count(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count


    #11. def del(i) - delete an i-th node on the list. Besure that such a node exists.
    
    def deleteIth(self, i):
        if self.head is None:
            print("The list is empty")
        elif i == 0:
            self.head = self.head.next
        else:
            cur = self.head
            count = 0
            while cur is not None and count < i:
                prev = cur
                cur = cur.next
                count += 1
            if cur is None:
                print("The node is not in the list")
            else:
                prev.next = cur.next


    #12. def sort() - sort the list by ascending order of info.     

    def sort(self):
        if self.head is None:
            return 'The list is empty'
        cur = self.head
        while cur is not None:
            min_node = cur
            tiep = cur.next
            while tiep is not None:
                if min_node.data > tiep.data:
                    min_node = tiep
                tiep = tiep.next
            cur.data, min_node.data = min_node.data, cur.data
            cur = cur.next


    #13. def del(p) - delete node p if it exists in the list.
            
    # def deleteNode(self, p):
    #     if self.head is None:
    #         print("The list is empty")
    #     else:
    #         cur = self.head
            


    #14. def toArray() - create and return array containing info of all nodes in the list.

    def toArray(self):
        arr = []
        cur = self.head
        while cur is not None:
            arr.append(cur.data)
            cur = cur.next
        return arr
    
    
    #15. Merge two ordered singly linked lists of integers into one ordered list.

    # def merge(self, llist):
        
    
    #16. def addBefore(p, x) - add a node with value x  before the node p. 

    def addBefore(self, p, x):
        new= Node(x)
        if self.head is None:
            print("The list is empty")
        elif self.head == p:
            new.next = self.head
            self.head = new
        else:
            cur = self.head
            while cur.next is not None and cur.next != p:
                cur = cur.next
            if cur.next is None:
                print("The node is not present in the list")
            else:
                new.next = cur.next
                cur.next = new


    #17. Attach a singly linked list to the end of another singly linked list.
    
    def attach(self, list1, list2):
        if list1.head is None:
            return list2
        else:
            cur = list1.head
            while cur.next is not None:
                cur = cur.next 
            cur.next = list2.head
            return list1


    #18. def max() - find and return the maximum value in the list.
            
    def max(self):
        if self.head is None:
            return "The list is empty"
        max_value = self.head.data
        cur = self.head.next
        while cur:
            if cur.data > max_value:
                max_value = cur.data
            cur = cur.next
        return max_value

    
    #19. def min() - find and return the minimum value in the list.
    def min(self):
        if self.head is None:
            return "The list is empty"
        min_value = self.head.data
        cur = self.head.next
        while cur is not None:
            if cur.data < min_val:
                min_val = cur.data
            cur = cur.next
        return min_val


    #20. def sum() - return the sum of all values in the list.

    def sum(self):
        sum = 0
        cur = self.head
        while cur is not None:
            sum += cur.data
            cur = cur.next
        return sum
    

    #21. def avg() - return the average of all values in the list.

    def avg(self):
        count = 0
        sum = 0
        if self.head is None:
            return "The list is empty"
        cur = self.head
        while cur is not None:
            count += 1
            sum += cur.data
            cur = cur.next
        return sum / count

    

    #22. def sorted() - check and return true if the list is sorted, return false if the list is not sorted.

    def sorted_check(self):
        if self.head is None:
            return "The list is empty"
        cur = self.head
        while cur.next is not None:
            if cur.data > cur.next.data:
                return False
            cur = cur.next
        return True


    #23. def insert(x) - insert node with value x into sorted list so that the new list is sorted.

    def insert(self, x):
        new = Node(x)
        if self.head is None or x < self.head.data:
            new.next = self.head
            self.head = new
            return 
        else:
            cur = self.head
            while cur.next is not None and cur.next.data < x:
                cur = cur.next
            new.next = cur.next
            cur.next = new
            return 

    
    #24. Reverse a singly linked list using only one pass through the list.
            
    # def reverse(self):
    #     prev = None
    #     current = self.head
        


    #25. Check whether two singly linked list have the same contents.
        
    def check_content(self, list1, list2):
        cur1 = list1.head
        cur2 = list2.head
        while (cur1 and cur2) is not None:
            if cur1.data != cur2.data:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1 == cur2 



lk = Singly_LinkedList()

# Add a node with value x  at the head of  a list.
lk.addToHead(2)
lk.addToHead(4)
lk.addToHead(3)


# Add a node with value x  at the tail of  a list.
lk.addToTail(5)
lk.addToTail(6)


