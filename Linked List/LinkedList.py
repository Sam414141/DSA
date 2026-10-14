class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def newNode():
    data = int(input("Enter value :"))
    return Node(data)

class LinkedList:
    head = None
    tail = None
    def __init__(self):
        self.head= None
    def insert_at_begining(self, new_node):
        tmp = self.head.next
        self.head = new_node
        
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
        
    def push(self, new_node : Node):
        if self.base == None:
            self.base = new_node
        else:
            temp = self.base
            while temp.next:
                temp.next = new_node
        
    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def del_node(self, value):
        tmp = self.head
        prev = None
        if tmp.data == value: #First node to delete
            self.head = self.head.next
        else:
            while tmp.data == value:
                prev = tmp
                tmp = tmp.next
                if tmp == None:
                    print("Value is not present in LinkedList")
                    return
            prev.next = tmp.next
            tmp = None
            
    def insert(self, new_node, pos):
        if pos == 1: # insert at the begining
            new_node.next = self.head
            self.head = new_node
        else:
            p=1
            temp = self.head
            while(p!=pos-1):
                temp = temp.next
                p+=1
            new_node.next = temp.next
            temp.next = new_node
            
my_list = LinkedList()
while True:
    print("---Linked List Operations---")
    print("Operetion List")
    print("")
    print("0.Exit")
    print("1.Insert New Node At Begining ---")
    print("2.Insert New Node At Specific Position ---")
    print("3.Insert New Node At End ---")
    print("4.Delete Node By Value ---")
    print("5.Delete Node By Position ---")
    print("6.Delete First Node ---")
    print("7.Delete last Node ---")
    print("8.Print List ---")
    print("9.Search Value ---")
    print("10.Is Empty ---")
    ch = input("Enter your choice :")
    if ch == 0:
        break
    if ch <=10 and ch >=0:
        match ch:
            case 1:
                insert_at_begining(newNode())
                break
            case 2:
                break
            case 3:
                break    
            case 4:
                break
            case 5:
                break
            case 6:
                break
            case 7:
                break
            case 8:
                break
            case 9:
                break
            case 10:
                break
# n1 = Node(11)
# n2 = Node(12)
# n3 = Node(13)
# n4 = Node(14)
# n5 = Node(15)
# my_list.append(n1)
# my_list.append(n2)
# my_list.append(n3)
# my_list.append(n4)
# my_list.insert(n5,1)
# my_list.print()