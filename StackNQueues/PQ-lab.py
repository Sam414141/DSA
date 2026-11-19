class Node:
    def __init__(self, pid, name, pr):
        self.pid = pid
        self.name = name
        self.priority = pr
        self.next = None

class pq:
    def __init__(self):
        self.front = self.rear = None
        self.count = 0

    # 1. Add Process to priority Queue
    def enqueue(self, new_node):
        if self.front == None:
            self.front = new_node
            self.count += 1
            return

        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            self.count += 1
            return

        else:
            temp = self.front
            prev = None

            while temp:
                if temp.priority > new_node.priority:
                    break
                else:
                    prev = temp
                    temp = temp.next

            prev.next = new_node
            new_node.next = temp
            self.count += 1

    # 2. Execute Process 
    def dequeue(self):
        if self.front == None:
            print("No processes to execute")
            return

        print("Executed Process:", self.front.pid, self.front.name)
        self.front = self.front.next
        self.count -= 1

    # 3. View Next Process in priority Queue
    def display_next(self):
        if self.front == None:
            print("No processes available")
            return

        print("Next Process to Execute:")
        print("Process ID:", self.front.pid)
        print("Process Name:", self.front.name)
        print("Priority:", self.front.priority)

    # 4. Display All Processes in priority Queue
    def display_all(self):
        if self.front == None:
            print("No processes available")
            return

        temp = self.front

        while temp:
            print("Process ID:", temp.pid)
            print("Process Name:", temp.name)
            print("Priority:", temp.priority)
            print()
            temp = temp.next

    # 5. Count all Processes in priority Queue
    def count_processes(self):
        print("Total Pending Processes:", self.count)


# Main program Execution
pr1 = pq()

pr1.enqueue(Node(101, "System Process", 1))
pr1.enqueue(Node(102, "Interactive Process", 2))
pr1.enqueue(Node(103, "Background Process", 3))
pr1.enqueue(Node(104, "Low Priority Process", 4))
pr1.enqueue(Node(105, "Interactive Process 2", 2))

# displaying all processes
pr1.display_all()

# display next process
print("\nNext Process:")
pr1.display_next()

# Executing Processes
print("\nExecuting Process:")
pr1.dequeue()

print("\nRemaining Processes:")
pr1.display_all()

pr1.count_processes()