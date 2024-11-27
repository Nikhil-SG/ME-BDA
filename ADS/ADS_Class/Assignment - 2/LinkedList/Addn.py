from SingleLL import SingleList

def get_sum_of_last_n_nodes(self, n):
    if n <= 0 or self.is_empty() or n > self.size():
        return 0

    front_pointer = self.head
    back_pointer = self.head

    for _ in range(n):
        if front_pointer is None:
            return 0
        front_pointer = front_pointer.next

    while front_pointer:
        front_pointer = front_pointer.next
        back_pointer = back_pointer.next

    sum_last_n_nodes = 0
    while back_pointer:
        sum_last_n_nodes += back_pointer.data
        back_pointer = back_pointer.next

    return sum_last_n_nodes

def main():
    list1 = SingleList()
    list1.add_at_tail(10)
    list1.add_at_tail(20)
    list1.add_at_tail(30)
    list1.add_at_tail(40)
    list1.add_at_tail(50)
    
    n = int(input("Enter the number of last nodes to sum: "))

    sum_last_n = list1.get_sum_of_last_n_nodes(n)

    print(f"Sum of the last {n} nodes: {sum_last_n}")

if __name__ == "__main__":
    SingleList.get_sum_of_last_n_nodes = get_sum_of_last_n_nodes
    main()
