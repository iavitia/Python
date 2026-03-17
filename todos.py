header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""
print(header)

todos = []
completed = []

while True:
    command = input("Enter a command. Type 'h' for help: \n")

    if command.isdigit():
         # complete todo
        if int(command) <= len(todos):
            todo_completed = todos.pop(int(command) - 1)
            completed.append(todo_completed)
        else:
            print("Invalid number")
    
    # Display help menu
    elif command == "h":
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("To complete a todo, enter its number")
    
    # quitting the program
    elif command == "q":
        ln = len(completed)
        print(f"Today you completed {ln} todos:")
        for complete in completed:
            print(f"* {complete}")
        break
    
    # add todo to list
    else:
        todos.append(command)

    # display todos
    idx = 0
    for idx in range(len(todos)):
        print(f"{idx + 1}) {todos[idx]}")

    print("*" * 50)