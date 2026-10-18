from datetime import datetime

expenses = []


def add_expense():
    name = input("What did you spend money on? ").strip()

    if not name:
        print("Please enter an expense name.")
        return

    try:
        amount = float(input("Enter the amount (Rs.): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    expense = {
        "name": name,
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y")
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nYour Expenses")
    print("-" * 40)

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['name']} - "
            f"Rs. {expense['amount']:.2f} "
            f"({expense['date']})"
        )

    print("-" * 40)
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spent: Rs. {total:.2f}")


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Expense tracker closed.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
