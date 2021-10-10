"""
This is a Python implementation of the how to insert commas
between a given sequence if string digit

For doctests run following command:
python -m doctest -v insert_commas.py
or
python3 -m doctest -v insert_commas.py

For manual testing run:
python insert_commas.py
"""


class StringBuilder(object):
    def __init__(self, val="") -> None:
        self.store = [val]

    def __iadd__(self, value):
        self.store.append(value)
        return self

    def __str__(self) -> str:
        return "".join(self.store)


class Node:
    def __init__(self, info: str) -> None:
        self.info = info
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, x: str):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            node = Node(x)
            self.tail.next = node
            self.tail = node

    def pop(self):
        node = self.head
        self.head = self.head.next
        node.next = None

    def peek(self) -> str:
        return self.head.info

    def empty(self) -> bool:
        return True if self.head is None else False

    def __str__(self) -> str:
        ret = StringBuilder()
        current = self.head
        while current:
            ret += current.info
            current = current.next
        return str(ret)


def build_string_queue(string: str) -> Queue:
    ret = Queue()
    i = 0
    for idx, ch in enumerate(reversed(string)):
        ret.push(ch)
        i += 1
        if i % 3 == 0:
            if len(string) - 1 - idx == 0:
                continue
            ret.push(",")
            i = 0
    return ret


def extract_string_from_queue(queue: Queue) -> str:
    ret = StringBuilder()
    while not queue.empty():
        ret += queue.peek()
        queue.pop()
    return str(ret)[::-1]


def insert_commas(string: str) -> str:
    """Implementation of the levenshtein distance in Python.
    :param string: the string representation of a number.
    :return: the string representation of the number delimited by commas.
    Examples:
    >>> insert_commas("1")
    '1'
    >>> insert_commas("100")
    '100'
    >>> insert_commas("100000")
    '100,000'
    >>> insert_commas("10000000")
    '10,000,000'
    >>> insert_commas("100000000000")
    '100,000,000,000'
    >>> insert_commas("634829301184902")
    '634,829,301,184,902'
    """
    q = build_string_queue(string)
    return extract_string_from_queue(q)


if __name__ == "__main__":
    print(insert_commas("1"))
    print(insert_commas("100"))
    print(insert_commas("1000"))
    print(insert_commas("100000"))
    print(insert_commas("10000000"))
    print(insert_commas("634829301184902"))
