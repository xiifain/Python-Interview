import pickle
import uuid
from prettytable import PrettyTable

# +------------- BEFORE RUNNING THIS FILE ------------------
# 1. Activate the virtual environment by typing this command in the terminal (source venv/bin/activate)
# 2. Run the file, it should work now
# 3. If the package is still not detected, run "pip install -r requirements.txt" command.


class Task:
    def __init__(self, name, task_entries = []):
        self.name = name
        self.task_entries = task_entries

    @classmethod
    def get_tasks(cls):
        try:
            with open('task_objects.dat', 'rb+') as f:
                try:
                    unpickler = pickle.Unpickler(f)
                    return unpickler.load()
                except:
                    return []
        except:
            return []

    # def get_task_entries(self, id):

class TaskEntries:
    def __init__(self, name, id , status=False):
        self.id = id
        self.name = name
        self.status = status




while True:

    tasks_list = Task.get_tasks()
    table = PrettyTable(['ID', 'TASK NAME', 'ENTRIES', 'ENTRY ID', 'STATUS'])
    table.align = 'r'
    
    for k,i in enumerate(tasks_list):
        table.add_row([k , i.name, "", "", ""])
        for no , entry in enumerate(i.task_entries):
            table.add_row([ '', '' , entry.name, no, entry.status])
    print(table)

    home_choice = str(input("Choose Options : \n 1. Add new Task \n 2. Add entry to a task \n 3. Change the status of an entry \n 4. Delete Task \n 5. Exit the shell \n Choose your options : "))

    if home_choice == '1':
        input_task = str(input("Enter New Task Name : "))
        if input_task == '' or input_task == ' ':
            print(' ---------- FORMAT ERROR, THE TASK NAME CANNOT BE BLANK --------- ')

        else :
            new_task = Task(input_task)
            tasks_list.append(new_task)

    elif home_choice == '2':
        input_entry = str(input("ENTER NEW ENTRY DATA : "))
        input_task_id = int(input("ENTER TASK ID : "))
        if input_task_id > len(tasks_list):
            print(" ------- TASK ID DOESN\'T EXISTS ---------")
        else:
            new_entry = TaskEntries(input_entry, input_task_id, False)
            tasks_list[input_task_id].task_entries.append(new_entry)

    elif home_choice == '3':
        task_id = int(input("ENTRY TASK FOR CHANGING STATUS : "))
        change_status_id = int(input("ENTER ENTRY ID FOR CHANGING STATUS : "))
        if ((task_id < len(tasks_list)) and (change_status_id < len(tasks_list[task_id].task_entries))):
            tasks_list[task_id].task_entries[change_status_id].status = True
        else:
            print(" --------------- ERROR IN ARGUMENTS ---------------")
    elif home_choice == '4':
        task_id = int(input("ENTRY TASK FOR REMOVING : "))
        if task_id < len(tasks_list):
            tasks_list.pop(task_id)
        else:
            print(" ---------- ERROR REMOVING -------------")

    elif home_choice == '5':
        break;
    else:
        print(" INPUT ERROR, PLEASE CHOOSE AGAIN  ")
    
    try:
        with open('task_objects.dat', 'wb') as objects_file:
            pickle.dump(tasks_list, objects_file)
            objects_file.flush()
            objects_file.close()
    except:
        print(" ------------ ERRORS OCCURED ---------------")



