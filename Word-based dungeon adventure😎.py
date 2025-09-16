"""
Now you have all the pieces in place, it's time to write your story!

For this task you'll implement a recursive function to create a story that has a number of random encounters using the previous tasks you've implemented. Make sure you are using your previously implemented functions! You can copy paste them into this task.

As this function relies on a lot of randomised behaviour, it will be manually marked. 

This means the "Mark" test will only be checking some of the requirements, like using recursion and no loops.

The function story() should:

Take one parameter:

An integer, that should determine the number of encounters your adventurer will run into.

Upon entering the dungeon, your explorer should be greeted with the message (this does not count as an encounter): 

"You enter the dungeon..."

Then, there are four different encounters that can occur, each with the same chance of happening:

Encounter 1 — Finding stairs:

Your explorer finds some descending stairs. You should ask the user "You've found some descending stairs, would you like to go down? "

If the user responds with "yes" or "y", using any letter casing, then you should print a random number of stairs between 1 and 10 inclusive.

If they choose not to, then you should print "You choose not to go down."

Encounter 2 — Finding treasure:

Your explorer finds some treasure. There is a 90% chance it is a square gem, and a 10% chance it is a rare diamond.

If they find the square gem you should print "You found a square gem!" and print a square of random size between 1 and 5 inclusive.

If they find the rare diamond you should print "You found a rare diamond!" and print a diamond with a random odd number between 1 and 15 inclusive.

Encounter 3 — Mirror realm:

Your explorer finds the mirror realm. You should let them know and ask them to test it with "You've found the mirror realm! Anything you say will be reversed, try it out: "

You should then print the users message in reverse order.

Encounter 4 — Mysterious Stranger:

Your explorer finds a mysterious stranger. Let them know with the message: "You come across a mysterious stranger, he warns you that..."

Assume there is a file called "stranger_structure.txt" which contains the sentence structure this mysterious stranger will use to say sentences. You can assume that their sentence structure begins with the <s> symbol and use this to make the initial function call. (Note you cannot make these assumptions for your "The Stranger" implementation)

Print a random sentence based off this sentence structure for your explorer.
"""

import random

def stairs(n):
    # Base case
    if n <= 0:
        return
    # Recursive call
    stairs(n - 1)
    print("\U00002585" * n)

#Define and implement your square function here
def square(square_size, current_calls = 0):
    # Base case
    if square_size <= 0 or current_calls == square_size:
        return
    
    if current_calls == 0 or current_calls == square_size - 1:
        print("\u25C6" * square_size)
    # Spaces in the middle
    else:
        print("\u25C6" + " " * (square_size - 2) + "\u25C6")
    
    # Recursive call
    square(square_size, current_calls + 1)

#Define and implement your diamond function here
def diamond(diamond_size, current_calls = 0):
    # Base case
    if diamond_size <= 0 or diamond_size % 2 == 0 or current_calls == diamond_size:
        return

    # Since the shape is symmetry, we can first calculate the middle row index
    mid = diamond_size // 2
    # Calculate distance from the middle row
    distance = abs(mid - current_calls)
    # Top and bottom cases
    if current_calls == 0 or current_calls == diamond_size - 1:
        print(" " * distance + "*" + " " * distance)

    else:
        # Calculate how many spaces go between the stars
        # Total line structure (from left to right):
        # [distance spaces] + * + [inner_distance spaces] + * + [distance spaces]
        inner_distance = diamond_size - 2 * distance - 2
        # Leading spaces + left star + inner spaces + right star + trailing spaces
        print(" " * distance + "*" + " " * inner_distance + "*" + " " * distance)
    # Recursive call
    diamond(diamond_size, current_calls + 1)


#Define and implement your mirror function here
def mirror(text):
    # Base case :empty string
    if text == "":
        # Ensures the output ends with a newline character
        print()
        return

    # Print the last character of the current string without a newline
    print(text[-1], end = "")
    # Recursive call
    mirror(text[:-1])


#Define and implement generate_structure function here.
def generate_structure(filepath):
    structure = {}
    # Get the structure from a provided file
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                # Skip empty line
                continue
            # Split the line into a key (symbol) and an expression
            key,expression = line.split(":")
            # Split the expression into a list of options by '|'
            options = expression.split("|")
            # Store the key and options into the structure dictionary
            structure[key.strip()] = [option.strip() for option in options]
        
    return structure

#Define and implement generate_sentence function here.
import random

def generate_sentence(symbol, structure):
    options = structure[symbol]
    choice = random.choice(options)

    # If the chosen option contains a comma, it is a sequence of symbols
    if ',' in choice:                              
            parts = choice.split(',')
            # Recursion
            for part in parts:
                generate_sentence(part.strip(), structure) 
    else:
        # Expand the choice if it is not an actual word
        if choice in structure:
            generate_sentence(choice, structure)
        else:
            # Print the the choice if it is an actual word
            print(choice, end=' ')   


def story(number_of_encounter:int): 
    # Base case
    if number_of_encounter <= 0:
        return

    # Randomly select an encounter type
    encounter = random.randint(1,4)

    if encounter == 1:
        # Encounter 1: Finding descending stairs
        response = input("You've found some descending stairs, would you like to go down? ")
        if response.lower() == "y" or response.lower() == "yes":
            stair_count = random.randint(1, 10)
            stairs(stair_count)
        else:
            # If user declines
            print("You choose not to go down.")

    elif encounter == 2:
        # Encounter 2: Finding treasure
        # There is a 90% chance it is a square gem
        if random.random() < 0.9:#float
            print("You found a square gem!")
            # A square of random size between 1 and 5 inclusive
            size = random.randint(1, 5)
            square(size)
        else:
            # A 10% chance it is a rare diamond
            print("You found a rare diamond!")
            # Print a diamond with a random odd number between 1 and 15 inclusive.
            size = random.choice([i for i in range(1, 16, 2)])
            diamond(size)

    elif encounter == 3:
        # Encounter 3: Finding the mirror realm
        talking = input("You've found the mirror realm! Anything you say will be reversed, try it out: ")
        mirror(talking)

    elif encounter == 4:
        # Encounter 4: Meeting a mysterious stranger
        print("You come across a mysterious stranger, he warns you that...")
        sentence_structure = generate_structure("stranger_structure.txt")
        generate_sentence("<s>", sentence_structure)
        print()

    # Recursive call
    story(number_of_encounter - 1)

if __name__ == "__main__":
    print("You enter the dungeon...")
    try:
        number_of_encounter = int(input("How many encounters would you like to have? "))
        story(number_of_encounter)
    except ValueError:
        print("Please enter a valid number.")

"""
def story(number_of_encounter=None): 
    if number_of_encounter is None:
        print("You enter the dungeon...")
        try:
            number_of_encounter = int(input("How many encounters would you like to have? "))
        except ValueError:
            print("Please enter a valid number.")
            return  # Stop if invalid input

    if number_of_encounter <= 0:
        return

    # 以下是原来的 encounter 随机逻辑
    # ...

    # Recursive call
    story(number_of_encounter - 1)

if __name__ == "__main__":
    story()

"""





















