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
