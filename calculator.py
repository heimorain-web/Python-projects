"""A small command-line calculator."""


def get_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    first = get_number("First number: ")
    operation = input("Choose an operation (+, -, *, /): ").strip()
    second = get_number("Second number: ")

    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        if second == 0:
            print("Cannot divide by zero.")
            return
        result = first / second
    else:
        print("Unknown operation.")
        return

    print(f"Result: {result:g}")


if __name__ == "__main__":
    main()
