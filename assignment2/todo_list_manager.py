#todo app

manager = []

def add_task(id,task,priority,completed=False):
    manager.append({'id': id,'title':task, 'priority':priority, 'completed':completed})
    print("Task added Successfully!")

def view_task(user_priority = 'default'):
    if not manager:
        print("Please add tasks to view")
        return
    priority_order = {'high':1, 'medium': 2, 'low':3}

    print(f"{'Id':>5} {'Title':>15} {'Priority':>15} {'Completed':>15}")
    if user_priority != 'default':
        filtered_list = list(filter(lambda x:x['priority'] == user_priority, manager))
    else:
        filtered_list = manager
    for task in filtered_list:
        print(f"{task['id']:>5} {task['title']:>15} {task['priority']:>15} {task['completed']:>15}")
# def view_task(user_priority='default'):
    if not manager:
        print("Please add tasks to view")
        return
    
    priority_order = {'high': 1, 'medium': 2, 'low': 3}

    if user_priority == 'default':
        task_list = manager                      # show all, original order
    elif user_priority == 'sort':
        task_list = sorted(manager, key=lambda x: priority_order[x['priority']])  # show all, high first
    else:
        task_list = [t for t in manager if t['priority'] == user_priority]        # show only matching
        if not task_list:
            print(f"No tasks with '{user_priority}' priority.")
            return

    print(f"\n{'Id':>5} {'Title':>15} {'Priority':>15} {'Completed':>15}")
    for task in task_list:
        print(f"{task['id']:>5} {task['title']:>15} {task['priority']:>15} {task['completed']:>15}")   

def mark_task_as_done(task_mark):
    
    for task in manager:
        if task['id'] == task_mark:
            task['completed'] = not task['completed'] 
            print(task['id'], task['title'])
            print('Task checked to mark done.')
            return
    print("Task not found")

def delete_task(task_delete):
    for task in manager:
        if task['id'] == task_delete:
            manager.remove(task)
            print("Task removed Successfully!!")
            return
    print("Task not found for deleting.")    

# def filter_task_by_priority():
#     pass


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
            if task != '' and task != " ":
                add_task(id_count, task, priority)
        
        case '2':
            view_task()

        case '3':
            view_task()
            task_mark = int(input("Enter the task number you want to mark done."))
            mark_task_as_done(task_mark)
            
        case '4':
            view_task()
            task_delete = int(input("Enter the task you want to delete."))
            delete_task(task_delete)


        case '5':
            view_task()
            priority = input("Enter the priority you want to sort with(high/low/medium): ")
            view_task(priority)

        case '6':
            break

