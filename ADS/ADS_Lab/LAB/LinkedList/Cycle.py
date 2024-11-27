from SingleLL import SingleList

def has_cycle(self):
    if self.is_empty():
        return False

    slow = self.head
    fast = self.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True

    return False

def main():
    list1 = SingleList()
    list1.add_at_tail(10)
    list1.add_at_tail(20)
    list1.add_at_tail(30)
    list1.add_at_tail(40)
    list1.add_at_tail(50)

    list1.tail.next = list1.head.next

    print("List with potential cycle:")
    current = list1.head
    count = 0
    while current and count < 10:  
        print(current.data, end=" -> ")
        current = current.next
        count += 1
    print("...")

    if list1.has_cycle():
        print("The list contains a cycle.")
    else:
        print("The list does not contain a cycle.")

if __name__ == "__main__":
    SingleList.has_cycle = has_cycle
    main()
