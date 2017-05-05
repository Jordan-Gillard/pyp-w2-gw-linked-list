# Hint 1

We said that a LinkedList is just an object keeping a reference to the start and end of a chain of nodes. Following the README example:

```python
n1 = Node(12)
n2 = Node(99)
n3 = Node(37)

n1.next = n2  # 12 -> 99
n2.next = n3  # 99 -> 37

my_list = LinkedList(start=n1, end=n3)  # WARNING! Not the actual interface.
```

As we also said in the README, this is all you need to implement every major list functionality. For example:

> Calculate the length of the list my_list

This can be easily solved with some simple Python logic:

```python
count = 0
auxiliar_node = my_list.start  # Important! See NOTE-1
while auxiliar_node is not None:
  count += 1
  auxiliar_node = auxiliar_node.next  # Important! See NOTE-2
print(count)
```

#### Note 1

Whenever you're working with a LinkedList and its `start` and `end` nodes, you should be **extremely careful** about how you handle those nodes. **Never lose the reference to the start or end of the list**, if you do so, you'll be completely screwed up. The moment you re-assign the references to any of those nodes, they'll be completely lost in memory. This is obviously not applied if you have to **mutate** or **modify** your list. For example, if you want to _append_ an element to the list, you'll have to change the reference of the `end` node.

#### Note 2

All the work needed to provide the functionality of a LinkedList is done by moving around the chain of nodes. In this case we're just advancing nodes one after the other until we reach the end of our node chain.
