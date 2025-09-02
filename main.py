import time
import random

reviews = [

]

"""
todo:
finish coding review option.
do regular menu
reg menu ordering
do regular menu with alcohol (if i have time)
FAQ option
job app option?
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
    print("1.) Order \n2.) placeholder \n3.) placeholder \n4.) Write a Review \n5.) Exit")
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
        customer_reviews()
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
        if sidechoice1 == 1 or 2 or 3 or 4: 
            print("Please choose your second side.")
            sidechoice2 = int(input(": "))
            if sidechoice2 == 1 or 2 or 3 or 4:
                   print("Processing Order...⟳")
                   time.sleep(2)
                   if mealchoice == 1:
                       print("Your order total will be 8🪙!")
                       payment()
                   elif mealchoice == 2:
                        print("Your order total will be 10🪙!")
                        payment()
                   elif mealchoice == 3:
                       print("Your order total will be 5🪙!")
                       payment() 
                   
            else:
                sidechoice2 = int(input("Please choose a valid number option. \n: "))
        else:
            sidechoice1 = int(input("Please choose a valid number option. \n: "))
            
    else:
        mealchoice = int(input("Please pick a valid number option. "))

def payment():
    creditcardnumber = random.randint(100000000,999999999)
    print('-'*25)
    print(f"Credit Card Number: {creditcardnumber}💳")
    userinput = int(input("Type in your Credit Card Number to finish Ordering! "))
    while userinput != creditcardnumber:
        print("Processing...⟳ please wait.")
        time.sleep(2)
        print(f"Credit Card Number: {creditcardnumber}💳")
        userinput = int(input("ERROR_-Invalid Number❌ Try Again. "))
    print("Processing...⟳ pleast wait.")
    print('-'*15)
    ordernumber = random.randint(1000,9999)
    time.sleep(2)
    print(f"Transcastion Complete! \nYour Order Number is {ordernumber}🎫!")
    time.sleep(1)
    print("Thank you for supporting Slingshot's Cafe! Come Again")

def regularmenu():
    print("regular menu")

def orderregularmenu():
    print("What would you like to order?")

def alcoholmenu():
    print("regular menu with alcohol")

def orderalcoholmenu():
    print("What would you like to order?")

def customer_reviews():
    print("Welcome to the Review Page of Slingshot's Cafe!")
    print("-"*30)
    print("Liked your food? Please Rate Us!")
    time.sleep(3)
    print("...If you didn't, please don't.")
    time.sleep(2)
    print('-'*15)
    name = input("Who is reviewing?: ")
    review = input("What would you like to say about your experience? ")
    stars = int(input("How many stars would you rate? "))
    newreview = Reviews(name,review,stars)
    reviews.append(newreview.features())
    print(f"Thank you for your review {name}!")
    see_review = int(input("Would you like to see your review? \n1.) Yes \n2.) No \n: "))
    if see_review == 1:
        show_reviews()
    elif see_review == 2:
        print("main menu")
    else:
        see_review = int(input("Please pick a valid number option. : "))

def show_reviews():
    for review in reviews:
        for key, value in review.items():
            print(f"{key}: {value}")
            
    print("-"*30)
    
class Reviews:
    def __init__(self,name,review,stars):
        self.reviewid = random.randint(100,999)
        self.name = name
        self.review = review
        self.stars = stars 
    
    def features(self):
        newDictionary = {'Review Id': self.reviewid, 
                         'Reviewer Name': self.name, 
                         'Review': self.review, 
                         'Stars': self.stars}
        return newDictionary

intro()




