print('┌───────────────────────────────────────────────────────────────────┐')
print('│          WELCOME TO 🎀 YOUR CRAVINGS 🎀 VENDING MACHINE           │')
print('│         Warning: May cause uncontrollable snack cravings.         │')
print('└───────────────────────────────────────────────────────────────────┘')
#user is welcomed with a welcome message by the help of simple print function

def vending_machine_simulation(user_balance):
    total_spent = 0
  #user balance is shown as 0 before the user can input the funds
    beverages = [ #with the help of dictionary function, all items are stored in "beverages", which also shows code names and prices
        {'code': '001', 'name': 'Coca Cola', 'price': 2.0},
        {'code': '002', 'name': 'Sprite', 'price': 2.0},
        {'code': '003', 'name': 'Mountain Dew', 'price': 2.5},
        {'code': '004', 'name': 'Regular Water', 'price': 1.0},
    ]

    snacks = [ #with the help of dictionary function, all items are stored in "snacks", which also shows code names and prices
        {'code': '011', 'name': 'Oman Chips', 'price': 1.5},
        {'code': '012', 'name': 'Lays', 'price': 2.0},
        {'code': '013', 'name': 'Bugles', 'price': 1.75},
        {'code': '014', 'name': 'Pringles', 'price': 3.0},
    ]

    sweets = [ #with the help of dictionary function, all items are stored in "sweets", which also shows code names and prices
        {'code': '021', 'name': 'Milky Bar', 'price': 2.5},
        {'code': '022', 'name': 'Toblerone', 'price': 4.0},
        {'code': '023', 'name': 'Maltesers', 'price': 3.5},
        {'code': '024', 'name': 'Hersheys', 'price': 4.0},
    ]

    def display_menu(category): #This function is used to show the user the items in a clean table
        print()
        print('┌───────┬─────────────────┬───────┐')
        print('│ Code  │      Item       │ Price │') #cleanly put table showing code, item and the price for user to see
        print('├───────┼─────────────────┼───────┤')
        for item in category: #loops through each item in the specified category
            code = item['code'] #gets the items code
            name = item['name'] #gets the name
            price = f"${item['price']}" #gets the price as a string with a $ sign 
            print(f"│{code.center(7)}│{name.center(17)}│{price.center(7)}│") #geting the values in a row with centred values
        print('└───────┴─────────────────┴───────┘')
        print()

    def select_item(category): #This function allows the user to select an item by entering its code
      while True:
            user_input = input("🌟 Enter the code of your desired item, type 'cancel' if you change your mind: ") #asks the user to enter the code of the desired item or to type cancel if not
            if user_input.lower() == 'cancel': #this is for if the user says cancel
                return None
            for item in category:
                if item['code'].lower() == user_input.lower(): #to verify if the code user gave matches item code    
                    return item
            print('\n ⚠️ Error: Item code not recognized. Please try again.') #This comment is shown if the code is not recognized 

    def process_payment(selected_item, current_total):
        item_price = float(selected_item['price']) #converts price of the item to a float
        print('\n───────────────────────────────────────────────────────────────────────────') #It also displays a fun message after a purchase is made
        print(f"                  🎀 Enjoy your {selected_item['name']}!🎀 ")
        print("Would you like to purchase another item? If not, press 4 to finish purchase") #It asks the user if there is any need of another item or to finish purchase
        print('\n───────────────────────────────────────────────────────────────────────────')

        return current_total + item_price #This function processes the payment by adding the item’s price to the total spent

    while True: 
        print('\n 🌟 Please select a category of item to purchase: ') #here are the categories for the user to choose from 
        print()
        print('1 - 🥤 Beverages') #if pressed 1, user is shown beverage options
        print('2 - 🍟 Snacks') #if pressed 2, user is shown snacks options
        print('3 - 🍫 Sweets') #if pressed 3, user is shown sweets options
        print('4 - ✅ Finish purchase') #if the user is done with the purchase, user can type 4 to finish purchase
        print()

        user_choice = input('🌟 Please enter the number of your choice: ') #asks the user to input what user might need

        if user_choice == '4':
            print('\n────────────────────────────────────────────────────────────────────')
            print('┌───────────────────────────────────────────────────────────────────┐')
            print('│                🎀 Thank you for your patronage! 🎀                │') #a sweet thank you message for the user
            print('└───────────────────────────────────────────────────────────────────┘')
            break

        elif user_choice in ['1', '2', '3']: #this is to make sure the user has input the right code
            if user_choice == '1':
                display_menu(beverages) #if the user has input 1, the user is shown the beverages menu
                selected_item = select_item(beverages) #this function lets the user to choose from beverages menu
            elif user_choice == '2':
                display_menu(snacks) #if the user has input 2, the user is shown the snacks menu
                selected_item = select_item(snacks) #this funtion lets the user to choose from snacks menu
            elif user_choice == '3':
                display_menu(sweets) #if the user has input 3, the user is shown the sweets menu
                selected_item = select_item(sweets) #this function lets the user to choose from sweets menu

            if selected_item:
                total_spent = process_payment(selected_item, total_spent) #processes the payment for the selected item and updates the total spent
                if selected_item['code'] == '001': #This function is to suggest items to the user, if the user inputs 001 the below is shown
                    print("     🌟 Customers who bought this item also purchased: Lays, Toblerone") #the user is suggested lays and toblerone
                    print('\n───────────────────────────────────────────────────────────────────────────')
                elif selected_item['code'] == '014': #if the user inputs 014, the below is shown
                    print("     🌟 Customers who bought this item also purchased: Mountain Dew, 'Maltesers") #the user is suggested lays and toblerone
                    print('\n───────────────────────────────────────────────────────────────────────────')
                elif selected_item['code'] == '024': #if the user inputs 024, the below is shown
                    print("     🌟 Customers who bought this item also purchased: Oman Chips, Sprite") #the user is suggested Oman Chips and Sprite
                    print('\n───────────────────────────────────────────────────────────────────────────')
                elif selected_item['code'] == '004': #if the user inputs 004, the below is shown
                    print("     🌟 Customers who bought this item also purchased: Bugles, Milky Bar") #the user is suggested Bugles and Milky Bar
                    print('\n───────────────────────────────────────────────────────────────────────────')
        else:
            print('⚠️ Error: Invalid choice. Please try again.') #if the user inputs a wrong code, an error is shown and the user is asked to try again

    return total_spent #returns the total amount spent


