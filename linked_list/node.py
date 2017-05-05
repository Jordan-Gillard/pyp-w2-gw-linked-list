class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        return '{}'.format(self.__repr__())

    def __eq__(self, other):
        return lambda x, y: x==y, self, other
        #return self.elem == other.elem and self.next == other.next
            

    def __repr__(self):
        if self.next:
            return 'Node({}) > Node({})'.format(self.elem, self.next.elem)
        return 'Node({}) > /'.format(self.elem)
