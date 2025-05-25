class Habit:
    def __init__(self, name):
        self.name = name
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✅" if self.done else "❌"
        return f"{self.name} - {status}"


class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, name):
        habit = Habit(name)
        self.habits.append(habit)

    def mark_habit_done(self, name):
        for habit in self.habits:
            if habit.name.lower() == name.lower():
                habit.mark_done()
                return True
        return False

    def show_all_habits(self):
        if not self.habits:
            print("No habits added yet.")
        for habit in self.habits:
            print(habit)

    def show_completed_habits(self):
        completed = [habit for habit in self.habits if habit.done]
        if not completed:
            print("No completed habits yet.")
        for habit in completed:
            print(habit)

    def show_pending_habits(self):
        pending = [habit for habit in self.habits if not habit.done]
        if not pending:
            print("No pending habits!")
        for habit in pending:
            print(habit)


def main():
    tracker = HabitTracker()
    while True:
        print("\nChoose an option:")
        print("1. Add habit")
        print("2. Mark habit done")
        print("3. Show all habits")
        print("4. Show completed habits")
        print("5. Show pending habits")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            name = input("Enter habit name to add: ")
            tracker.add_habit(name)
            print(f"Habit '{name}' added.")

        elif choice == '2':
            name = input("Enter habit name to mark as done: ")
            if tracker.mark_habit_done(name):
                print(f"Habit '{name}' marked as done.")
            else:
                print(f"Habit '{name}' not found.")

        elif choice == '3':
            print("\nAll Habits:")
            tracker.show_all_habits()

        elif choice == '4':
            print("\nCompleted Habits:")
            tracker.show_completed_habits()

        elif choice == '5':
            print("\nPending Habits:")
            tracker.show_pending_habits()

        elif choice == '6':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1 to 6.")


if __name__ == "__main__":
    main()

