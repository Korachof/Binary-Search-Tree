class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        current_node = self.root

        while True:
            if new_node.value == current_node.value:
                return False

            elif new_node.value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return True

                else:
                    current_node = current_node.left

            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return True

                else:
                    current_node = current_node.right

    def contains(self, value):
        if self.root is None:
            return False

        check_node = self.root

        while check_node is not None:
            if check_node.value == value:
                return True