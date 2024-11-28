from SingleLL import SingleList

def find_middle(self):
    if self.is_empty():
        return None

    slow = self.head
    fast = self.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data

def main():
    list1 = SingleList()
    list1.add_at_tail(10)
    list1.add_at_tail(20)
    list1.add_at_tail(30)
    list1.add_at_tail(40)
    list1.add_at_tail(50)
    
    print("List:")
    current = list1.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    middle = list1.find_middle()
    if middle is not None:
        print(f"The middle element is: {middle}")
    else:
        print("The list is empty.")

if __name__ == "__main__":
    SingleList.find_middle = find_middle
    main()
