import numpy as np
class Node:

    def __init__(self, data):
        self.left = None
        self.Data = data
        self.right = None

    def insertData(self, data):
        if self.Data:
            if self.Data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertData(data)
            elif self.Data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertData(data)
        else:
            self.Data = data

    def leftRootRight_Traverse(self):
        if self.left:
            self.left.leftRootRight_Traverse()
        print(self.Data)
        if self.right:
            self.right.leftRootRight_Traverse()

#Insert the values in the root node
root = Node(10)
#To Insert data in right or left side node.
root.insertData(5)
root.insertData(15)
root.insertData(1)
root.insertData(6)

# T0print the values from left to root then right.
root.leftRootRight_Traverse()

array=np.array([5,4,8,7])
#
root = node(10)
i=0
for i in range(0,3):
    root.inserNode(array[i])
(root.LeftrootRight_Traverse())