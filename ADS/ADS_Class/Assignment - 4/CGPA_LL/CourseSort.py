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
            while sorted_node and sorted_node.cgpa >= current.cgpa:  # Descending order
                prev = sorted_node
                sorted_node = sorted_node.next

            if sorted_node:
                prev.next = current
                current.next = sorted_node
            else:
                sorted_list.head = current

            current = next_node

        self.head = sorted_list.head

    def print_list(self):
        current = self.head
        while current:
            print(f"Course Number: {current.registration_number}, Program: {current.program}, CGPA: {current.cgpa}")
            current = current.next

def create_program_wise_sorted_lists(linked_list):
    program_lists = {}
    current = linked_list.head

    while current:
        program = current.program
        if program not in program_lists:
            program_lists[program] = LinkedList()
        program_lists[program].insert_node(current.registration_number, current.program, current.cgpa)
        current = current.next

    for program, program_list in program_lists.items():
        program_list.sort_by_cgpa()
        program_list.print_list()

# Example usage
linked_list = LinkedList()
linked_list.insert_node("1", "BDA", 9.5)
linked_list.insert_node("2", "AIML", 7.8)
linked_list.insert_node("3", "VLSI", 9.2)
linked_list.insert_node("4", "MVT", 8.0)
linked_list.insert_node("5", "CC", 9.0)
linked_list.insert_node("6", "EMD", 8.2)

create_program_wise_sorted_lists(linked_list)