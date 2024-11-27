class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def get_count(self):
        def count_nodes(node):
            if node is None:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        return count_nodes(self.root)

    def add_node(self, data):
        def insert_node(node, data):
            if node is None:
                return Node(data)
            if data < node.data:
                node.left = insert_node(node.left, data)
            else:
                node.right = insert_node(node.right, data)
            return node

        self.root = insert_node(self.root, data)

    def search_node(self, data):
        def search_node_helper(node, data):
            if node is None or node.data == data:
                return node
            if data < node.data:
                return search_node_helper(node.left, data)
            else:
                return search_node_helper(node.right, data)

        return search_node_helper(self.root, data)

    def in_order_traversal(self):
        def in_order(node):
            if node is None:
                return
            in_order(node.left)
            print(node.data)
            in_order(node.right)

        in_order(self.root)

    def pre_order_traversal(self):
        def pre_order(node):
            if node is None:
                return
            print(node.data)
            pre_order(node.left)
            pre_order(node.right)

        pre_order(self.root)

    def post_order_traversal(self):
        def post_order(node):
            if node is None:
                return
            post_order(node.left)
            post_order(node.right)
            print(node.data)

        post_order(self.root)

    def level_order_traversal(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def delete_node(self, data):
        def delete_node_helper(node, data):
            if node is None:
                return None

            if data < node.data:
                node.left = delete_node_helper(node.left, data)
            elif data > node.data:
                node.right = delete_node_helper(node.right, data)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    successor = node.right
                    while successor.left:
                        successor = successor.left
                    node.data = successor.data
                    node.right = delete_node_helper(node.right, successor.data)

            return node

        self.root = delete_node_helper(self.root, data)

    def find_height(self):
        def find_height_helper(node):
            if node is None:
                return 0
            return 1 + max(find_height_helper(node.left), find_height_helper(node.right))

        return find_height_helper(self.root)
    
    def print_list(self):
       return self.in_order_traversal()
    
if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.add_node(50)
    bst.add_node(30)
    bst.add_node(70)
    bst.add_node(20)
    bst.add_node(40)
    bst.add_node(60)
    bst.add_node(80)

 
    print("Is the BST empty?", bst.is_empty())

    print("Number of nodes:", bst.get_count())

    node = bst.search_node(40)
    if node:
        print("Node found:", node.data)
    else:
        print("Node not found")

    print("In-order traversal:")
    bst.in_order_traversal()
    print("Pre-order traversal:")
    bst.pre_order_traversal()
    print("Post-order traversal:")
    bst.post_order_traversal()
    print("Level-order traversal:")
    bst.level_order_traversal()

    bst.delete_node(30)
    print("After deletion:")
    bst.print_list()

    print("Height of the BST:", bst.find_height())