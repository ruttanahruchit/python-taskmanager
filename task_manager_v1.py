# Exercise 1: Modify and run
#tasks = []
tasks = ["Learn Python", "Build a Task Manager"]
print("=== Task Manager ===")
print("\nYour current tasks:")
print(tasks[0])
print(tasks[1])
print("Task count:", len(tasks))

#print("Your task list is empty. Let's add some tasks.\n")
# first_task = input("Enter your first task: ")
# tasks.append(first_task)
# second_task = input("Enter your second task: ")
# tasks.append(second_task)
new_task = input("\nEnter a new task: ")
tasks.append(new_task)
print("Added: " + new_task)

print("\nYour new tasks:")
print(tasks[0])
print(tasks[1])
print(tasks[2])
print("New task count:", len(tasks))
