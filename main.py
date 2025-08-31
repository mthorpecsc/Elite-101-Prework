import time
import random

"""
todo:
test out code
finish orderkidsmenu + kidsmenu function
regular menu
regular menu with alcohol
kids menu ordering
regular menu ordering
reg menu + alcohol ordering
other chatbot options

"""

def intro():
    print("💙 Welcome to Slingshot's Cafe! 💙")
    print("We sell an assortment of desserts, drinks, and snacks. 🍰")
    time.sleep(1)
    print("-"*30)
    print("My name is Biscuit, and I can assist you with any questions regarding the cafe!😄")
    time.sleep(2) 
    user_name = input("But first, who's visiting today?: ")
    time.sleep(1)
    print(f"Thank you for choosing to support Slingshot's Cafe {user_name}!😁 How may I help you?")
    time.sleep(1)
    mainmenu()
    
def mainmenu():
    print("1.) Order \n2.) placeholder \n3.) placeholder \n4.) placeholder \n5.) Exit")
    main_menu_option = int(input(": "))
    if main_menu_option == 1:
        myage() 
    elif main_menu_option == 2:
        print("Loading...")
        time.sleep(1)
        print('placehold')
    elif main_menu_option == 3:
        print("Loading...")
        time.sleep(1)
        print('placehold')
    elif main_menu_option == 4:
        print("Loading...")
        time.sleep(1)
        print('placehold')
    else: 
        print("Loading...")
        time.sleep(1)
        print("Please pick a valid choice from the list: ")
        time.sleep(.5)
        print("1.) Order \n2.) placeholder \n3.) placeholder \n4.) placeholder \n5.) Exit")
        main_menu_option = int(input(": "))

def myage():
    print("Welcome to the Ordering page of Slingshot's Cafe!")
    user_age = int(input("What is your age?: "))
    if user_age < 13:
        kidsmenu()
    elif 20 >= user_age >= 13:
        regularmenu()
    elif user_age >= 21:
        alcoholmenu()

def kidsmenu():
    print("Page Loading...")
    time.sleep(1)
    print(" 🌸 You are now viewing the kid's menu for Slingshot's Cafe! 🌸")
    print('-'*30)
    time.sleep(2)
    print("Here's what we have to offer~!")
    print("Meals \n----")
    print("Grilled Cheese (2 Sides) - $8")
    print("Hamburger Meal (1 Side) - $10")
    print("Mac N Cheese Meal (2 Sides) - $5")
    time.sleep(3)
    userchoice = int(input("What would you like to do?: "))
    time.sleep(1)
    print("1.) Order \n2.) View Other Menus \n3.) Exit to Main Menu")
    if userchoice == 1:
        print("Loading...")
        time.sleep(1)
        orderkidsmenu()
    elif userchoice == 2:
        print("other menus")
    elif userchoice == 3:
        mainmenu()

def orderkidsmenu():
    print("What would you like to order?")


def regularmenu():
    print("regular menu")

def orderregularmenu():
    print("What would you like to order?")

def alcoholmenu():
    print("regular menu with alcohol")

def orderalcoholmenu():
    print("What would you like to order?")

#intro()
kidsmenu()
