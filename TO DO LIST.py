def add_task():
    task=input("ENTER NEW TASK: ")
    todolist.append(task)
    print('TASK ADDED SUCCESFULLY')
def view_task():
    if len(todolist) == 0:
        print("NO TASKS IN THE LIST")
    else:
        print('TO DO LIST: ')
        for i,task in enumerate(todolist):
            print(f'{i+1}. {task}')
def del_task():
    if len(todolist) == 0:
        print("NO TASKS IN THE LIST")
    else:
        print('TO DO LIST: ')
        for i,task in enumerate(todolist):
            print(f'{i+1}. {task}')
        choice=int(input("ENTER TASK NUMBER T0 DELETE: "))
        if 0<=choice<=len(todolist):
            del todolist[choice-1]
            print("TASK DELETED SUCCESSFULLY")
        else:
            print(("INVALID TASK NUMBER"))

def main():
    while True:
        print("~~~~ TO DO LIST~~~~")
        print('1. ADD TASK')
        print('2. DELETE TASK')
        print('3. VIEW TASK')
        print('4. EXIT')

        choice=int(input("ENTER CHOICE: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            del_task()
        elif choice == 3:
            view_task()
        elif choice == 4:
            print("THANKS FOR USING TO DO LIST")
            break
        else:
            print('INAVLID CHOICE TRY AGAIN')


if __name__=='__main__':
    main()