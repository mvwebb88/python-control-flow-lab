# Python Control Flow Lab 

# - print() = console.log()
# - input() = prompt()
# - Indentation replaces {}
# - True/False are capitalized

# Helper functions (safe input)

def get_yes_no(prompt):
    """Keep asking until the user enters yes/no."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Please type yes or no (y/n).")


def get_non_negative_int(prompt):
    """Keep asking until the user enters a whole number 0 or greater."""
    while True:
        value = input(prompt).strip()

        # isdigit() prevents int() from crashing (safe input)
        if value.isdigit():
            return int(value)
        else:
            print("Please enter a whole number like 0, 5, or 18.")


# Exercise 0: Example

def print_greeting():
    python_is_fun = True  # Similar to JS: const pythonIsFun = true;

    if python_is_fun:
        print("Python is fun!")


# Exercise 1: Vowel or Consonant

def check_letter():
    while True:
        user_input = input("Please enter a letter (a-z or A-Z): ").strip()

        # Must be exactly 1 letter
        if len(user_input) == 1 and user_input.isalpha():
            break
        else:
            print("Invalid entry. Please enter exactly ONE letter.")

    letter = user_input.lower()
    vowels = "aeiou"

    if letter in vowels:
        print(f"The letter {user_input} is a vowel.")
    else:
        print(f"The letter {user_input} is a consonant.")


# Exercise 2: Old enough to vote?

def check_voting_eligibility():
    voting_age = 18
    age = get_non_negative_int("Please enter your age: ")

    if age > 120:
        print("That age seems unlikely. Please double-check your entry.")
    elif age >= voting_age:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")


# Exercise 3: Calculate Dog Years

def calculate_dog_years():
    dog_age = get_non_negative_int("Input a dog's age: ")

    if dog_age <= 2:
        dog_years = dog_age * 10
    else:
        dog_years = 20 + (dog_age - 2) * 7

    print(f"The dog's age in dog years is {dog_years}.")


# Exercise 4: Weather Advice (and / or / not)

def weather_advice():
    is_cold = get_yes_no("Is it cold? (yes/no): ")
    is_raining = get_yes_no("Is it raining? (yes/no): ")

    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif (not is_cold) and is_raining:
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

    # Quick OR example (to meet the learning goal)
    if is_cold or is_raining:
        print("Bonus tip: Check the forecast before you head out!")


# Exercise 5: What's the Season?

def determine_season():
    valid_months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

    # Loop until valid month is entered
    while True:
        month = input("Enter the month of the year (Jan - Dec): ").strip().title()
        if month in valid_months:
            break
        else:
            print("Invalid month. Please enter a 3-letter month like Jan, Feb, Mar, etc.")

    # Loop until valid day is entered
    while True:
        day_input = input("Enter the day of the month: ").strip()
        if day_input.isdigit():
            day = int(day_input)
            if 1 <= day <= 31:
                break
        print("Invalid day. Please enter a number from 1 to 31.")

    if (month == "Dec" and day >= 21) or (month in ("Jan", "Feb")) or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or (month in ("Apr", "May")) or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or (month in ("Jul", "Aug")) or (month == "Sep" and day <= 21):
        season = "Summer"
    else:
        season = "Fall"

    print(f"{month} {day} is in {season}.")

# Loop demo (for-loop + processing a sequence)

def loop_demo():
    word = input("Type a word: ").strip().lower()
    vowels = "aeiou"
    vowel_count = 0

    # for loop is like JS: for (const char of word)
    for char in word:
        if char in vowels:
            vowel_count += 1

    print(f"'{word}' has {vowel_count} vowel(s).")


# Menu (so one exercise at a time)

def main():
    while True:
        print("\nWhich exercise do you want to run?")
        print("0 - Example")
        print("1 - Vowel or Consonant")
        print("2 - Old enough to vote?")
        print("3 - Calculate Dog Years")
        print("4 - Weather Advice")
        print("5 - What's the Season?")
        print("6 - Loop Demo (extra practice)")
        print("q - Quit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "0":
            print_greeting()
        elif choice == "1":
            check_letter()
        elif choice == "2":
            check_voting_eligibility()
        elif choice == "3":
            calculate_dog_years()
        elif choice == "4":
            weather_advice()
        elif choice == "5":
            determine_season()
        elif choice == "6":
            loop_demo()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 0-6 or q.")


# This makes the menu run when you do: python3 exercises.py
main()


