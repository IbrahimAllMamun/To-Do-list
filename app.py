tasks = []


def show_menu():
    print("Menu:")
    print("1. Add a task")
    print("2. Mark as done")
    print("3. View todo list")
    print("4. Exit \n")


show_menu()
user_input = int(input('Enter your choice: '))

while user_input != 4:
    if user_input == 1:
        task = input('What is to be done: ')
        tasks.append(task)
        print('Added task:', task, '\n')
    elif user_input == 2:
        task = input('What is to be marked as done: ')
        if task in tasks:
            tasks.remove(task)
            print('Removed task:', task, '\n')
        else:
            print('The task is not in the list\n')
    elif user_input == 3:
        i = 1
        print('Todo list: ')
        for task in tasks:
            print(str(i)+'. '+task)
            i += 1
        print('\n')
    else:
        print('Please enter one of 1,2,3 or 4\n')
    show_menu()
    user_input = int(input('Enter your choice: '))
print('Goodbye')
