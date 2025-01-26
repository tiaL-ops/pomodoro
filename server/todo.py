import json

class Todo:
    def __init__(self, tasks_file="tasks.json"):
        self.tasks = []
        try:
            with open(tasks_file, "r") as file:
                json_array = json.load(file)
                for item in json_array:
                    task = {"Description": item.get("Description", ""), "Status": item.get("Status", "Open")}
                    self.tasks.append(task)
        except FileNotFoundError:
            print(f"Warning: {tasks_file} not found. Starting with an empty task list.")
        except json.JSONDecodeError:
            print(f"Error: Failed to parse {tasks_file}. Starting with an empty task list.")

    def add_task(self, description):
        if description:
            task = {"Description": description, "Status": "Open"}
            self.tasks.append(task)
        else:
            print("Error: Task description cannot be empty.")

    def remove_task(self, description):
        for task in self.tasks:
            if task["Description"] == description:
                self.tasks.remove(task)
                return
        print(f"Error: Task '{description}' not found.")

    def mark_task_done(self, description):
        for task in self.tasks:
            if task["Description"] == description:
                task["Status"] = "Done"
                return
        print(f"Error: Task '{description}' not found.")

    def get_tasks(self):
        return self.tasks

    def save_tasks(self, tasks_file="tasks.json"):
        with open(tasks_file, "w") as file:
            json.dump(self.tasks, file, indent=4)

    @staticmethod
    def main():
        my_todo = Todo()
        while True:
            print("\nMenu:")
            print("1. Add a task")
            print("2. Remove a task")
            print("3. Mark a task as done")
            print("4. Show all tasks")
            print("5. Quit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                task_desc = input("Enter task description: ").strip()
                my_todo.add_task(task_desc)
            elif choice == "2":
                task_desc = input("Enter task description to remove: ").strip()
                my_todo.remove_task(task_desc)
            elif choice == "3":
                task_desc = input("Enter task description to mark as done: ").strip()
                my_todo.mark_task_done(task_desc)
            elif choice == "4":
                tasks = my_todo.get_tasks()
                if tasks:
                    print("\nTasks:")
                    for idx, task in enumerate(tasks, start=1):
                        print(f"{idx}. {task['Description']} - {task['Status']}")
                else:
                    print("\nNo tasks available.")
            elif choice == "5":
                my_todo.save_tasks()
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Todo.main()
