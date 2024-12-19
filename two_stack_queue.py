"""
Name: Amanda Hoelting
Title: Two Stack Queue
"""
class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.

        Parameters
        ----------
        data: int or float
            An individual character or number to be stored in self.__data
        '''
        self.__data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.

        Parameters
        ----------
        next_node: Node object
            A pointer to a Node that will be set to self.__next_node
        '''
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object):
    """
    A class to represent a queue.

    ...

    Attributes
    ----------
    head : Node object
        A node that was added to the queue first
    next_node : Node object
        A node that was added to the queue last

    Methods
    -------
    __str__():
        Loops through the queue and prints each Node's data
    enqueue(data):
        Adds a node to tail of the queue and updates the NextNode of the previous tail
    dequeue(next_node):
        Removes the tail node from the queue and returns its data
    isEmpty():
        Returns true if queue is empty
    """
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        if self.isEmpty():
            return '[]'
        node_str = '['
        current = self.__head
        while current.getNext() != None:
            node_str += str(current.getData()) + ', '
            current = current.getNext()
        node_str += str(current.getData()) + ']'
        return node_str

    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.

        Parameters
        ----------
        newData: Int or float
            An individual character or number to be stored in a node
        '''
        # Hint: Think about what's different for the first node added to the Queue
        new_node = Node()
        new_node.setData(newData)
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.setNext(new_node)
            self.__tail = new_node


    def dequeue(self):
        '''Return the head of the Queue
        Update head.'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        if self.isEmpty():
            raise AttributeError
        elif self.__head.getNext() == None:
            temp_node = Node()
            temp_node.setData(self.__head.getData())
            self.__head = None
            return temp_node.getData()
        else:
            data = self.__head.getData()
            self.__head = self.__head.getNext()
            return data



    def isEmpty(self):
        '''Check if the Queue is empty.'''
        return self.__head == None


class Stack(object):
    """
    A class to represent a stack.

    ...

    Attributes
    ----------
    top : Node object
        A node that was added to the queue first

    Methods
    -------
    __str__():
        Loops through the stack and prints each Node's data
    push(data):
        Pushes a node on the top of the stack and updates the NextNode of the previous top
    pop():
        Pops the top node off the stack and returns its data
    isEmpty():
        Returns true if stack is empty
    """
    def __init__(self):
        ''' We want to initialize our Stack to be empty.
        (ie) Set top as null'''

        self.__top = None

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        if self.isEmpty():
            return '[]'
        else:
            data_str = '['
            current = self.__top
            while current.getNext() != None:
                data_str += str(current.getData()) + ', '
                current = current.getNext()
            data_str += str(current.getData()) + ']'
            return data_str

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top

        Parameters
        ----------
        newData: Int or float
            An individual character or number to be stored in a node
        '''
        new_node = Node()
        new_node.setData(newData)
        if self.__top != None:
            new_node.setNext(self.__top)
            self.__top = new_node
        else:
            self.__top = new_node



    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        if self.__top == None:
            raise AttributeError
        temp_node = Node()
        temp_node.setData(self.__top.getData())
        self.__top = self.__top.getNext()
        return temp_node.getData()

    def isEmpty(self):
        '''Check if the Stack is empty.'''
        return self.__top == None


class TwoStackQueue(object):
    """
    A class to represent a two stack queue.

    ...

    Attributes
    ----------
    head : Stack object
        A stack that is at the head of queue
    next_node : Stack object
        A stack that is at the tail of queue

    Methods
    -------
    __str__():
        Loops through the queue's tail stack and prints each Node's data
    enqueue(data):
        Adds a node to stack at the head of the queue
    dequeue():
        Pops the node from the tail stack and returns its data
    isEmpty():
        Returns true if the queue is empty
    """
    def __init__(self):
        self.__head = Stack()
        self.__tail = Stack()

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        if self.isEmpty():
            return '[]'
        while not self.__head.isEmpty():
            self.__tail.push(self.__head.pop())
        string = self.__tail.__str__()
        return string



    def enqueue(self, newData):
        '''Pushes a new node with the new data onto the head stack

        Parameters
        ----------
        newData: Int or float
            An individual character or number to be stored in a node
        '''
        self.__head.push(newData)


    def dequeue(self):
        '''Pops data off of the tail stack
        or pops data from the head stack and pushes it onto the tail stack'''
        if self.__tail.isEmpty:
            if self.isEmpty():
                raise AttributeError
            else:
                while not self.__head.isEmpty():
                    self.__tail.push(self.__head.pop())
                data = self.__tail.pop()
                while not self.__tail.isEmpty():
                    self.__head.push(self.__tail.pop())
                return data
        else:
            return self.__tail.pop()

    def isEmpty(self):
        '''Check if the Queue is empty.'''
        return self.__head.isEmpty() and self.__tail.isEmpty()



def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    myStack = Stack()
    myQueue = Queue()

    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()

    for c in s:
        if c != " ":
            c = c.lower()
            myStack.push(c)
            myQueue.enqueue(c)

    return str(myStack) == str(myQueue)

def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''
    myStack = Stack()
    myQueue = TwoStackQueue()
    # Return appropriate value
    for c in s:
        if c != " ":
            c = c.lower()
            myStack.push(c)
            myQueue.enqueue(c)
    return str(myStack) == str(myQueue)
