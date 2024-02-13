class Worker:
    department = "Engineering"

    def __init__(self, name):
        self.name = name

    def change_name(self, name):
        self.name = name

worker1 = Worker("James")
worker1.change_name("Peter")
Worker.department = "IT"
worker2 = Worker("David")

# print(worker1.name)
# print(worker1.department)
# print(worker2.name)
# print(worker2.department)

from tabulate import tabulate

workers = [worker1, worker2]
headers = ["", "Employee", "Department"]
worker_data = [[i, worker.name, worker.department] for i, worker in enumerate(workers, 1)]
print(tabulate(worker_data, headers=headers))


def print_name(name):
    print(name)
    return name

name = print_name("Armand")
print(name)