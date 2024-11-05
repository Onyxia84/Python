import msvcrt
import time
from game import game

def main_menu() :
    a = 1
    while a == 1 :
        message = """Main Menu:
1. Create New Game
2. Load Saved 
3. About
4. Exit
"""
        print(message)
        while msvcrt.kbhit() == False:  
            touche = msvcrt.getch().decode('utf-8') 
            print (">" + touche)
            if touche == '1':  
                print("Enter your name:")
                x = input()
                time.sleep(1)
                print('Hello, ' + x)
                time.sleep(1)
                game()
                break
            elif touche == '2' :
                print("Loading game")
            elif touche == '3' :
                print("About")
            elif touche == '4' :
                print("Leaving game...")
                a = 2
                break
            else :
                print("Incorrect input please retry")
                continue