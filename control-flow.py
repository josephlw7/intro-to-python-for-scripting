def check_letter():
  """
  Prompts the user to enter a letter (a-z or A-Z) and determines if it's a vowel or a consonant.
  Handles both uppercase and lowercase letters and provides feedback for invalid input.
  """
  letter = input("Enter a letter: ")

  # Convert the input to lowercase for case-insensitive comparison
  letter = letter.lower()

  # Check if the input is a single alphabetical character
  if not letter.isalpha() or len(letter) != 1:
    print("Invalid input. Please enter a single alphabetical character.")
  elif letter in 'aeiou':
    print(f"The letter {letter} is a vowel.")
  else:
    print(f"The letter {letter} is a consonant.")

# Call the function to run the program
check_letter()


def check_voting_eligibility():
    """
    Checks if a user is old enough to vote based on their input age.
    Handles invalid input (non-integer or negative age).
    """
    voting_age = 18  # Set the minimum voting age

    while True:  # Loop to continue prompting until valid input is received
        try:
            # Prompt the user to enter their age and attempt to convert it to an integer
            age_str = input("Please enter your age: ")
            age = int(age_str)

            # Validate input: Check if age is a possible value (non-negative)
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
            else:
                break  # Exit the loop if input is valid

        except ValueError:
            # Handle cases where the input cannot be converted to an integer
            print("Invalid input. Please enter a valid integer age.")

    # Determine if the user is eligible to vote based on the entered age
    if age >= voting_age:
        print("You are eligible to vote!")
    else:
        # Calculate years left until eligible and print the message
        years_left = voting_age - age
        print(f"You are not eligible to vote. You have {years_left} years left until you are eligible.")

# Call the function to check voting eligibility
check_voting_eligibility()

