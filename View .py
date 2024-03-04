def view_pending_tasks(tasks):
    pending_tasks = [task for task in tasks if "(Completed)" not in task]
    return pending_tasks

# Example usage:
tasks = ["Task 1", "Task 2 (Completed)", "Task 3"]
pending_tasks = view_pending_tasks(tasks)
print("Pending tasks:", pending_tasks)
