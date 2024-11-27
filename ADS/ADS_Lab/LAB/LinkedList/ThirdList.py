from SingleLL import SingleList

def main():
    def to_set(single_list):
        elements = set()
        cur = single_list.head
        while cur:
            elements.add(cur.data)
            cur = cur.next
        return elements

    list1 = SingleList()
    list2 = SingleList()

    list1.add_at_tail(1)
    list1.add_at_tail(2)
    list1.add_at_tail(3)
    list1.add_at_tail(4)
    
    list2.add_at_tail(3)
    list2.add_at_tail(4)
    list2.add_at_tail(5)
    list2.add_at_tail(6)
    
    elements_set_1 = to_set(list1)  
    common_list = SingleList()      

    cur = list2.head
    while cur:
        if cur.data in elements_set_1:
            common_list.add_at_tail(cur.data)
        cur = cur.next

    print("Common elements in both lists:")
    cur = common_list.head
    while cur:
        print(cur.data)
        cur = cur.next

if __name__ == "__main__":
    main()
