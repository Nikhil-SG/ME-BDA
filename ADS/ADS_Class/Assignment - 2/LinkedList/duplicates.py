from SingleLL import SingleList

def remove_duplicates(self):
    if self.is_empty():
        return

    seen = set()
    current = self.head
    prev = None

    while current:
        if current.data in seen:
            prev.next = current.next
            if current == self.tail:
                self.tail = prev
        else:
            seen.add(current.data)
            prev = current

        current = current.next

def main():
    list1 = SingleList()
    list1.add_at_tail(10)
    list1.add_at_tail(20)
    list1.add_at_tail(10)
    list1.add_at_tail(30)
    list1.add_at_tail(20)
    list1.add_at_tail(40)
    
    print("Original list:")
    current = list1.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    list1.remove_duplicates()
    
    print("List after removing duplicates:")
    current = list1.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    SingleList.remove_duplicates = remove_duplicates
    main()
