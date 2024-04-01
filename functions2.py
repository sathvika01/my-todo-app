FILEPATH = "todos.txt"
def get_todos(filename = FILEPATH):
    """
    Reads a text file and returns the items as a list
    """

    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local




def write_todos(todos_arg,filepath = FILEPATH):
    """Writes the todos items into todos.txt"""

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())

