Data = {
        "espresso" : {
            "Ingredients":{
                    "water" : 50,
                    "coffee": 18
                           },
                "cost":1.5
            },
        "lattee":{
                  "Ingredients":{
                      "water" : 200,
                      "coffee" : 24,
                      "milk" : 150},
                      "cost":2.5
                    },
        "cappuccino": {
                        "Ingredients":{
                            "water": 250,
                            "coffee":24,
                            "milk":100},
                            "cost":3.0
                        },
        "resources": {
                        "water": 300,
                        "coffee":100,
                        "milk":200,
                        "money": 0
                      }
        }

def calculate(quarter,dime,nickel,pennies):
    """
    Docstring for calculate
    
    :param quarter: Description
    :param dime: Description
    :param nickel: Description
    :param pennies: Description
    """
    total = quarter * 0.25
    total += dime * 0.10
    total += nickel * 0.05
    total += pennies * 0.01
    
    return float(format(total,".2f"))

#returns the change amount 
def change(m,user_input):
    cost = Data[user_input]["cost"] 
    if m == cost:
        Data["resources"]["money"] += m
        return f"Here enjoy your {user_input}!"
    elif m > cost:
        n = m - cost
        Data["resources"]["money"] += m
        return f"Here is ${n:.2f} in change"
    
#makes espressoo    
def make_espresso(i):
    Data["resources"]["water"] -= Data[i]["Ingredients"]["water"]
    Data["resources"]["coffee"] -= Data[i]["Ingredients"]["coffee"]
#makes lattee or cappauccino
def make_lattee_or_cappuccino(i):
    Data["resources"]["water"] -= Data[i]["Ingredients"]["water"]
    Data["resources"]["coffee"] -= Data[i]["Ingredients"]["coffee"]
    Data["resources"]["milk"] -= Data[i]["Ingredients"]["milk"]

#Checks whether the resources are sufficient or not
def is_resource_suffcient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= Data["resources"][item]:
            print(f"Sorry ther is not enough {item}")
            return True
        else:
            return False

#returns report of the resources
def report():
    return Data["resources"]

#----------------------Main function---------------------------#
def coffee_machine():
    turn_off = False

    while not turn_off:
        milk = Data["resources"]["milk"]
        water  = Data["resources"]["water"]
        coffee = Data["resources"]["coffee"]

        user_input = input("what would you like ? (espresso,lattee,cappuccino) ")
        if user_input == "report":
            print(report())
            continue

        elif user_input == "off":
            turn_off = True
            break

        elif is_resource_suffcient(Data[user_input]["Ingredients"]):
            break
        
        quarter = int(input("How many quarters ? "))
        dime = int(input("How many dimes ? "))
        nickel = int(input("How many nickels ? "))
        pennies = int(input("How many pennies ? "))

        result = calculate(quarter,dime,nickel,pennies)

        if result < Data[user_input]["cost"]:
            print("Sorry that's not enough money. Money refunded")
        else:
            print(change(result,user_input))
            if user_input == "espresso":
                make_espresso(user_input)
            elif user_input == "lattee":
                make_lattee_or_cappuccino(user_input)
            else:
                make_lattee_or_cappuccino(user_input)

coffee_machine()