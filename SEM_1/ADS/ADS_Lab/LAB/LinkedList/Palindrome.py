from SingleLL import SingleList

def is_palindrome(self):
    if self.is_empty():
        return True

    slow = self.head
    fast = self.head
    prev_of_slow = None
    
    while fast and fast.next:
        fast = fast.next.next
        prev_of_slow = slow
        slow = slow.next

    second_half = None
    if fast: 
        second_half = slow.next
    else:
        second_half = slow

    prev_of_slow.next = None
    second_half = reverse(second_half)

    first_half = self.head
    is_palindrome = True
    while second_half:
        if first_half.data != second_half.data:
            is_palindrome = False
            break
        first_half = first_half.next
        second_half = second_half.next
    
    return is_palindrome

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def main():
    list1 = SingleList()
    list1.add_at_tail(1)
    list1.add_at_tail(2)
    list1.add_at_tail(3)
    list1.add_at_tail(2)
    #list1.add_at_tail(1)
    
    print("List:")
    current = list1.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    
    if list1.is_palindrome():
        print("The list is a palindrome.")
    else:
        print("The list is not a palindrome.")

if __name__ == "__main__":
    SingleList.is_palindrome = is_palindrome
    main()
