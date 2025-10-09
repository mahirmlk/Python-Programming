"""
Multithreading runs multiple tasks at the same time.
Good for I/O tasks (file reading, network requests, etc.)
"""

import threading
import time

# Simple thread example
def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()  # Wait for thread to finish

# Multiple threads
def task(name):
    for i in range(3):
        print(f"{name}: {i}")
        time.sleep(0.5)

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads finished")

# Function with return value using list
results = []

def calculate(n):
    result = n * n
    results.append(result)
    print(f"Calculated: {n}^2 = {result}")

threads = []
for num in [2, 3, 4, 5]:
    t = threading.Thread(target=calculate, args=(num,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Results: {results}")

# Download simulation
def download_file(filename):
    print(f"Starting download: {filename}")
    time.sleep(2)  # Simulate download time
    print(f"Finished: {filename}")

files = ["file1.txt", "file2.txt", "file3.txt"]
threads = []

for file in files:
    t = threading.Thread(target=download_file, args=(file,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All downloads complete")

# Thread with class
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    
    def run(self):
        print(f"{self.name} starting")
        time.sleep(1)
        print(f"{self.name} finished")

t1 = MyThread("Worker-1")
t2 = MyThread("Worker-2")

t1.start()
t2.start()

t1.join()
t2.join()

# Check active threads
def worker():
    time.sleep(2)

t = threading.Thread(target=worker)
t.start()
print(f"Active threads: {threading.active_count()}")
t.join()