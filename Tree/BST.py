class Node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

class BST():
    def __init__(self):
        self.root = None
    
    def insert(self,new_node):
        if self.root == None:# this block is executed when BST is empty
            self.root = new_node
        else:
            tmp = self.root
            while True:
                if new_node.data < tmp.data:
                    if tmp.left == None:
                        tmp.left = new_node
                        return
                    else:
                        tmp = tmp.left
                else:
                    if tmp.right == None:
                        tmp.right = new_node
                        return
                    else:
                        tmp = tmp.right
    def inorder(self,rt):
        if rt == None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)
    def preorder(self,rt):
            if rt == None:
                return
            else:
                print(rt.data, end=" ")
                self.preorder(rt.left)
                self.preorder(rt.right)
    def postorder(self,rt):
            if rt == None:
                return
            else:
                self.postorder(rt.left)
                self.postorder(rt.right)
                print(rt.data, end=" ")
    def findmax(self):
        if self.root == None:
            print("Tree is Empty")
            return
        else:
            tmp = self.root
            while tmp.left:
                tmp = tmp.left
            print(f"Max Value in a tree : {tmp.data}")
    def findmin(self):
            if self.root == None:
                print("Tree is Empty")
                return
            else:
                tmp = self.root
                while tmp.right:
                    tmp = tmp.right
                print(f"Max Value in a tree : {tmp.data}")
    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            if level == 0:
                node = self.root
            if node is None:
                print("Tree is empty")
                return

        if node.right:
            self.print_tree(node.right, level + 1, "R--- ")

        print("    " * level + prefix + str(node.data))

        if node.left:
            self.print_tree(node.left, level + 1, "L--- ")
            
    # def del_node(self,)
    def get_successor(self,temp):
        temp = temp.right
        while temp is not None and temp.left is not None:
            temp = temp.left
        return temp





tree = BST()
values = [50, 30, 70, 20, 40, 60, 80, 35, 45]
# values = [100,10,450,0,65,300]
for value in values:
    tree.insert(Node(value))

# tree.print_tree()
print("Inorder")
tree.inorder(tree.root)
print()
print("Preorder")
tree.preorder(tree.root)
print()
print("Postorder")
tree.postorder(tree.root)            
print()

tree.findmax()  
tree.findmin()
        
tree.print_tree()
