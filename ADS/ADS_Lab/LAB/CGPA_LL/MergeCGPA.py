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

    def merge_by_cgpa(self, other_list):
        merged_list = LinkedList()
        current1 = self.head
        current2 = other_list.head
        
        while current1 and current2:
            if current1.cgpa >= current2.cgpa:  # Use >= for descending order
                merged_list.insert_sorted(current1.registration_number, current1.program, current1.cgpa)
                current1 = current1.next
            else:
                merged_list.insert_sorted(current2.registration_number, current2.program, current2.cgpa)
                current2 = current2.next

        # Append remaining nodes from the longer list
        while current1:
            merged_list.insert_sorted(current1.registration_number, current1.program, current1.cgpa)
            current1 = current1.next

        while current2:
            merged_list.insert_sorted(current2.registration_number, current2.program, current2.cgpa)
            current2 = current2.next

        return merged_list

    def insert_sorted(self, registration_number, program, cgpa):
        new_node = Node(registration_number, program, cgpa)
        if not self.head or self.head.cgpa < cgpa:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.cgpa >= cgpa:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(f"Registration Number: {current.registration_number}, Program: {current.program}, CGPA: {current.cgpa}")
            current = current.next

# Example usage
list1 = LinkedList()
list1.insert_node("1", "BDA", 8.5)
list1.insert_node("2", "BDA", 7.8)
list1.insert_node("3", "BDA", 9.2)
list1.insert_node("4", "BDA", 8.0)
list1.insert_node("5", "BDA", 8.6)
list1.insert_node("6", "BDA", 8.2)
list1.insert_node("7", "BDA", 9.3)
list1.insert_node("8", "BDA", 9.4)
list1.insert_node("9", "BDA", 8.0)
list1.insert_node("10", "BDA", 8.0)

list2 = LinkedList()
list2.insert_node("1", "AIML", 8.9)
list2.insert_node("2", "AIML", 8.7)
list2.insert_node("3", "AIML", 9.0)
list2.insert_node("4", "AIML", 8.1)
list2.insert_node("5", "AIML", 8.6)
list2.insert_node("6", "AIML", 8.3)
list2.insert_node("7", "AIML", 9.3)
list2.insert_node("8", "AIML", 9.1)
list2.insert_node("9", "AIML", 7.2)
list2.insert_node("10", "AIML", 7.0)

print("List 1:")
list1.print_list()

print("List 2:")
list2.print_list()

merged_list = list1.merge_by_cgpa(list2)

print("Merged List (Descending CGPA):")
merged_list.print_list()
