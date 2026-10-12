class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList():
    head = None
    tail = None
    size = 0        
    def Print(self):
        if self.head == None:
            print("List is Empty")
        else:
            tmp = self.head
            while tmp != None:
                print(tmp.data)
                tmp = tmp.next
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.size += 1
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = new_node
            self.tail = new_node
            self.size += 1
    def insert(self, new_node, pos):
        if pos >= 0 and pos <= self.size:
            if self.head == None:
                self.head = new_node
            else:
                if pos == 1:
                    self.insert_at_head(new_node)
                else:
                    tmp = self.head
                    p = 1
                    while p < pos-1:
                        tmp = tmp.next
                        p += 1
                    new_node.next = tmp.next
                    tmp.next = new_node
                    self.size += 1            
        else:
            print("Invalid Index")               
            del new_node
    def insert_at_head(self,new_node):
        if self.head == None:
            self.head = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
    def delete_head(self):
        if self.size != 0:
            tmp = self.head.next
            self.head = tmp
            self.size -= 1
        else:
            print("List is Empty !!")
    def delete_tail(self):
            if self.size != 0:
                tmp = self.head
                prev = tmp
                while tmp.next != None:
                    prev = tmp
                    tmp = tmp.next
                prev.next = None
                tmp = None   
            else:
                print("List is Empty !!")
    def delete_by_value(self, val):
        if self.size != 0:
            tmp = self.head
            prev = self.head
            while tmp.next != None:
                if tmp.data == val:
                    prev.next = tmp.next
                    tmp = None
                else:
                    prev = tmp
                    tmp = tmp.next
        else:
            print("List is Empty !!")
    
mylist = LinkedList()
mylist.append(Node(11))
mylist.append(Node(12))
mylist.append(Node(13))
mylist.append(Node(14))
mylist.insert(Node(11),1)
mylist.delete_head()
mylist.delete_tail()
mylist.delete_by_value(12)
mylist.Print()