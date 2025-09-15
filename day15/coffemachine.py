#☕
# penny= 1 cent 0.01$  , nickel= 5 cents, dime= 10 cents, quarter= 25 cents 0.25$

MENU= {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffe": 18
        },
        "cost":1.5
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "coffe": 18,
            "milk":150
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "coffe": 24,
            "milk":100
        },
        "cost":3.0

    }
}

resources = {
    "water": 300,
    "coffe":100,
    "milk":200,
    "money":0
}

def payment():
    print("Please insert coins.")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickels=int(input("How many nickels?: "))
    pennies=int(input("How many pennies?: "))
    total= float((quarters* 0.25)+ (dimes*0.1)+(nickels*0.05)+(pennies*0.01))
    return total


while True:
    menu_input= input("What would you like?\n(espresso/latte/cappuccino) or (report/off): ")
    if menu_input== "off":
        exit("Coffe machine is closing...")
    elif menu_input=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffe']}g")
        print(f"Money: ${resources['money']:.2f}")

    elif menu_input == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            if resources["coffe"] >= MENU["espresso"]["ingredients"]["coffe"]:
                total= payment()
                if total == MENU["espresso"]["cost"]:
                    print("Here is your espresso ☕️ Enjoy!")
                    new_money=resources["money"] + MENU["espresso"]["cost"]
                    new_water=resources["water"] - MENU["espresso"]["ingredients"]["water"]
                    new_coffe=resources["coffe"] - MENU["espresso"]["ingredients"]["coffe"]
                    resources.update({"money":new_money ,"water":new_water , "coffe": new_coffe})

                elif total > MENU["espresso"]["cost"]:
                    change=total - MENU["espresso"]["cost"]
                    print("Here is $%.2f change." %change)
                    print("Here is your espresso ☕️ Enjoy!")
                    new_money=resources["money"] + MENU["espresso"]["cost"]
                    new_water=resources["water"] - MENU["espresso"]["ingredients"]["water"]
                    new_coffe=resources["coffe"] - MENU["espresso"]["ingredients"]["coffe"]
                    resources.update({"money":new_money ,"water":new_water , "coffe": new_coffe})
                else:
                    print("Insufficient amount")
                    print("Here is your money back.\nCoffe machine is closing...")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")

    elif menu_input == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
            if resources["coffe"] >= MENU["latte"]["ingredients"]["coffe"]:
                if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                    total= payment()
                    if total == MENU["latte"]["cost"]:
                        print("Here is your latte ☕️ Enjoy!")
                        new_money=resources["money"] + MENU["latte"]["cost"]
                        new_water=resources["water"] - MENU["latte"]["ingredients"]["water"]
                        new_coffe=resources["coffe"] - MENU["latte"]["ingredients"]["coffe"]
                        new_milk=resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                        resources.update({"money":new_money ,"water":new_water , "coffe": new_coffe, "milk":new_milk})

                    elif total > MENU["latte"]["cost"]:
                        change=total - MENU["latte"]["cost"]
                        print("Here is $%.2f change." %change)
                        print("Here is your latte ☕️ Enjoy!")
                        new_money=resources["money"] + MENU["latte"]["cost"]
                        new_water=resources["water"] - MENU["latte"]["ingredients"]["water"]
                        new_coffe=resources["coffe"] - MENU["latte"]["ingredients"]["coffe"]
                        new_milk=resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                        resources.update({"money":new_money ,"water":new_water , "coffe": new_coffe, "milk":new_milk})
                    else:
                        print("Insufficient amount")
                        print("Here is your money back.\nCoffe machine is closing...")
                else:
                    print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")

    elif menu_input == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
            if resources["coffe"] >= MENU["cappuccino"]["ingredients"]["coffe"]:
                if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                    total= payment()
                    if total == MENU["cappuccino"]["cost"]:
                        print("Here is your cappuccino ☕️ Enjoy!")
                        new_money=resources["money"] + MENU["cappuccino"]["cost"]
                        new_water=resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                        new_coffe=resources["coffe"] - MENU["cappuccino"]["ingredients"]["coffe"]
                        new_milk=resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                        resources.update({"money":new_money ,"water":new_water , "coffe": new_coffe, "milk":new_milk})

                    elif total > MENU["cappuccino"]["cost"]:
                        change=total - MENU["cappuccino"]["cost"]
                        print("Here is $%.2f change." %change)
                        print("Here is your cappuccino ☕️ Enjoy!")
                        new_money=resources["money"] + MENU["cappuccino"]["cost"]
                        new_water=resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                        new_coffe=resources["coffe"] - MENU["cappuccino"]["ingredients"]["coffe"]
                        new_milk=resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                        resources.update({"money":new_money ,"water":new_water , "coffe": new_coffe, "milk":new_milk})
                    else:
                        print("Insufficient amount")
                        print("Here is your money back.\nCoffe machine is closing...")
                else:
                    print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    else:
        print("We dont have any %s in here." %menu_input)
