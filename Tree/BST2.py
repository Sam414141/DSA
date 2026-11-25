class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BST():
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        new_node = Node(data)
        if self.root == None:
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
    
    def preorder(self,rt):
        if rt == None:
            return
        else:
            print(rt.data ,end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
            return
            
    def inorder(self,rt):
        if rt == None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)
    def postorder(self,rt):
        if rt == None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data,end=" ")
    
tree = BST()                
values = [50, 30, 70, 20, 40, 60, 80, 35, 45]
for i in values:
    tree.insert(i)

print("Preorder =",end=" ")
tree.preorder(tree.root)
print()
print("Inorder = ",end=" ")
tree.inorder(tree.root)
print()
print("Postorder = ",end=" ")
tree.postorder(tree.root)


# tree.print_tree()