import Task
import unittest

class Task(unittest.TestCase):
    def test_init(self):
        my_task = Task("Task 1", "5/8")
        self.assertEqual(self.title, "Task 1")
        self.assertEqual(self.due_date, "5/8")

def main():
    unittest.main()

main()

tasks = {"synthesis 03", "project 09","dry cleaning pickup"}

tasks.add("laundry")

tasks.remove("dry cleaning pickup")

print(tasks) # Output: {"synthesis 03", "Project 09", "laundry"}

for key in tasks:
    value = tasks[key]
    print(key + ":", value)

    