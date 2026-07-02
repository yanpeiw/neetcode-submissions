class listNode:
    
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
    #creating a dummy node
        self.head = listNode(0)
        self.tail = listNode(0)
    #setting the dummy head node's next pointer to the tail and vice versa
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next 
        while cur and index > 0:
            cur = cur.next
            index -= 1 
        if cur and cur != self.tail and index == 0:
            return cur.val
        return -1
    def addAtHead(self, val: int) -> None:
        node = listNode(val)
        next = self.head.next
        prev = self.head
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev


    def addAtTail(self, val: int) -> None:
        
        node = listNode(val)
        prev = self.tail.prev
        next = self.tail

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

        
    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node = listNode(val)
            prev = cur.prev
            next = cur

            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0 and cur != self.tail:
            next = cur.next
            prev = cur.prev
            next.prev = prev
            prev.next = next 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)