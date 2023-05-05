class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = True  # True for red, False for black

class LLRBTREE:
    def __init__(self):
        self.root = None
    
    # Function to perform left rotation on the given node
    def rotateLeft(self, node):
        print("Left rotation!!")
        child = node.right
        childLeft = child.left

        child.left = node
        node.right = childLeft

        return child
    
    # Function to perform right rotation on the given node
    def rotateRight(self, node):
        print("Right rotation!!")
        child = node.left
        childRight = child.right

        child.right = node
        node.left = childRight

        return child
    
    # Function to check if a node is red or not
    def isRed(self, node):
        if node is None:
            return False
        return node.color
    
    # Function to swap colors of two nodes
    def swapColors(self, node1, node2):
        temp = node1.color
        node1.color = node2.color
        node2.color = temp
    
    # Function to insert a new node in the left-leaning Red-Black Tree
    def insert(self, node, data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        else:
            return node
        
        # Case 1
        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotateLeft(node)
            self.swapColors(node, node.left)
        
        # Case 2
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
            self.swapColors(node, node.right)
        
        # Case 3
        if self.isRed(node.left) and self.isRed(node.right):
            node.color = not node.color
            node.left.color = False
            node.right.color = False
        
        return node
    
    # Function to do inorder traversal of the tree
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            c = '●' if node.color else '◯'
            print(str(node.data) + c + " ", end='')
            self.inorder(node.right)

if __name__ == '__main__':
    llrbTree = LLRBTREE()
    
    while True:
        num = int(input("Enter an integer: "))
        llrbTree.root = llrbTree.insert(llrbTree.root, num)
        llrbTree.inorder(llrbTree.root)
        
        ch = input("\nDo you want to continue? (y/n): ")
        if ch.lower() != 'y':
            break
