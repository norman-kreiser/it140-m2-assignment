"""Given a prompt with a name and age, then determine and report birth year.

Input:
    name: str, typed by the user
    age: int, typed by the user

Process:
    Subtract the user's age from the current year to get birth year

Output:
    A 'Hello", with the user's birth year

Typical usage example:
    What is your name? Alex
    How old are you? 24
    Hello Alex! You were born in 2001.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name?")
    age = int(input("How old are you?"))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"\nHello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===

