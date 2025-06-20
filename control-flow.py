# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():
    user_input = input("Please enter a letter (A-Z or a-z): ")
    if len(user_input) != 1:
        print("Oops! Please enter only one character.")
        return
    letter = user_input.lower()
    if not letter.isalpha():
        print(f"'{user_input}' is not an alphabetical letter. Please enter a letter from A to Z.")
        # Stop the function if it's not an alphabet.
        return
    vowels = "aeiou"
    if letter in vowels:
        print(f"The letter {user_input} is a vowel.")
    else:
        print(f"The letter {user_input} is a consonant.")
check_letter()

# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    # This function checks if a user is old enough to vote.
    MIN_VOTING_AGE = 18
    try:
        age_input = input("Please enter your age: ")
        age = int(age_input)
    except ValueError:
        print("Invalid input! Please enter a valid whole number for your age.")
        return
    if age < 0:
        print("Please enter a valid age.")
    elif age >= 18:
            print("Congrats! You can vote!")
    else:
        # If the user is younger than the minimum voting age, figure out how many years they need to wait.
        years_to_wait = MIN_VOTING_AGE - age
        print(f"Sorry, at {age} years old, you are not yet eligible to vote.")
# Call the function to check for voting eligibility
check_voting_eligibility()

# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    """
    Calculates a dog's age in dog years.

    # Prompt the user to enter a dog's age: "Input a dog's age: "

      The first two years of a dog's life are counted as 10 dog years each,
      and each subsequent year is counted as 7 dog years.
    """
        # Prompt the user for the input 
    dog_age = int(input("Input a dog's age:"))
        
        # Calculate dog years
    if dog_age <=2:
      dog_years = dog_age * 10
    else:
      dog_years = (2 * 10) + ((dog_age - 2) * 7)     

    # Print the result
    print(f"The dog's age in dog years is {dog_years}.")

# call the function
calculate_dog_years() 

# Problem 4: Weather advice
#
# Write a Python script named `weather_advice` that provides clothing advice
# based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle
#   multiple conditions.

def weather_advice():
    """ 
    Provides clothing advice based on whether it's cold and/or raining.
    """
    # Have the user input the tempeture outside
    is_cold_input = input("Is it cold today? (yes/no): ").lower()
    # Have the user input it is is raining outside or not
    is_raining_input = input("Is it raining today? (yes/no): ").lower()

    # Confirm is 'yes'/'no' inputs are (True/False) values
    is_cold = (is_cold_input == 'yes')
    is_raining = (is_raining_input == 'yes')

    # Determine clothing advice using logical operators
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    else: # This covers the case where it's not cold AND not raining
        print("Wear light clothing.")

# Call the function to run the script
weather_advice()

# Problem 5: What's the season?
#
# Write a Python function named `determine_season` that figures out the season
# based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three
#   characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month:
#   "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in
#   <season>."

def determine_season():
    month_input = input("Enter the month of the year (Jan - Dec): ")
    try:
        day_input = input("Enter the day of the month: ")
        day = int(day_input)
    except ValueError:
        print("Invalid day! Please enter a number for the day.")
    if not (1 <= day <= 31):
        print("Invalid day! Day must be between 1 and 31.")
        return        
    season = "Unknown" # Default value
    if (month_input == "Dec" and day >= 21) or \
       month_input in ("Jan", "Feb") or \
       (month_input == "Mar" and day <= 19):
        season = "Winter"
    
    elif (month_input == "Mar" and day >= 20) or \
         month_input in ("Apr", "May") or \
         (month_input == "Jun" and day <= 20):
        season = "Spring"
    
    elif (month_input == "Jun" and day >= 21) or \
         month_input in ("Jul", "Aug") or \
         (month_input == "Sep" and day <= 21):
        season = "Summer"
    
    elif (month_input == "Sep" and day >= 22) or \
         month_input in ("Oct", "Nov") or \
         (month_input == "Dec" and day <= 20):
        season = "Fall"
    else:
        print("Could not determine season. Please ensure the month abbreviation is correct (example Jan).")
        return
    print(f"{month_input.capitalize()} {day} is in {season}.")

# Call the function to run the script.
determine_season()