print('''
Name: Hoàng Thái Dương
ID: HE181802
Class: AI1811
''')


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Circular_LinkedList:
    def __init__(self):
        self.head = None


    #1. def addToHead(x) - add a node with value x at the head of a list.

    def addToHead(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            new.next = new
        else:
            new.next = self.head
            node = self.head
            while node.next != self.head:
                node = node.next
            node.next = new
            self.head = new

    
    #2. def addToTail(x) - add a node with value x  at the tail of  a list.

    def addToTail(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            new.next = new
        else:
            node = self.head
            while node.next != self.head:
                node = node.next
            node.next = new
            new.next = self.head


    #3. def addAfter(p, x) - add a node with value x  after the node p.

    def addAfter(self, target, data):
        if not self.head:
            return None
        else:
            node = self.head
            while node.data != target:
                node = node.next
                if node == self.head:
                    return None
            new = Node(data)
            new.next = node.next
            node.next = new


    #4. def traverse() - traverse from head to tail and dislay info of all nodes in the list.

    def traverse(self):
        if not self.head:
            return None
        else:
            node = self.head
            while True:
                print(node.data, end = ' ')
                node = node.next
                if node == self.head:
                    break
            print()

    
    #5. def deleteFromHead() - delete the head and return its info.

    def deleteFromHead(self):
        if not self.head:
            return None
        else:
            node = self.head
            while node.next != self.head:
                node = node.next
            deleted_data = self.head.data
            node.next = self.head.next
            self.head = self.head.next
            return deleted_data


    #6. def deleteFromTail() - delete the tail and return its info. 

    def deleteFromTail(self):
        if not self.head:
            return None
        else:
            prev_node = self.head
            cur_node = self.head.next
            while cur_node.next != self.head:
                prev_node = cur_node
                cur_node = cur_node.next
            del_data = cur_node.data
            prev_node.next = cur_node.next
            return del_data


    #7. def deleteAter(p) - delete the node after the node  p  and return its info.

    def deleteAfter(self, p):
        if not self.head:
            return None
        else:
            node = self.head
            while node.data != p:
                node = node.next
                if node == self.head:
                    return None
            del_data = node.next.data
            node.next = node.next.next
            return del_data

    
    #8. def del(x) - delele the first node whose info is equal to x.

    def del_Node_equal(self, x):
        if not self.head:
            return None
        else:
            if self.head.data == x:
                del_data = self.head.data
                self.deleteFromHead()
                return del_data
            else:
                node = self.head
                while node.next.data != x:
                    node = node.next
                    if node.next == self.head:
                        return None
                del_data = node.next.data
                node.next = node.next.next
                return del_data


    #9. def search(x) - search and return the reference to the first node having info x.  

    def search(self, x):
        if not self.head:
            return None
        else:
            node = self.head
            while node.data != x:
                node = node.next
                if node == self.head:
                    return None
            return node
        

     #10. def count() - count and return number of nodes in the list. 

    def count(self):
        if not self.head:
            return 0
        else:
            count = 0
            node = self.head
            while True:
                count += 1
                node = node.next
                if node == self.head:
                    break
            return count
        

    #11. def del(i) - delete an i-th node on the list. Besure that such a node exists.

    def delete_node(self, index):
        if not self.head:
            return None
        else:
            if index == 0:
                self.deleteFromHead()
            else:
                node = self.head
                count = 0
                while count < index - 1 and node.next != self.head:
                    node = node.next
                    count += 1
                if count == index - 1:
                    node.next = node.next.next


    #12. def sort() - sort the list by ascending order of info. 

    def sort(self):
        if not self.head:
            return None
        else:
            node = self.head
            while node.next != self.head:
                node2 = node.next
                while node2 != self.head:
                    if node.data > node2.data:
                        node.data, node2.data = node2.data, node.data
                    node2 = node2.next
                node = node.next


    #13. def del(p) - delete node p if it exists in the list.

    def deleteNode(self, target_node):
        if not self.head:
            return None
        else:
            if self.head == target_node:
                self.deleteFromHead()
            else:
                node = self.head
                while node.next != target_node:
                    node = node.next
                    if node.next == self.head:
                        return None
                node.next = node.next.next


    #14. def toArray() - create and return array containing info of all nodes in the list.

    def toArray(self):
        if not self.head:
            return []
        else:
            arr = []
            node = self.head
            while True:
                arr.append(node.data)
                node = node.next
                if node == self.head:
                    break
            return arr
        

# Test case:
# Linked list
lk = Circular_LinkedList()

# Test addToHead
lk.addToHead(4)
lk.addToHead(5)
lk.addToHead(6)
lk.addToHead(9)
lk.addToHead(8)
print("List sau khi thêm vào đầu: ", end = ' ')
lk.traverse()  # Output: 8 9 6 5 4

# Test addToTail
lk.addToTail(2)
lk.addToTail(1)
print("List sau khi thêm vào cuối: ", end = ' ')
lk.traverse()  # Output: 8 9 6 5 4 2 1

# Test addAfter
lk.addAfter(9, 10)
print("Chuỗi sau khi thêm 10 vào sau 9 : ", end = ' ')
lk.traverse()  # Output: 8 9 10 6 5 4 2 1

# Test deleteFromHead
cur = lk.deleteFromHead()
print("Node bị xóa: ", cur, " List sau khi xóa node đầu: ", end = ' ')
lk.traverse()  # Output: 9 10 6 5 4 2 1

# Test deleteFromTail
cur1 = lk.deleteFromTail() 
print("Node bị xóa: ", cur1, " List sau khi bị xóa node cuối: ", end = ' ')
lk.traverse() # Output: 9 10 6 5 4 2

# Test deleteAfter
cur2 = lk.deleteAfter(10)
print("Node bị xóa: ", cur2, " List sau khi bị xóa node sau node 10: ", end = ' ') 
lk.traverse() # Output: 9 10 5 4 2

# Test del_Node_equal()
cur3 = lk.del_Node_equal(5)
print("Node bị xóa: ", cur3, " List sau khi bị xóa node có data = 5: ", end = ' ') 
lk.traverse() # Output: 9 10 4 2

# Test search()
x = 4
print('The node có info:', x)
print(lk.search(x))

# Test count()
print("Số phần tử của list: ",lk.count()) # Output = 4


# Test delete_node()
i = 2
lk.delete_node(i)
print("List sau khi xóa node thứ", i,": ", end = ' ')
lk.traverse() # Output = 9 10 2

# Test sort()
lk.sort()
print("List mới sau khi sắp xếp: ", end = ' ')
lk.traverse() # Output = 2 9 10

# Test toArray()
print("Chuyển list này thành array: ",lk.toArray())
        
    
