#todo app

manager = []

def add_task(id,task,priority,completed=False):
    manager.append({'id': id,'title':task, 'priority':priority, 'completed':completed})
    print("Task added Successfully!")

def view_task():
    print(f"{'Id':>5} {'Title':>15} {'Priority':>15} {'Completed':>15}")
    for task in manager:
        print(f"{task['id']:>5} {task['title']:>15} {task['priority']:>15} {task['completed']:>15}")

def mark_task_as_done():
    pass

def delete_task():
    view_task()
    task_delete = input("Enter the task you want to delete.")

def filter_task_by_priority():
    pass
id_count = 0
while True:
    print('''
    
    1. Add Task
    2. View Tasks
    3. Mark Task as Done
    4. Delete Task
    5. Filter Tasks by Priority
    6. Exit\n\n
    ''')
    choice = input('Enter the choice: ')
    
    match choice:
        case '1':
            id_count += 1
            task = input("Enter the task: ")
            priority = input("Enter the task priority(high/medium/low): ")
            if task != '' or task != " ":
                add_task(id_count, task, priority)
        
        case '2':
            view_task()

        case '3':
            view_task()
            task_done = int(input("Enter the task number you want to mark done."))
            for task in manager:
                if task['id'] == task_done:
                    task['completed'] = not task['completed'] 
                       
                    print(task['id'], task['title'])
                    # else:
                    #     task['completed'] = 0

                    print(task)
        case '4':
            pass

        case '5':
            pass

        case '6':
            break