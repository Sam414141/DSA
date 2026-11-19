class node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    # 1. Add Process
    def enqueue(self, new_node):
        if self.front == None:
            self.front = new_node
            return

        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        else:
            temp = self.front

            while temp.next != None and temp.next.priority <= new_node.priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

    # 2. Execute Process
    def dequeue(self):
        if self.front:
            temp = self.front
            print("Executed Process:", temp.pid, temp.name)
            self.front = self.front.next
            temp.next = None
        else:
            print("Queue is empty")

    # 3. View Next Process
    def display_next(self):
        if self.front:
            print("Next Process:", self.front.pid, self.front.name, self.front.priority)
        else:
            print("Queue is empty")

    # 4. Display All Processes
    def display(self):
        temp = self.front

        if temp == None:
            print("Queue is empty")
            return

        while temp:
            print(temp.pid, temp.name, temp.priority)
            temp = temp.next

    # 5. Count Processes
    def count(self):
        temp = self.front
        c = 0

        while temp:
            c = c + 1
            temp = temp.next

        print("Total Processes:", c)


# Create Priority Queue
pq = PriorityQueue()

pq.enqueue(node(101, "System Process", 1))
pq.enqueue(node(102, "Interactive Process", 2))
pq.enqueue(node(103, "Background Process", 3))
pq.enqueue(node(104, "Low-Priority Process", 4))

print("All Processes:")
pq.display()

print("\nNext Process:")
pq.display_next()

print("\nTotal Processes:")
pq.count()

print("\nExecuting Process:")
pq.dequeue()

print("\nRemaining Processes:")
pq.display()

print("\nTotal Processes:")
pq.count()