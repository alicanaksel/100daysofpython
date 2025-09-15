# --------------------------------------------
# Coffee Machine (OOP version)
# Classes and methods follow the provided spec:
# - MenuItem, Menu, CoffeeMaker, MoneyMachine
# English comments included throughout.
# --------------------------------------------

from dataclasses import dataclass
from typing import Dict, Optional


# ----------------------------
# Domain Model: MenuItem
# ----------------------------
@dataclass
class MenuItem:
    """
    Represents a single drink on the menu.
    name: display name of the drink (e.g., "latte")
    cost: price in dollars (float)
    ingredients: mapping of resource name -> amount required
                 e.g., {"water": 200, "coffee": 18, "milk": 150}
    """
    name: str
    cost: float
    ingredients: Dict[str, int]


# ----------------------------
# Menu: holds available drinks
# ----------------------------
class Menu:
    """
    Holds a list of MenuItem objects and provides:
    - get_items(): returns "espresso/latte/cappuccino"
    - find_drink(order_name): returns the MenuItem or None
    """

    def __init__(self):
        # Build items exactly like the original dict
        self.menu = [
            MenuItem(
                name="espresso",
                cost=1.5,
                ingredients={"water": 50, "coffee": 18}
            ),
            MenuItem(
                name="latte",
                cost=2.5,
                ingredients={"water": 200, "coffee": 18, "milk": 150}
            ),
            MenuItem(
                name="cappuccino",
                cost=3.0,
                ingredients={"water": 250, "coffee": 24, "milk": 100}
            ),
        ]

    def get_items(self) -> str:
        """Return a slash-separated list of drink names (e.g., 'latte/espresso/cappuccino')."""
        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name: str) -> Optional[MenuItem]:
        """
        Lookup a drink by its name and return the MenuItem if it exists.
        If not found, return None.
        """
        order_name = order_name.strip().lower()
        for item in self.menu:
            if item.name == order_name:
                return item
        return None


# ----------------------------
# CoffeeMaker: manages resources
# ----------------------------
class CoffeeMaker:
    """
    Manages machine resources and brewing.
    - report(): prints remaining resources
    - is_resource_sufficient(drink): True if enough; prints message if not
    - make_coffee(order): deducts resources and prints a success message
    """

    def __init__(self):
        # Start with the same initial resources as the original script
        self.resources = {
            "water": 300,   # in ml
            "coffee": 100,  # in g
            "milk": 200     # in ml
        }

    def report(self) -> None:
        """Print the current resource levels."""
        print(f"Water: {self.resources.get('water', 0)}ml")
        print(f"Milk: {self.resources.get('milk', 0)}ml")
        print(f"Coffee: {self.resources.get('coffee', 0)}g")

    def is_resource_sufficient(self, drink: MenuItem) -> bool:
        """
        Check if resources suffice for the chosen drink.
        If insufficient, print a message and return False.
        """
        for ingredient, required in drink.ingredients.items():
            if self.resources.get(ingredient, 0) < required:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def make_coffee(self, order: MenuItem) -> None:
        """
        Deduct the required ingredients from the resources.
        Print a confirmation once done.
        """
        for ingredient, required in order.ingredients.items():
            self.resources[ingredient] -= required
        print(f"Here is your {order.name} ☕️ Enjoy!")


# ----------------------------
# MoneyMachine: handles coins & profit
# ----------------------------
class MoneyMachine:
    """
    Tracks profit and processes coin payments.
    - report(): prints total profit
    - make_payment(cost): prompts for coins, returns True if enough
                          and provides change if needed
    """

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self.profit = 0.0

    def report(self) -> None:
        """Print the current profit."""
        print(f"Money: ${self.profit:.2f}")

    def _process_coins(self) -> float:
        """
        Ask the user to insert coins and compute the total value.
        Returns the total in dollars as a float.
        """
        print("Please insert coins.")
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
        except ValueError:
            print("Invalid input. Treating as 0 coins.")
            quarters = dimes = nickels = pennies = 0

        total = (
            quarters * self.COIN_VALUES["quarters"]
            + dimes * self.COIN_VALUES["dimes"]
            + nickels * self.COIN_VALUES["nickels"]
            + pennies * self.COIN_VALUES["pennies"]
        )
        return float(total)

    def make_payment(self, cost: float) -> bool:
        """
        Request coins from the user and determine if payment is sufficient.
        - If equal: accept and add to profit.
        - If more: accept, add cost to profit, return change.
        - If less: reject and return False.
        """
        total_inserted = self._process_coins()

        if total_inserted < cost:
            print("Insufficient amount.")
            print("Here is your money back.")
            return False

        # Accept payment
        self.profit += cost

        change = total_inserted - cost
        if change > 0:
            print("Here is $%.2f change." % change)

        return True


# ----------------------------
# App Loop
# ----------------------------
def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        choice = input(
            f"What would you like? ({menu.get_items()}) or (report/off): "
        ).strip().lower()

        if choice == "off":
            print("Coffee machine is closing...")
            break

        if choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        # Find the drink in the menu
        drink = menu.find_drink(choice)
        if drink is None:
            print(f"We don't have any '{choice}'.")
            continue

        # Check resources first
        if not coffee_maker.is_resource_sufficient(drink):
            # If not sufficient, skip to next loop iteration
            continue

        # Process payment; if successful, make coffee
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
