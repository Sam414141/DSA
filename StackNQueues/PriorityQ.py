class Node():
    def __init__(self,data,pr):
        self.data = data
        self.priority = pr
        self.next = None
        
class Prq():
    def __init__(self,new_node):
        self.front = new_node
        
    def enqueue(self,new_node):
        if self.front == None:
            self.front = new_node
        else:
            prev = self.front
            tmp = self.front
            while tmp:
                if tmp.priority >= new_node.priority:
                    new_node.next = tmp
                    tmp.next = new
                    
                