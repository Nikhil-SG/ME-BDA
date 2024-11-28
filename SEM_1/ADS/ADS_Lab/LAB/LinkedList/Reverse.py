from SingleLL import SingleList

def reverse(self):
    prev = None
    current = self.head
    self.tail = self.head  # The old head will become the new tail

    while current:
        next_node = current.next  # Save the next node
        current.next = prev  # Reverse the link
        prev = current  # Move prev to the current node
        current = next_node  # Move to the next node

    self.head = prev  # Update head to the new front of the list

SingleList.reverse = reverse  # Add the reverse method to SingleList

def main():
    # Create a linked list and populate it
    list1 = SingleList()
    list1.add_at_tail(10)
    list1.add_at_tail(20)
    list1.add_at_tail(30)
    list1.add_at_tail(40)
    list1.add_at_tail(50)
    
    # Print the original list
    print("Original list:")
    current = list1.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    # Reverse the list
    list1.reverse()
    
    # Print the reversed list
    print("Reversed list:")
    current = list1.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    main()
