"""A simple command-line to-do list."""


def show_tasks(tasks):
    if not tasks:
        print("No tasks added yet.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. [{status}] {task['title']}")


def main():
    tasks = []

    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            title = input("Task name: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                print("Task added.")
            else:
                print("Task name cannot be empty.")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            if not tasks:
                continue

            try:
                number = int(input("Task number to mark done: "))
                if 1 <= number <= len(tasks):
                    tasks[number - 1]["done"] = True
                    print("Task marked as done.")
                else:
                    print("That task number does not exist.")
            except ValueError:
                print("Please enter a whole number.")

        elif choice == "4":
            print("To-do list closed.")
            break
        else:
            print("Please choose an option from 1 to 4.")


if __name__ == "__main__":
    main()
