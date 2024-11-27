from SingleLL import SingleList

def main():
    sll = SingleList()
    print("Adding elements to the list:")
    sll.add_at_head(10)    
    sll.add_at_tail(20)     
    sll.add_at_tail(30)    
    sll.add_at_head(5)     

    print(f"First element: {sll.get_first()}") 
    print(f"Last element: {sll.get_last()}")  
    
    print(f"Size of the list: {sll.size()}")   
    
    print("Adding element after value 10:")
    sll.add_after_value(10, 15) 
    print(f"List after adding 15 after 10: {[node.data for node in iter_list(sll)]}")

    print("Deleting element after value 15:")
    sll.del_after_value(15)     
    print(f"List after deleting element after 15: {[node.data for node in iter_list(sll)]}")

    print("Deleting element at head:")
    print(sll.del_at_head())    
    print(f"List after deleting head: {[node.data for node in iter_list(sll)]}")  
    
    print("Deleting element at tail:")
    print(sll.del_at_tail())   
    print(f"List after deleting tail: {[node.data for node in iter_list(sll)]}")  

    print(f"Is 10 in the list? {'Yes' if sll.is_member(10) else 'No'}")  
    print(f"Is 30 in the list? {'Yes' if sll.is_member(30) else 'No'}")

def iter_list(sll):
    current = sll.head
    while current:
        yield current
        current = current.next

if __name__ == "__main__":
    main()
