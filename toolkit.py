"""
Personal Developer Toolkit
Course: Software Engineering Essentials (Python) - Week 8
Author: Gamar Joseph Abwanja
Description: An interactive, menu-driven Python toolkit containing a 
             calculator, a task manager, and a guessing game.
"""

import random


def run_calculator():
    """Tool 1: Simple Calculator using conditionals and f-strings."""
    print("\n--- Tool 1: Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Invalid number input. Returning to main menu.")
        return

    print("\nSelect Operation:")
    print("a. Addition (+)")
    print("b. Subtraction (-)")
    print("c. Multiplication (*)")
    print("d. Division (/)")

    operation = input("Choose operation (a/b/c/d): ").strip().lower()

    if operation == "a":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == "b":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == "c":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == "d":
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result:.2f}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print(f"'{operation}' is an invalid operation choice.")


def run_todo_list():
    """Tool 2: Interactive To-Do List using dynamic lists and loops."""
    print("\n--- Tool 2: Interactive To-Do List ---")
    todo_list = []

    while True:
        print("\nTo-Do Menu: [add] / [remove] / [show] / [back]")
        choice = input("What would you like to do? ").strip().lower()

        if choice == "add":
            task = input("Enter task description: ").strip()
            if task:
                todo_list.append(task)
                print(f"Added task: '{task}'")
            else:
                print("Task cannot be blank.")

        elif choice == "remove":
            task = input("Enter task to remove: ").strip()
            if task in todo_list:
                todo_list.remove(task)
                print(f"Removed task: '{task}'")
            else:
                print(f"'{task}' was not found in your list.")

        elif choice == "show":
            if not todo_list:
                print("Your to-do list is currently empty.")
            else:
                print("\nYour Current Tasks:")
                for index, item in enumerate(todo_list, start=1):
                    print(f"  {index}. {item}")

        elif choice == "back":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please enter add, remove, show, or back.")


def run_guessing_game():
    """Tool 3: Number Guessing Game using loops, random numbers, and conditionals."""
    print("\n--- Tool 3: Number Guessing Game ---")
    secret_number = random.randint(1, 20)
    attempts = 0
    print("I have picked a secret number between 1 and 20. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 20:
                print("Please enter a number within the range 1 to 20.")
                continue

            if guess < secret_number:
                print(f"Too low! Try again.")
            elif guess > secret_number:
                print(f"Too high! Try again.")
            else:
                print(f"Congratulations! You guessed {secret_number} correctly in {attempts} attempt(s)!")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    """Main program loop and menu driver."""
    print("==========================================")
    print(" WELCOME TO THE PERSONAL DEVELOPER TOOLKIT ")
    print("==========================================")

    while True:
        print("\n==================================")
        print("          MAIN MENU               ")
        print("==================================")
        print("1. Simple Calculator")
        print("2. Interactive To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit Program")
        print("==================================")

        user_choice = input("Enter your choice (1-4): ").strip()

        if user_choice == "1":
            run_calculator()
        elif user_choice == "2":
            run_todo_list()
        elif user_choice == "3":
            run_guessing_game()
        elif user_choice == "4":
            print("\nThank you for using the Personal Developer Toolkit. Goodbye!")
            break
        else:
            print(f"\n[!] '{user_choice}' is an invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
    
