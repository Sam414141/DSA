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
    def Print_Node(self, pos):
        if self.head == None:
            print("List is Empty")
        else:
            p = 1
            tmp = self.head
            while p != pos:
                tmp = tmp.next
                p+=1
            print(tmp.data)
                    
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
    # Delete First Node
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
                self.size -= 1   
            else:
                print("List is Empty !!")
    def print_size(self):
        print(self.size)
    def print_mid(self):
        mid = (self.size//2)+1
        print("Middle Node is :")
        self.Print_Node(mid)
    # 6. Reverse Linked List
    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("List reversed successfully!")
    # Sum of consecutive numbers
    def sum_consecutive_pairs(self):
        if self.head is None or self.head.next is None:
            print("At least two nodes are required!")
            return
        tmp = self.head
        while tmp.next is not None:
            total = tmp.data + tmp.next.data
            print(f"{tmp.data} + {tmp.next.data} = {total}")
            tmp = tmp.next
    # reverse function
    # def rev(self):
    #     tmp = self.head
    #     prev = None
    #     while(tmp):
    #         next = tmp.next()
    
    # Find Mid and delete
    # def findmid_del(self):
    #     temp = 

    # Delete First and last node
    def del_first_n_last(self):
        tmp = self.head
        self.head = tmp.next
        
        tmp = self.head
        prev = tmp
        while tmp.next != None: 
            prev = tmp
            tmp = tmp.next
        prev.next = None
        tmp = None
mylist = LinkedList()

# 1. Create Linked List
mylist.append(Node(11))
mylist.append(Node(12))
mylist.append(Node(13))
mylist.append(Node(14))
mylist.append(Node(15))
mylist.append(Node(16))




print("1. Created Linked List:")
mylist.Print()

print()
mylist.del_first_n_last()
mylist.Print()
# # 2. Traverse and print node values
# print("\n2. Traverse Linked List:")
# mylist.Print()

# # 3. Insert node at a specific position
# print("\n3. Insert 99 at position 3:")
# mylist.insert(Node(99), 3)
# mylist.Print()

# # 4. Find Middle node
# print("\n4. Find Middle Node:")
# mylist.print_mid()

# # 5. Delete node
# print("\n5. Delete Head Node:")
# mylist.delete_head()
# mylist.Print()

# # 6. Reverse List
# print("\n6. Reverse Linked List:")
# mylist.reverse_list()
# mylist.Print()

# # 7. Sum of every two consecutive node values
# print("\n7. Sum of Consecutive Node Values:")
# mylist.sum_consecutive_pairs()
