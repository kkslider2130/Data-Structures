"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        newNode = ListNode(value)
        if(self.head):
            current = self.head
            newNode.next = current
            self.head = newNode
            self.length += 1
        else:
            self.length += 1
            self.head = newNode
            self.tail = newNode
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if(self.head):
            current = self.head
            if self.head == self.tail:
                self.tail = None
            if current.next:
                after = current.next
                after.previous = None
            self.head = current.next
            self.length -= 1
            return current.value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        newNode = ListNode(value)
        if(self.head):
            current = self.tail
            while(current.next):
                current = current.next
            newNode.prev = current
            current.next = newNode
            self.tail = newNode
            self.length += 1
        else:
            self.length += 1
            self.head = newNode
            self.tail = newNode
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        current_tail = self.tail
        if current_tail.prev:
            self.tail = current_tail.prev
            new_tail = current_tail.prev
            new_tail.value = None
        else:
            self.tail = None
            self.head = None
        self.length -= 1
        return current_tail.value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        current = self.head
        while current != node:
            current = current.next
        if current.prev:
            before = current.prev
            before.next = current.next
        if current.next:
            after = current.next
            after.prev = current.prev
        old_head = self.head
        old_head.prev = current
        current.next = old_head
        current.prev = None
        self.head = current
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        current = self.head
        while current != node:
            current = current.next
        if current.prev:
            before = current.prev
            before.next = current.next
            if node == self.tail:
                self.tail = before
        if current.next:
            after = current.next
            after.prev = current.prev
            if node == self.head:
                self.head = after
        old_tail = self.tail
        old_tail.next = current
        current.prev = old_tail
        current.next = None
        self.tail = current
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        current = self.head
        while current != node:
            current = current.next
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        if current.prev:
            before = current.prev
            before.next = current.next
            if node == self.tail:
                self.tail = before
        if current.next:
            after = current.next
            after.prev = current.prev
            if node == self.head:
                self.head = after
        self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        current = self.head
        i = 0
        while current:
            if current.value > i:
                i = current.value
            current = current.next
        return i
