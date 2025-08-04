class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
class BSTree:
    def __init__(self):
        self.root=None
    def insertNode(self,node,val):
        n=Node(val)
        if self.root==None:
            self.root=n
            print(f"roote node is addded {val}")
            return
        if val<node.val:
            if node.left==None:
                node.left=n
                print(f"node is added left side{val}")
            else:
                self.insertNode(node.left,val)
        else:
            if node.right==None:
                node.right=n
                print(f"node is added right side{val}")
            else:
                self.insertNode(node.right,val)
b=BSTree()
b.insertNode(None,10)
b.insertNode(b.root,5)
b.insertNode(b.root,11)
b.insertNode(b.root,9)
b.insertNode(b.root,15)

