import tkinter as tk
from tkinter import messagebox, simpledialog

# ☕
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
    "money":0.0
}

def payment_dialog(root):
    messagebox.showinfo("Payment", "Please insert coins.")
    try:
        quarters = simpledialog.askinteger("Payment", "How many quarters? (0.25$)", parent=root, minvalue=0, initialvalue=0)
        if quarters is None: return None
        dimes    = simpledialog.askinteger("Payment", "How many dimes? (0.10$)", parent=root, minvalue=0, initialvalue=0)
        if dimes is None: return None
        nickels  = simpledialog.askinteger("Payment", "How many nickels? (0.05$)", parent=root, minvalue=0, initialvalue=0)
        if nickels is None: return None
        pennies  = simpledialog.askinteger("Payment", "How many pennies? (0.01$)", parent=root, minvalue=0, initialvalue=0)
        if pennies is None: return None
    except Exception:
        messagebox.showerror("Error", "Invalid coin input.")
        return None

    total = float((quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01))
    return total

def check_resources(drink):
    need = MENU[drink]["ingredients"]
    # check sequentially and report the first missing item
    if "water" in need and resources["water"] < need["water"]:
        messagebox.showwarning("Resource", "Sorry there is not enough water.")
        return False
    if "coffe" in need and resources["coffe"] < need["coffe"]:
        messagebox.showwarning("Resource", "Sorry there is not enough coffee.")
        return False
    if "milk" in need and resources["milk"] < need["milk"]:
        messagebox.showwarning("Resource", "Sorry there is not enough milk.")
        return False
    return True

def process_order(root, drink):
    # resource check
    if not check_resources(drink):
        return

    # take payment
    total = payment_dialog(root)
    if total is None:
        return  # user canceled

    cost = MENU[drink]["cost"]
    if total < cost:
        messagebox.showinfo("Payment", "Sorry that's not enough money. Money refunded.")
        return

    change = total - cost
    if change > 0:
        messagebox.showinfo("Change", "Here is $%.2f dollars in change." % change)

    # make the coffee: increase cash by cost only
    resources["money"] += cost
    # deduct resources
    need = MENU[drink]["ingredients"]
    if "water" in need: resources["water"] -= need["water"]
    if "coffe" in need: resources["coffe"] -= need["coffe"]
    if "milk"  in need: resources["milk"]  -= need["milk"]

    messagebox.showinfo("Enjoy", f"Here is your {drink} ☕️ Enjoy!")
    update_status_text()

def show_report():
    report_lines = [
        f"Water: {resources['water']}ml",
        f"Milk: {resources['milk']}ml",
        f"Coffee: {resources['coffe']}g",
        f"Money: ${resources['money']:.2f}"
    ]
    messagebox.showinfo("Report", "\n".join(report_lines))

def update_status_text():
    status_var.set(
        f"Water: {resources['water']}ml | "
        f"Milk: {resources['milk']}ml | "
        f"Coffee: {resources['coffe']}g | "
        f"Money: ${resources['money']:.2f}"
    )

def main():
    root = tk.Tk()
    root.title("Coffee Machine")

    global status_var
    status_var = tk.StringVar()

    # Title
    tk.Label(root, text="What would you like? (espresso / latte / cappuccino)").pack(padx=12, pady=(12,6))

    # Drink buttons
    btn_frame = tk.Frame(root)
    btn_frame.pack(padx=12, pady=6)

    tk.Button(btn_frame, text="espresso ($1.50)", width=18,
              command=lambda: process_order(root, "espresso")).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(btn_frame, text="latte ($2.50)", width=18,
              command=lambda: process_order(root, "latte")).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(btn_frame, text="cappuccino ($3.00)", width=18,
              command=lambda: process_order(root, "cappuccino")).grid(row=0, column=2, padx=5, pady=5)

    # Report and Exit
    util_frame = tk.Frame(root)
    util_frame.pack(padx=12, pady=(6,12))
    tk.Button(util_frame, text="report", width=12, command=show_report).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(util_frame, text="off", width=12, command=root.destroy).grid(row=0, column=1, padx=5, pady=5)

    # Status bar
    tk.Label(root, textvariable=status_var, anchor="w").pack(fill="x", padx=12, pady=(0,12))
    update_status_text()

    root.mainloop()

if __name__ == "__main__":
    main()
