class Node:
    def __init__(self, registration_number, program, cgpa):
        self.registration_number = registration_number
        self.program = program
        self.cgpa = cgpa
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, registration_number, program, cgpa):
        new_node = Node(registration_number, program, cgpa)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def sort_by_cgpa(self):
        if not self.head or not self.head.next:
            return

        sorted_list = LinkedList()
        current = self.head

        while current:
            next_node = current.next
            current.next = None  

            sorted_node = sorted_list.head
            prev = None
            while sorted_node and sorted_node.cgpa >= current.cgpa:  # Use >= for descending order
                prev = sorted_node
                sorted_node = sorted_node.next

            if prev:
                prev.next = current
            else:
                sorted_list.head = current
            current.next = sorted_node

            current = next_node

        self.head = sorted_list.head

    def print_list(self):
        current = self.head
        while current:
            print(f"Registration Number: {current.registration_number}, Program: {current.program}, CGPA: {current.cgpa}")
            current = current.next

linked_list = LinkedList()
linked_list.insert_node("1", "BDA", 8.5)
linked_list.insert_node("2", "BDA", 7.8)
linked_list.insert_node("3", "BDA", 9.2)
linked_list.insert_node("4", "BDA", 8.0)
linked_list.insert_node("5", "BDA", 8.6)
linked_list.insert_node("6", "BDA", 8.2)
linked_list.insert_node("7", "BDA", 9.3)
linked_list.insert_node("8", "BDA", 9.0)
linked_list.insert_node("9", "BDA", 8.0)
linked_list.insert_node("10", "BDA", 8.0)

print("Before sorting:")
linked_list.print_list()

linked_list.sort_by_cgpa()

print("After sorting:")
linked_list.print_list()