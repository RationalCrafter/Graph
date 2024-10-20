# A simple implementation of a singly linked list in python
class Node:
    """Class Node: Defines a basic element in a singly linked list.
    Each node instance contains 2 attributes a key and a reference to
    the next element in the linked list."""

    __slots__ = "key", "next_node"

    def __init__(self, key=None, next_node=None):
        self.key = key
        self.next_node = next_node

    def __repr__(self) -> str:
        return f"Node(key={self.key}, next_node={self.next_node})"


class SinglyLinkedList:
    __slots__ = "head", "current_node"

    def __init__(self, key=None, linked_list=None):
        """Default constructor for the SinglyLinkedList data structure.

        Accepts up to 2 arguments: a key(data) and a list. If a key is provided
        without an accompanying reference to a list, it will be assumed that the list
        is empty and the user is creating the first node. If a linked_list is provided,
        it'll be assumed that this node is being inserted into an existing list."""

        if linked_list is not None:
            self.head = Node(key, linked_list.head)
        elif key is not None:
            self.head = Node(key, None)
        else:
            self.head = None
        # used to traverse the list
        self.current_node = self.head

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.key))
            current = current.next_node
        return f"SinglyLinkedList({','.join(nodes)})"

    def is_empty(self):
        """Check's if the current linked list contains any nodes.

        Returns True if the list is empty and False, otherwise."""
        if self.head is None or self.head.key is None:
            return True
        return False

    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_node is None:
            print("Raising StopIteration")
            raise StopIteration
        key = self.current_node.key
        self.current_node = self.current_node.next_node
        return key

    def insert_front(self, key):
        """Inserts a key into a linked list.

        This method creates a node for an element
        with the specified key at the start of the list."""
        if key is not None:
            self.head = Node(key, self.head)

    def delete_front(self):
        """Deletes the head of the linked list and returns its key, if the list is not empty."""
        if self.head is not None:
            key = self.head.key
            self.head = self.head.next_node
            return key
        return None


if __name__ == "__main__":
    print("Debugging and Benchmarks (invoked directly)")
    # testing basic functionality
    print("Creating a node...")
    print("Node with no arguments to the constructor")
    testNode = Node()
    if testNode.key is None:
        print("testNode.key: OK!")
    if testNode.next_node is None:
        print("testNode.next_node: OK!")
    print("Node with a key argument to the constructor")
    testNode = Node(key=2)
    if testNode.key == 2:
        print("testNode.key: OK!")
    if testNode.next_node is None:
        print("testNode.next_node: OK!")
    print("Node with all arguments to the constructor")
    testNode = Node(key=2, next_node=Node(key=3))
    if testNode.key == 2:
        print("testNode.key: OK!")
    if testNode.next_node is not None:
        print(
            f"testNode.next_node!=None\ntestNode.next_node={testNode.next_node}\ntestNode.next_node.key={testNode.next_node.key}"
        )
    # test inserting a larger number of keys
    print("Inserting elements on the list")
    NUM_KEYS = 10
    linked_list = SinglyLinkedList()
    print(f"is_empty status == {linked_list.is_empty()}")
    for k in range(NUM_KEYS):
        linked_list.insert_front(k)
        print(f"Inserting k={k}")
        print(f"List head={linked_list.head}")

    print("Insertion Completed.\nNew status:")
    print(f"is_empty status == {linked_list.is_empty()}")

    print("Testing default iteration")
    for k in linked_list:
        print(f"Retrieved key = {k}")

    print(f"5 in linked_list? {5 in linked_list}")
