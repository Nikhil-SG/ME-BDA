class SingleList:
    class Node:
        def __init__(self, ele):
            self.data = ele
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def get_first(self):
        if not self.is_empty():
            return self.head.data
        else:
            return None

    def get_last(self):
        if not self.is_empty():
            return self.tail.data
        else:
            return None

    def add_at_head(self, ele):
        new_node = self.Node(ele)
        if not self.is_empty():
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1

    def add_at_tail(self, ele):
        new_node = self.Node(ele)
        if not self.is_empty():
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1

    def del_at_head(self):
        if not self.is_empty():
            ele = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.count -= 1
            return ele
        else:
            return None

    def del_at_tail(self):
        if not self.is_empty():
            ele = self.tail.data
            if self.count == 1:
                self.head = self.tail = None
            else:
                cur = self.head
                while cur.next != self.tail:
                    cur = cur.next
                cur.next = None
                self.tail = cur
            self.count -= 1
            return ele
        else:
            return None

    def is_member(self, key):
        cur = self.head
        while cur:
            if cur.data == key:
                return True
            cur = cur.next
        return False

    def add_after_value(self, key, ele):
        cur = self.head
        while cur:
            if cur.data == key:
                new_node = self.Node(ele)
                new_node.next = cur.next
                cur.next = new_node
                if cur == self.tail:
                    self.tail = new_node
                self.count += 1
                return True
            cur = cur.next
        return False

    def del_after_value(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur.next:
                ele = cur.next.data
                cur.next = cur.next.next
                if cur.next is None:
                    self.tail = cur
                self.count -= 1
                return ele
            cur = cur.next
        return None
