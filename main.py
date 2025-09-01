import time
import random

"""
todo:
fix orderkidsmenu
do regular menu
do regular menu with alcohol
do regular menu ordering
do reg menu + alcohol ordering
FAQ option
job app option?
need more ideas

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
        print("Loading...⟳")
        time.sleep(1)
        print('placehold')
    elif main_menu_option == 3:
        print("Loading...⟳")
        time.sleep(1)
        print('placehold')
    elif main_menu_option == 4:
        print("Loading...⟳")
        time.sleep(1)
        print('placehold')
    else: 
        print("Loading...⟳")
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
    print("Page Loading...⟳")
    time.sleep(1)
    print(" 🌸 You are now viewing the kid's menu for Slingshot's Cafe! 🌸")
    print('-'*30)
    time.sleep(2)
    print("Here's what we have to offer~!")
    print("Meals \n----")
    print("Grilled Cheese (2 Sides) - 8🪙")
    print("Hamburger Meal (1 Side) - 10🪙")
    print("Mac N Cheese Meal (2 Sides) - 5🪙")
    time.sleep(3)
    print("What would you like to do?")
    time.sleep(1)
    userchoice = int(input("1.) Order \n2.) View Other Menus \n3.) Exit to Main Menu \n: "))
    if userchoice == 1:
        print("Loading...⟳")
        time.sleep(1)
        orderkidsmenu()
    elif userchoice == 2:
        print("Loading...⟳")
        time.sleep(1)
        print("Other Menus \n------------ \n-*Regular Menu")
        print("Would you to: \n1.) View Regular Menu \n2.) Return to Kid's Menu \n3.) Return to Main Menu")
        time.sleep(2)
        userchoice2 = int(input(":"))
        if userchoice2 == 1:
            print("Loading...⟳")
            time.sleep(1)
            regularmenu()
        elif userchoice2 == 2:
            print("Bringing you back to Kid's Menu...⟳")
            time.sleep(2)
            kidsmenu()
        elif userchoice2 == 3:
            print("Loading...⟳")
            time.sleep(1)
            mainmenu()
        else:
            userchoice2 = int(input("Please pick a valid number option. \n:"))
    elif userchoice == 3:
        print("Exiting to Main Menu...⟳")
        time.sleep(2)
        mainmenu()
    else:
        print("Loading...")
        time.sleep(1)
        userchoice = int(input("Please pick a valid number option. \n:"))

def orderkidsmenu():
    print("-"*30)
    print("Which meal would you like to order?")
    time.sleep(1)
    print("1.) Grilled Cheese (2 Sides) - 8🪙")
    print("2.) Hamburger Meal (1 Side) - 10🪙")
    print("3.) Mac N Cheese Meal (2 Sides) - 5🪙")
    mealchoice = int(input(": "))
    if mealchoice == 1 or 2 or 3:
        print(f"You've picked Meal # {mealchoice}!")
        print("Please choose your first side.")
        print("1.) Mashed Potatos \n2.) Vegetable Mix \n3.) Fruit \n4.) French Fries")
        sidechoice1 = int(input(": "))
        #research how to do this part or redo codE
        if sidechoice1 != 1 or 2 or 3 or 4: 
            sidechoice1 = int(input("Please pick a valid number option. "))

        print("Please choose your second side.")
        sidechoice2 = int(input(": "))

        if sidechoice2 != 1 or 2 or 3 or 4:
            sidechoice2 = int(input("Please pick a valid number option. "))


        print("Processing Order...⟳")
        time.sleep(2)
        print("Your order total will be * 10🪙*")
        payment()
    else:
        mealchoice = int(input("Please pick a valid number option. "))

def payment():
    creditcardnumber = random.randint(100000000,999999999)
    print(f"Credit Card Number: {creditcardnumber}💳")
    userinput = int(input("Type in your Credit Card Number to finish Ordering! "))
    while userinput != creditcardnumber:
        print("Processing...⟳ please wait.")
        time.sleep(2)
        print(f"Credit Card Number: {creditcardnumber}💳")
        userinput = int(input("ERROR_-Invalid Number❌ Try Again. "))
    print("Processing...⟳ pleast wait.")
    ordernumber = random.randint(1000,9999)
    time.sleep(2)
    print(f"Transcastion Complete! \nYour Order Number is {ordernumber}🎫!")


def regularmenu():
    print("regular menu")

def orderregularmenu():
    print("What would you like to order?")

def alcoholmenu():
    print("regular menu with alcohol")

def orderalcoholmenu():
    print("What would you like to order?")

#intro()
orderkidsmenu()



