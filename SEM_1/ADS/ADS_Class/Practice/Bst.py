class BST:
    class Node:
        def __init__(self,ele):
            self.data = ele
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None
        self.count = 0

    def Isempty(self):
        return self.count == 0
    
    def count(self):
        return self.count
    
    def Add(self,ele):
        cur = parent = self.root
        while cur != None and ele != cur.data:
            parent = cur
            if ele < cur.data:
                cur = cur.left
            elif ele > cur.data:
                cur = cur.right

        if cur == None:
            new_node = self.Node(ele)
            if parent == None:
                self.root = new_node
            elif ele < parent.data:
                parent.left = new_node
            elif ele > parent.data:
                parent.right = new_node
            self.count += 1

    def Ismember(self,key):
        if not self.Isempty():
            cur = self.root
            while cur:
                if key < cur.data:
                    cur = cur.left
                elif key > cur.data:
                    cur = cur.right
                else:
                    return True
            return cur != None
        else:
            return None
        
    def Levelorder(self):
        if not self.Isempty():
            queue = Flexiqueue()
            queue.enqueue(self.root)
            while not queue.Iempty():
                node = queue.dequeue()
                print(node)
                if node.left:
                    queue.enqueue(node.left)
                elif node.right:
                    queue.enqueue(node.right)

    def DeleteNode(self,key):
        if not self.Isempty():
            self.root = self.Delete(self.root,key)

    def Delete(self,node,key):
        if node is None:
            return None
        if key < node.data:
            self.Delete(node.left,key)
        elif key > node.data:
            self.Delete(node.right,key)
        else:
            if node.left and node.right:
                temp = FindMin(node.right,key)
                node.data = temp.data
                node.right = self.Delete(node.right,temp.data)
            elif node.left:
                node = node.right
            elif node.right:
                node = node.left
            self.count -= 1
        return node
    
    def FindMin(self,node,key):
        if node.left is None:
            return node
        else:
            return(self.find(node.left,key))