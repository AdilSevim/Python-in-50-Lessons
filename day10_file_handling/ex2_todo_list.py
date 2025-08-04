"""
Day 10, Example 2: Todo List Manager

Purpose: Manage a todo list saved to a file.
We use file handling to save and load todo items.

Expected output when run:
(First creates todo.txt if it doesn't exist)
Todo List:
1. Buy groceries
2. Finish Python project
3. Call mom

Adding new task...
Todo List:
1. Buy groceries
2. Finish Python project
3. Call mom
4. Go to gym
"""

def load_todo_list(filename):
    """Load todo items from a file.
    
    Args:
        filename: Name of the file to load from
    
    Returns:
        A list of todo items
    """
    try:
        with open(filename, "r") as f:
            # Read all lines and remove newline characters
            todos = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        # If file doesn't exist, return empty list
        todos = []
    
    return todos


def save_todo_list(filename, todos):
    """Save todo items to a file.
    
    Args:
        filename: Name of the file to save to
        todos: List of todo items
    """
    with open(filename, "w") as f:
        for todo in todos:
            f.write(todo + "\n")


def display_todo_list(todos):
    """Display the todo list with numbers.
    
    Args:
        todos: List of todo items
    """
    if not todos:
        print("No tasks in the list.")
    else:
        print("Todo List:")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")


def main():
    """Manage a todo list with file persistence."""
    filename = "todo.txt"
    
    # Load existing todo list
    print("Loading todo list...")
    todo_list = load_todo_list(filename)
    
    # If list is empty, add some sample tasks
    if not todo_list:
        todo_list = ["Buy groceries", "Finish Python project", "Call mom"]
        save_todo_list(filename, todo_list)
        print("Created sample todo list.")
    
    # Display current todo list
    display_todo_list(todo_list)
    
    # Add a new task
    print("\nAdding new task...")
    todo_list.append("Go to gym")
    save_todo_list(filename, todo_list)
    
    # Display updated todo list
    display_todo_list(todo_list)


if __name__ == "__main__":
    main()
