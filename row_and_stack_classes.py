#THE STACK CLASS REPRESENTS A STACK DATA TYPE AND THE ROW CLASS REPRESENTS A ROW DATA TYPE
#THE ALGORITHM TO SORT A ROW USING TWO STACKS IS USED IN A METHOD CALLED sort_row() OF THE->
#->ROW CLASS AND IT USES TWO OBJECTS OF THE STACK CLASS TO SORT AN OBJECT OF THE ROW CLASS

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.top = -1

    def __repr__(self):
        if self.head == None:
            return '[]'

        pointer = self.head
        if pointer.next == None:
            return '[' + str(pointer.item) + ']'

        list = '['
        while pointer.next:
            list = list + str(pointer.item) + ", "
            pointer = pointer.next
            if not pointer.next:
                list = list + str(pointer.item) + ']'
        return list

    def push(self, item):
        new_node = Node(item)

        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node
            self.top = self.top + 1
            return True
        else:
            self.head = new_node
            self.top = self.top + 1
            return True
            
    def pop(self):
        if self.head:
            if self.top == 0:
                self.head = None
                self.top = self.top -1
                return True
            else:
                pointer = self.head
                while True:
                    if pointer.next.next == None:
                        pointer.next = None
                        self.top = self.top - 1
                        return True
                    pointer = pointer.next
        else:
            return False

    def check_top(self):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            return pointer.item
        else:
            return False

    def destroy(self):
        self.head = None

class Row:
    def __init__(self, maximun_size):
        self.maximun_size = maximun_size
        self.row = [None] * maximun_size
        self.length = 0

    def __repr__(self):
        if self.length == 0: #if the list is empty, returns an empty vector
            return '[]'
        else: #if the list is not empty, this formats and returns the content
            items = '['
            for i in range(0, self.length):
                if i < self.length - 1:
                    items = items + "'" + str(self.row[i]) + "'" + ", "
                else:
                    items = items + "'" + str(self.row[i]) + "'"
            items = items + ']'
            return items
    
    def insert(self, item):
        if self.length == self.maximun_size: # checking if there is free space in the row
            return False
        elif self.length == 0:
            self.row[0] = item
            self.length = self.length + 1
            return True
        else:
            self.row[self.length] = item
            self.length = self.length + 1
            return True

    def remove(self):
        if self.length > 0: # if the list is not empty, the whole row is overwritten by each item, from the first position to the end, receiving the item on its right.
            for item in range(0, self.length-1):
                self.row[item] = self.row[item+1]
            self.length = self.length - 1
            return True

    def consult(self):
        if self.length > 0:
            return self.row[0]
        else:
            return False

    def destroy(self):
        self.length = 0

    def sort_row(self):
        sorted_stack = Stack()
        secondary_stack = Stack()
        
        while self.length != 0:
                while self.consult() > sorted_stack.check_top() and sorted_stack.top != -1:
                    secondary_stack.push(sorted_stack.check_top())
                    sorted_stack.pop()
                sorted_stack.push(self.consult())
                self.remove()

                while secondary_stack.top != -1:
                    sorted_stack.push(secondary_stack.check_top())
                    secondary_stack.pop()

        while sorted_stack.top != -1:
            self.insert(sorted_stack.check_top())
            sorted_stack.pop()

        return True
