# Coffee Machine:

coffee={

    'espresso': {'water': 50 , 'coffee': 18, 'milk': 0,'price':1.50},
    'latte' :{'water': 200 , 'coffee': 24, 'milk': 150,'price':2.50},
    'cappuccino':{'water': 250 , 'coffee': 24, 'milk': 100,'price':3.00}
}

resources={
    'milk': 300,
    'water': 300,
    'coffee': 100,
    'money': 1000
}

def report(resources):
    print("Current Status of Resources:")
    print(f"{'Milk'}: {resources['milk']} ml")
    print(f"{'Water'}: {resources['water']} ml")
    print(f"{'Coffee'}: {resources['coffee']} gm")
    print(f"{'Money'}: {resources['money']} $")



def resource_check(choice):
    if coffee[choice]['milk'] > resources['milk']:
        print("Insufficient Milk")
        return False
    elif coffee[choice]['water'] > resources['water']:
        print("Insufficient Water")
        return False
    elif coffee[choice]['coffee'] > resources['coffee']:
        print("Insufficient Coffee")
        return False
    else:
        return True

def exchange(amount,choice):
    if amount > resources['money']:
        print("Insufficient funds available for exchange. Add funds in coffee machine.Money refunded")
        return False
    elif amount < coffee[choice]['price']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources['money']+=coffee[choice]['price']
        print(f"Here is {amount-coffee[choice]['price']:.2f} in exchange")
        return resources

def brew_coffee(choice):
    resources['milk']-=coffee[choice]['milk'] 
    resources['water']-=coffee[choice]['water'] 
    resources['coffee']-=coffee[choice]['coffee']

def add_resources():
    milk=int(input("how many ml of milk to add?:"))
    water=int(input("how many ml of water to add?:"))
    coffee=int(input("how many gm of coffee to add?:"))
    money=int(input("how many $ to add?:"))
    resources['milk']+=milk
    resources['water']+=water
    resources['coffee']+=coffee
    resources['money']+=money


def initiate_machine():
    isOn = True
    while isOn:
        choice=input("What would you like? espresso/latte/cappuccino: ").lower()
        if choice in ["espresso","latte","cappuccino"]:
            if resource_check(choice):
                print("Please insert coins.")
                quaters=int(input("how many quarters?:"))*0.01
                dimes=int(input("how many dimes?:"))*0.10
                nickles=int(input("how many nickles?:"))*0.05
                pennies=int(input("how many pennies?:"))*0.25
                amount=quaters+dimes+nickles+pennies
                if exchange(amount,choice):
                    brew_coffee(choice)
                    print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                print("Add Resources")
        elif choice=='report':
            report(resources)
        elif choice=="shutdown":
            isOn=False
        elif choice=='add':
            add_resources()
            report(resources)
        else:
            print("Invalid input try again")
        
    

initiate_machine()