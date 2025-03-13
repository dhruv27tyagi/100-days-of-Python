## Three flavours - espresso , latte and cappucino
## recipe - espresso (50 ml water, 18g coffee), latte (200 ml water, 24g coffee, 150ml milk), cappuccino(250ml water, 24g coffee, 100 ml milk)
## prices - espresso : 1.5$, latte:2.5$, cappucino : 3$
## Resources - 300 ml water, 200 ml milk, 100g coffee
## coin operated - penny(1cent), Dime(10cents), Nickel(5 cents), Quarter(25 cents)

## program req - 1. print report 2. check sufficient resources 3. process coins 4. check transaction successful 5. make coffee

current_resources = {
    "water":300,
    "coffee":100,
    "milk":200,
    "money":5
    }

price = {
    "espresso":1.5,
    "latte":2.5,
    "cappuccino":3
}

recipie = [
    {
        "coffee_type":"espresso",
        "water": 50,
        "coffee":18,
        "milk":0,
    },
    {
        "coffee_type":"latte",
        "water":200,
        "coffee":24,
        "milk":150,
    },
    {
        "coffee_type":"cappuccino",
        "water":250,
        "coffee":24,
        "milk":100,
    }]

def select_recipie(coffee_type):
    selected_recipie = None
    for recipe in recipie:
        if recipe["coffee_type"] == coffee_type:
            selected_recipie = recipe
            break
    return selected_recipie

def espresso():
    resources_required = recipie[0]
    return resources_required

def latte():
    pass

def cappuccino():
    pass

def report():
    print(current_resources)

def check_resources(coffee_type):
    selected_recipe = select_recipie(coffee_type=coffee_type)
    
    if selected_recipe is None:
        print(f"Recipe for {coffee_type} not found.")
        return False
    
    for resource, required in selected_recipe.items():
        if resource == "coffee_type":
            continue  # Skip coffee_type since it's not a resource
        if resource in current_resources:
            if current_resources[resource] < required:
                print(f"Sorry, not enough {resource}.")
                return False
        else:
            print(f"Invalid resource: {resource}.")
            return False
    return True

def update_resources(coffee_type):
    selected_recipe = select_recipie(coffee_type=coffee_type)
    if selected_recipe:
        for resource, required in selected_recipe.items():
            if resource == "coffee_type":
                continue
            current_resources[resource] -= required
        # Update money based on the coffee price
        current_resources["money"] += price[coffee_type]

def transaction(coffee_type):
    update_resources(coffee_type=coffee_type)


machine_On = True
while machine_On:
    coffee_type = input("What would you like? (espresso/latte/capppuccino): ").lower()

    if coffee_type in ["espresso", "latte", "cappuccino"]:
        if check_resources(coffee_type=coffee_type):
            transaction(coffee_type=coffee_type)
    elif coffee_type == "off":
        machine_On = False
        print("Turning off the coffee machine.")
    elif coffee_type == "report":
        report()
    else:
        print("Invalid input. Please choose 'espresso', 'latte', or 'cappuccino'.")