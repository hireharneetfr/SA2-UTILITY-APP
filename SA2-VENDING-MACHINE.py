print('┌───────────────────────────────────────────────────────────────────┐')
print('│          WELCOME TO 🎀 YOUR CRAVINGS 🎀 VENDING MACHINE           │')
print('│         Warning: May cause uncontrollable snack cravings.         │')
print('└───────────────────────────────────────────────────────────────────┘')

def vending_machine_simulation(user_balance):
    total_spent = 0
 
    beverages = [
        {'code': '001', 'name': 'Coca Cola', 'price': 2.0},
        {'code': '002', 'name': 'Sprite', 'price': 2.0},
        {'code': '003', 'name': 'Mountain Dew', 'price': 2.5},
        {'code': '004', 'name': 'Regular Water', 'price': 1.0},
    ]

    snacks = [
        {'code': '011', 'name': 'Oman Chips', 'price': 1.5},
        {'code': '012', 'name': 'Lays', 'price': 2.0},
        {'code': '013', 'name': 'Bugles', 'price': 1.75},
        {'code': '014', 'name': 'Pringles', 'price': 3.0},
    ]

    sweets = [
        {'code': '021', 'name': 'Milky Bar', 'price': 2.5},
        {'code': '022', 'name': 'Toblerone', 'price': 4.0},
        {'code': '023', 'name': 'Maltesers', 'price': 3.5},
        {'code': '024', 'name': 'Hersheys', 'price': 4.0},
    ]


    def display_menu(category):
        print('\n')
        print('┌───────┬─────────────────┬───────┐')
        print('│ Code  │      Item       │ Price │')
        print('├───────┼─────────────────┼───────┤')
        for item in category:
            code = item['code']
            name = item['name']
            price = f"${item['price']}"
            print(f"│{code.center(7)}│{name.center(17)}│{price.center(7)}│")
        print('└───────┴─────────────────┴───────┘')

    def select_item(category):
        while True:
            user_input = input("🌟 Enter the code of your desired item, type 'cancel' if you change your mind: ")
            if user_input.lower() == 'cancel':
                return None
            for item in category:
                if item['code'].lower() == user_input.lower():
                    return item
            print('\n ⚠️ Error: Item code not recognized. Please try again.')

    def process_payment(selected_item, current_total):
        item_price = float(selected_item['price'])
        print('\n────────────────────────────────────────────────────────────────────')
        print(f"                 🎀 Enjoy your {selected_item['name']}!🎀 ")
        return current_total + item_price

    while True:
        print('\n 🌟 Please select a category of item to purchase: ')
        print('1 - 🥤 Beverages')
        print('2 - 🍟 Snacks')
        print('3 - 🍫 Sweets')
        print('4 - ✅ Finish purchase')

        user_choice = input('🌟 Please enter the number of your choice: ')

        if user_choice == '4':
            print('\n────────────────────────────────────────────────────────────────────')
            print('┌───────────────────────────────────────────────────────────────────┐')
            print('│                🎀 Thank you for your patronage! 🎀                │')
            print('└───────────────────────────────────────────────────────────────────┘')
            break

        elif user_choice in ['1', '2', '3']:
            if user_choice == '1':
                display_menu(beverages)
                selected_item = select_item(beverages)
            elif user_choice == '2':
                display_menu(snacks)
                selected_item = select_item(snacks)
            elif user_choice == '3':
                display_menu(sweets)
                selected_item = select_item(sweets)

            if selected_item:
                total_spent = process_payment(selected_item, total_spent)
                if selected_item['code'] == '001':
                    print("            🌟 Customers also bought: Lays, Toblerone")
                    print('\n────────────────────────────────────────────────────────────────────')
                elif selected_item['code'] == '014':
                    print("            🌟 Customers also bought: Mountain Dew, 'Maltesers")
                    print('\n────────────────────────────────────────────────────────────────────')
                elif selected_item['code'] == '024':
                    print("            🌟 Customers also bought: Oman Chips, Sprite")
                    print('\n────────────────────────────────────────────────────────────────────')
                elif selected_item['code'] == '004':
                    print("            🌟 Customers also bought: Bugles, Milky Bar")
                    print('\n────────────────────────────────────────────────────────────────────')
        else:
            print('⚠️ Error: Invalid choice. Please try again.')

    return total_spent


def get_user_balance():
    while True:
        try:
            user_balance = float(input('💵 Please input your payment amount: $'))
            if user_balance <= 0:
                print('⚠️ Error: Amount must be greater than $0.')
            else:
                return user_balance
        except ValueError:
            print('⚠️ Error: Please enter a valid numeric amount.')

balance = get_user_balance()


while True:
    total_cost = vending_machine_simulation(balance)

    if total_cost > balance:
        print('            ⚠️  Insufficient funds. Transaction canceled ⚠️')
        print('          Please select items within your available balance.')
        print('────────────────────────────────────────────────────────────────────\n')
        print('🔄 Returning to selection menu...')
        print(' ')
    else:
        remaining_balance = balance - total_cost
        print('         Your items have been delivered. 🎀 Bon appétit! 🎀        ')
        print('────────────────────────────────────────────────────────────────────')    
        print(f'\n 💰 Total: ${total_cost:.2f}')
        print('────────────────────────────────────────────────────────────────────')
        print(f' 💵 Change: ${remaining_balance:.2f}')
        print('────────────────────────────────────────────────────────────────────')
        print('\n')
        break
