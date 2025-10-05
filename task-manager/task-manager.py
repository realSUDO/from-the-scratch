import json
import os
from pathlib import Path

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_DIR = f"{CURRENT_DIR}/tasks.txt"

def clear_screen() : 
    os.system("clear")

def print_warning(msg):
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    print(f"{YELLOW}{msg}{RESET}")


def load_task_category():
    task_categories = {"1": "Real-World Growth", "2": "Gym", "3": "College"}
    for x, y in task_categories.items():
        print(f"{x} : {y}")
    return task_categories


def add_task(tasks):
    clear_screen()
    categories = load_task_category()
    category_index = input("Enter task category : ").strip()
    description = input("Enter task description : ").strip()
    tasks.append(
        {"task_category": categories.get(category_index), "task_desc": description}
    )
    save_task(tasks)
    print("Task added successfully ✅")
    input("Press Enter to continue")
    clear_screen()
    

def save_task(tasks):
    with open(TASK_DIR, "w") as f:
        json.dump(tasks, f)


def update_task(tasks):
    clear_screen()
    list_task(tasks)
    if not tasks : 
        input("There are no tasks to update. Press ENTER to continue")
        return
    try : 
        index = int(input("Which task do you want to update : ")) - 1
        if not 0 < index <= len(tasks):
            raise ValueError("Invalid index value")
        clear_screen()
        categories = load_task_category()
        category_index = input("Enter task category : ").strip()
        description = input("Enter task description : ").strip()
        tasks[index]["task_category"] = categories.get(category_index)
        tasks[index]["task_desc"] = description
        save_task(tasks)
        print("Task updated successfully ✅")
        input("Press Enter to conitnue")
        clear_screen()

    except ValueError : 
        input("\033[93mPlease Enter a valid index\033[0m")
        clear_screen()


def remove_task(tasks):
    clear_screen()
    list_task(tasks)
    index = int(input("Which task do you want to delete : ")) - 1
    if not 0 <= index <= len(tasks):
        raise ValueError("Invalid index value")
    del tasks[index]
    save_task(tasks)
    print("Task deleted successfuly ✅")
    input("Press Enter to continue")
    clear_screen()


def load_data():
    try:
        with open(TASK_DIR, "r") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                print_warning("!! Tasks were abruptly deleted or not created yet !!")
                return []

    except FileNotFoundError:
        return []


def list_task(tasks):
    if not tasks : 
        print("There are no taks .. add one to get started with : ")

    else : 
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.get('task_category')} : {task.get('task_desc')}")
        print()
 
    

def menu() : 
    print("1. List task")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")
    choice = input("\nEnter whats on your mind : ")
    print("-" * 90)
    return choice




def main():
    tasks = load_data()

    print("Hello there bozo..! what would you like to hit today ?")
    print("-" * 90)
    while True:
        choice = menu()
        match choice:
            case "1":
                clear_screen()
                list_task(tasks)
                input("Press Enter to continue")
                clear_screen()
            case "2":
                add_task(tasks)
            case "3":
                update_task(tasks)
            case "4":
                remove_task(tasks)
            case "5":
                break
            case _:
                print("Well you wouldn't want it but fuck you!!")
                print("Lets do it again..!")
                print("-" * 90)


if __name__ == "__main__":
    main()
