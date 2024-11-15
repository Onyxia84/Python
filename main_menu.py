import msvcrt
from about import about
import time
from game import game

# Main menu function to navigate the game options
def main_menu():
    continue_menu = True  # Variable to control the menu loop
    while continue_menu:
        # Display the main menu options
        message = """Main Menu:
1. Create New Game
2. Load Saved Game
3. About
4. Exit
"""
        print(message)

        # Wait for a key press from the user
        while not msvcrt.kbhit():
            pass  # Wait until a key is pressed

        key_pressed = msvcrt.getch().decode('utf-8')  # Capture the pressed key
        print(">" + key_pressed)

        # Handle user input based on the key pressed
        if key_pressed == '1':
            print("Enter your name:")  # Prompt for user name
            user_name = input()
            time.sleep(1)  # Pause for better user experience
            print(f'Hello, {user_name}')
            time.sleep(1)
            game()  # Start a new game
            break

        elif key_pressed == '2':
            print("Loading game...")  # Load a saved game

        elif key_pressed == '3':
            about()
            continue  # Display information about the game

        elif key_pressed == '4':
            print("Exiting the game...")  # Exit the program
            continue_menu = False  # Stop the menu loop

        else:
            print("Invalid input, please try again.")  # Handle invalid inputs
            continue
