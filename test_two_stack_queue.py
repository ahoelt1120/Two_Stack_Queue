"""
Name: Amanda Hoelting
Title: Test Suite for Two Stack Queue Project
"""
import two_stack_queue
import unittest

class T0_TestingQueue(unittest.TestCase):

    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        s = two_stack_queue.Queue()
        s.enqueue("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")

    def test_dequeue_empty(self):
        # testing if exception is raised if dequeue is used on empty queue
        print("\n")
        s = two_stack_queue.Queue()
        with self.assertRaises(Exception):
            s.dequeue()
        print("\n")

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = two_stack_queue.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")

class T1_TestingStack(unittest.TestCase):

    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        s = two_stack_queue.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")

    def test_push(self):
        #testing push functionality
        print("\n")
        s = two_stack_queue.Stack()
        s.push("1")
        s.push("2")
        s.push("3")
        s.push("4")
        print("return numbers in opposite order they were pushed")
        self.assertEqual(s.__str__(), "[4, 3, 2, 1]")
        print("\n")

    def test_pop_once(self):
        #testing pop operation once
        print("\n")
        s = two_stack_queue.Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        value = s.pop()
        print("return numbers in opposite order they were pushed")
        self.assertEqual(value, 4)
        self.assertEqual(s.__str__(), "[3, 2, 1]")
        print("\n")

    def test_pop_more(self):
        #testing pop operation three times
        print("\n")
        s = two_stack_queue.Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.pop()
        s.pop()
        s.pop()
        print("return numbers in opposite order they were pushed")
        self.assertEqual(s.__str__(), "[1]")
        print("\n")

    def test_pop_empty(self):
        # testing if exception is raised if pop is used on empty stack
        print("\n")
        s = two_stack_queue.Stack()
        with self.assertRaises(Exception):
            s.pop()
        print("\n")



class T2_TestingPalindrome(unittest.TestCase):


    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = two_stack_queue.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")

    def test_palindrome_string(self):
        # testing with palindrome string
        print("\n")
        string = "TaCo Cat"
        p = two_stack_queue.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")

class T2_TestingTwoStackQueue(unittest.TestCase):

    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        s = two_stack_queue.TwoStackQueue()
        s.enqueue("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")

    def test_dequeue_empty(self):
        # testing if exception is raised if dequeue is used on empty queue
        print("\n")
        s = two_stack_queue.TwoStackQueue()
        with self.assertRaises(Exception):
            s.dequeue()
        print("\n")

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = two_stack_queue.TwoStackQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")


    def test_basic_enqueue_dequeue(self):
        # testing the basic enqueue operation
        print("\n")
        q = two_stack_queue.TwoStackQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.dequeue()
        q.enqueue(3)
        q.enqueue(4)
        q.dequeue()
        q.enqueue(5)
        q.enqueue(6)
        q.dequeue()
        q.dequeue()

        self.assertEqual(q.__str__(), '[5, 6]')
        print("\n")

    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = two_stack_queue.isPalindromeEC(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")

    def test_palindrome_string(self):
        # testing with palindrome string
        print("\n")
        string = "TaCo Cat"
        p = two_stack_queue.isPalindromeEC(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")


if __name__ == '__main__':
    unittest.main()
