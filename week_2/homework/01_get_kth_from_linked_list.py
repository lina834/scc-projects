class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # self.before = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        # self.tail = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
        # self.tail = cur.next


    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        pointer_ahead = self.head
        pointer_behind = self.head

        for i in range(k):
            pointer_ahead = pointer_ahead.next

        while pointer_ahead is not None:
            pointer_behind = pointer_behind.next
            pointer_ahead = pointer_ahead.next

        return pointer_behind


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!