import pytest
from singly_linked_list import SinglyLinkedList


class TestSLL:
    def setup_method(self):
        self.num_elements = 10

    def test_insert(self):
        lst = SinglyLinkedList()
        for i in range(self.num_elements):
            lst.insert_front(i)

        # Verify the linked list's representation matches the expected values
        assert (
            repr(lst)
            == f"SinglyLinkedList({','.join(str(i) for i in range(self.num_elements - 1, -1, -1))})"
        )

    def test_membership(self):
        lst = SinglyLinkedList()
        for i in range(self.num_elements):
            lst.insert_front(i)

        # Check for membership
        for i in range(self.num_elements):
            assert i in lst

        # Check for a value that should not be present
        assert 100 not in lst

    def test_std_iteration(self):
        lst = SinglyLinkedList()
        for i in range(self.num_elements):
            lst.insert_front(i)

        # Verify the iteration yields the correct elements
        expected_values = list(
            range(self.num_elements - 1, -1, -1)
        )  # Reverse order due to insert_front
        assert list(lst) == expected_values
