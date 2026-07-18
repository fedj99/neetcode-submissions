from dataclasses import dataclass

@dataclass
class Node:
    val: int
    next: "Node | None" = None
    prev: "Node | None" = None

class LinkedList:
    
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def _get(self, index: int) -> Node | None:
        current = self.head
        for i in range(index):
            if current is None:
                break
            current = current.next
        return current

    
    def get(self, index: int) -> int:
        node = self._get(index)
        return node.val if node else -1
        

    def insertHead(self, val: int) -> None:
        new = Node(val=val, next=self.head, prev=None)

        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.head.prev = new
            self.head = new
        

    def insertTail(self, val: int) -> None:
        new = Node(val=val, next=None, prev=self.tail)

        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        

    def remove(self, index: int) -> bool:
        cur = self._get(index)

        if cur is None:
            return False

        if cur.prev is None:
            # cur is head
            self.head = cur.next
            if self.head is not None:
                self.head.prev = None
        else:
            cur.prev.next = cur.next
        
        if cur.next is None:
            # cur is tail
            self.tail = cur.prev
            if self.tail is not None:
                self.tail.next = None
        else:
            cur.next.prev = cur.prev

        return True
        

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current is not None:
            values.append(current.val)
            current = current.next
        return values
        
