# split_example.py
from SingleLL import SingleList

def split(self):
    list1 = SingleList()
    list2 = SingleList()

    current = self.head
    toggle = True

    while current:
        if toggle:
            list1.add_at_tail(current.data)
        else:
            list2.add_at_tail(current.data)
        
        toggle = not toggle
        current = current.next

    return list1, list2

SingleList.split = split

def main():
    list1 = SingleList()
    list1.add_at_tail(10)
    list1.add_at_tail(20)
    list1.add_at_tail(30)
    list1.add_at_tail(40)
    list1.add_at_tail(50)
    
    print("Original list:")
    current = list1.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    list1a, list1b = list1.split()

    print("First split list:")
    current = list1a.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("Second split list:")
    current = list1b.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    main()
