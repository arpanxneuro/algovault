class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def printLinkedList(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next

if __name__ == '__main__':
    llist_count = int(input().strip())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input().strip())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
