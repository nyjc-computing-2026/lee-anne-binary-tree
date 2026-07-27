class Node:
    """Node class for binary tree storing student records."""

    def __init__(self, id: int, name: str):
        """Initialize a new node with student record.

        Args:
            id: Student ID (used as sorting key)
            name: Student name
        """
        self.id = id
        self.name = name
        self.left = None
        self.right = None

    def preorder(self) -> list[dict]:
        """Return preorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in preorder (root, left, right)
        """
        # Replace this code with your implementation
        result = [{"id": self.id, "name": self.name}]
        if self.left:
            result += self.left.preorder()

        if self.right:
            result += self.right.preorder()

        return result
    
    
    def inorder(self) -> list[dict]:
        """Return inorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in inorder (left, root, right)
        """
        # Replace this code with your implementation
        result = []
        if self.left: 
            result += self.left.inorder()

        result.append({"id": self.id, "name": self.name})

        if self.right:
            result += self.right.inorder()

        return result

            

    def postorder(self) -> list[dict]:
        """Return postorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in postorder (left, right, root)
        """
        # Replace this code with your implementation
        result = []

        if self.left:
            result += self.left.postorder()

        if self.right: 
            result += self.right.postorder()

        result.append({"id": self.id, "name": self.name})
        return result 


class Tree:
    """Binary search tree for storing and managing student records."""

    def __init__(self):
        """Initialize an empty tree."""
        self.root = None

    def add(self, id: int, name: str) -> None:
        """Add a new student record to the tree.

        Args:
            id: Student ID (used as sorting key)
            name: Student name

        Note:
            If id already exists, this operation should be ignored.
        """
        # Replace this code with your implementation
        newnode = Node(id, name)
        
        if self.root == None:
            self.root = newnode
            return

        current = self.root

        while True:
            if id < current.id:
                if current.left == None:
                    current.left = newnode
                    return
                current = current.left

            elif id > current.id:
                if current.right == None:
                    current.right = newnode
                    return
                current = current.right

            else:
                return
            


    def find_node(self, id: int):
        """Find a student node by ID.

        Args:
            id: Student ID to search for

        Returns:
            Node object if found, None otherwise
        """
        # Replace this code with your implementation
        current = self.root
        while current:
            if id == current.id:
                return current
            elif current.id > id:
                current = current.left
            else:
                current = current.right

            return None

    def preorder(self) -> list[dict]:
        """Return preorder traversal of tree.

        Returns:
            List of {id, name} dicts in preorder (root, left, right)
        """
        # Replace this code with your implementation
        if self.root:
            return self.root.preorder()
        return []

    def inorder(self) -> list[dict]:
        """Return inorder traversal of tree.

        Returns:
            List of {id, name} dicts in inorder (left, root, right)
        """
        # Replace this code with your implementation
        if self.root:
            return self.root.inorder()
        return []

    def postorder(self) -> list[dict]:
        """Return postorder traversal of tree.

        Returns:
            List of {id, name} dicts in postorder (left, right, root)
        """
        # Replace this code with your implementation
        if self.root:
            return self.root.postorder()
        return []


# Sample data for testing
if __name__ == "__main__":
    # Create a new tree
    tree = Tree()

    # Add sample student records
    # Format: tree.add(id, name)
    tree.add(50, "Alice")
    tree.add(30, "Bob")
    tree.add(70, "Charlie")
    tree.add(20, "Diana")
    tree.add(40, "Eve")
    tree.add(60, "Frank")
    tree.add(80, "Grace")

    print("Tree created with sample data:")
    print(f"Inorder traversal (sorted by ID): {tree.inorder()}")
    print(f"Preorder traversal: {tree.preorder()}")
    print(f"Postorder traversal: {tree.postorder()}")

    # Test find_node
    print("\nTesting find_node:")
    node = tree.find_node(30)
    if node:
        print(f"Find ID 30: Found node with id={node.id}, name={node.name}")
    else:
        print("Find ID 30: Not found")

    node = tree.find_node(999)
    if node:
        print(f"Find ID 999: Found node with id={node.id}, name={node.name}")
    else:
        print("Find ID 999: Not found")

    print("\nTest complete! Run 'python test_main.py' to run automated tests.")
