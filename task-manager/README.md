# Task Manager

## What This Is
A simple command-line task manager to organize daily tasks by categories.

## Why This Exists
This is my you may say first complete Python project after learning the basics. 
No tutorials, no copy-pasting.. just me solving a real problem with code I understand.

## What I Learned Building This
- **File I/O**: Reading/writing JSON files for data persistence
- **Error Handling**: Proper try/except blocks and input validation
- **Data Structures**: Working with lists of dictionaries
- **User Experience**: Designing clear CLI interactions
- **Code Organization**: Separating concerns into functions
- **More Python Insights**: A lot of things i wouldn't have known if i didn't decide to go in deep

## Challenges I Faced
- Abrupt external action's consequences handling
- Making the interface user-friendly despite being a cli

## Code I'm Proud Of
```python
#This part is the one that confused me
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
```

### You want to use it ? 
- clone the repo using ```git clone https://github.com/realSUDO/from-the-scratch/task-manager.git```
- run the thing using ```cd task-manager && python task-manager.py```


