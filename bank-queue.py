import time
import heapq

# Node for Linked List Queue
class CustomerNode:
    def __init__(self, name, service_time, priority=0):
        self.name = name
        self.service_time = service_time  # time needed to serve the customer
        self.priority = priority          # 0 = normal, 1 = VIP
        self.next = None

# Bank Queue using Linked List
class BankQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, name, service_time, priority=0):
        new_customer = CustomerNode(name, service_time, priority)
        if self.is_empty():
            self.front = self.rear = new_customer
        else:
            self.rear.next = new_customer
            self.rear = new_customer

    def dequeue(self):
        if self.is_empty():
            return None
        removed_customer = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_customer

    def display(self):
        if self.is_empty():
            print("Queue is empty.\n")
            return
        current = self.front
        print("Current Queue:")
        while current:
            tag = " (VIP)" if current.priority == 1 else ""
            print(f" - {current.name}{tag}, Service Time: {current.service_time}s")
            current = current.next
        print()

# Priority Queue for VIP handling
class PriorityBankQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, name, service_time, priority=0):
        # Negative priority ensures VIPs (1) are served before normals (0)
        heapq.heappush(self.queue, (-priority, time.time(), name, service_time))

    def dequeue(self):
        if not self.queue:
            return None
        _, _, name, service_time = heapq.heappop(self.queue)
        return CustomerNode(name, service_time)

    def display(self):
        if not self.queue:
            print("Queue is empty.\n")
            return
        print("Current Queue:")
        for item in sorted(self.queue, reverse=True):
            _, _, name, service_time = item
            print(f" - {name}, Service Time: {service_time}s")
        print()

# Simulation
def simulate_bank():
    print("\n🏦 Welcome to Bank Queue Simulation 🏦\n")
    queue = PriorityBankQueue()

    # Add sample customers
    queue.enqueue("Alice", 3)
    queue.enqueue("Bob", 5)
    queue.enqueue("Charlie", 2, priority=1)  # VIP
    queue.enqueue("Diana", 4)

    queue.display()

    total_wait_time = 0
    total_customers = len(queue.queue)

    print("Starting service...\n")

    while queue.queue:
        customer = queue.dequeue()
        print(f"Now serving: {customer.name} {'(VIP)' if customer.priority == 1 else ''}")
        print(f"Service time: {customer.service_time} seconds")
        time.sleep(0.5)  # Simulate service delay (reduce for faster demo)
        total_wait_time += customer.service_time
        print(f"{customer.name} has been served.\n")

    avg_wait = total_wait_time / total_customers if total_customers else 0
    print(f"✅ All customers served.")
    print(f"📊 Total customers: {total_customers}")
    print(f"⏱️  Total service time: {total_wait_time} seconds")
    print(f"📈 Average waiting time: {avg_wait:.2f} seconds\n")

# Run simulation
if __name__ == "__main__":
    simulate_bank()
