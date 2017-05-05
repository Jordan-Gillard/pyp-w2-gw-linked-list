from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """
    
    def __init__(self, elements=None):
        self.start = None
        self.end = None
        if elements:
            for elem in elements:
                self.append(elem)
    
    def next(self):
        pass
        
    __next__ = next

    def __str__(self):
        return '[{}]'.format(', '.join([str(elem) for elem in self]))
        

    def __len__(self):
        return self.count()

    def __iter__(self):
        node = self.start
        while node:
            yield node.elem
            node = node.next
        raise StopIteration

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        for i, elem in enumerate(self):
            if i == index:
                return elem
        '''
        if index > self.count() - 1:
            raise IndexError
        i = 0
        for element in self:
            if i == index:
                return element
            i += 1
    '''
    def __add__(self, other):
        new_list = self.__class__([elem for elem in self])
        for elem in other:
            new_list.append(elem)
        return new_list
        # if other:
        #     for elem in other:
        #         self.append(elem)
        # return self

    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        return self
        
    def __ne__(self, other):
        return not self.__eq__(other)
        # return not self == other
        
        '''
        node_a = self.start
        node_b = other.start

        while True:
            if not node_a and not node_b:
                return False

            if not bool(node_a) or not bool(node_b):
                return True

            if node_a.elem != node_b.elem:
                return True

            node_a = node_a.next
            node_b = node_b.next
                '''

    def __eq__(self, other):
        node_a = self.start
        node_b = other.start

        while True:
            if not node_a and not node_b:
                return True

            if not bool(node_a) or not bool(node_b):
                return False

            if node_a.elem != node_b.elem:
                return False

            node_a = node_a.next
            node_b = node_b.next
        '''
        if self:
            node_a = self.start
        if other:
            node_b = other.start

        while self and other:
            if not node_a and not node_b:
                return True

            if not bool(node_a) or not bool(node_b):
                return False

            if node_a.elem != node_b.elem:
                return False

            node_a = node_a.next
            node_b = node_b.next
        return False
        '''
                

    def append(self, elem):
        if self.start is None:
            self.start = Node(elem)
            self.end = self.start
            return self.start
        else:
            new_node = Node(elem)
            self.end.next = new_node
            self.end = new_node
            
    def count(self):
        counter = 0
        for _ in self:
            counter += 1
        return counter

    def pop(self, index=None):
        if len(self) == 0:
            raise IndexError
        
        if index == None:
            index = self.count() - 1
            
        if index > self.count() - 1:
            raise IndexError
            
        if index == 0:
            elem = self.start.elem
            self.start = self.start.next
            return elem
        
        previous_node = None
        current_node = self.start
        
        i = 0
        for elements in self:
            if i == index:
                previous_node.next = current_node.next
                return current_node.elem
                
            previous_node = current_node
            current_node = current_node.next
            
            i += 1
                
            
                
            
        '''    
        pop_count = 0 #changed from -1
        popped_element = None
        if index == 0:
            popped_element = self.start.elem
            self.start = self.start.next
            return popped_element
        for element in self:
            pop_count += 1
            if Node(element).next == self.end:
                if index == None or index == pop_count+1:
                    popped_element = self.end.elem
                    self.end = Node(element)
                    self.end.next = None
                    return popped_element
            elif pop_count +1 == index:
                popped_element = Node(element).next.elem
                new_next = Node(element).next.next
                Node(element).next = new_next
        return popped_element
    '''