def get_user_balance(): #asks the function to get users payment amount
    while True:
        try:
            user_balance = float(input(' 💵 Please input your payment amount: $')) #asks the user for a float amount to be input
            if user_balance <= 0: #this function is to check if the input is greater then 0
                print('⚠️ Error: Amount must be greater than $0.')  #error is shown if the input is not greater then 0
            else:
                return user_balance
        except ValueError: #This function is to make sure there is no non numeric input
            print('⚠️ Error: Please enter a valid numeric amount.') #If the input is not a number, an error is displayed

balance = get_user_balance() #This function stores the user balance


while True: #starting of an loop
    total_cost = vending_machine_simulation(balance) #to store the total cost

    if total_cost > balance:
        print('            ⚠️  Insufficient funds. Transaction canceled ⚠️')
        print('          Please select items within your available balance.') #Prints this message when the funds are low
        print('────────────────────────────────────────────────────────────────────\n')
        print('🔄 Returning to selection menu...') #User is then sent back to menu
        print(' ')
    else:
        remaining_balance = balance - total_cost #If the user has enough balance to be able to buy desired item, balance is displaced
        print('         Your items have been delivered. 🎀 Bon appétit! 🎀        ') #With a items being delivered and a sweet bon appetit message :)
        print('────────────────────────────────────────────────────────────────────')    
        print(f'\n 💰 Total: ${total_cost:.2f}') #This shows the total spent by the user
        print('────────────────────────────────────────────────────────────────────')
        print(f' 💵 Change: ${remaining_balance:.2f}') #This shows any change/balance tht remain after the purchase was made
        print('────────────────────────────────────────────────────────────────────')
        print()
        break #to break the loop 