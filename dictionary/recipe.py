recipe = {
    "title": "cake recipe" ,
    "number_of_orders": 5 ,
    "is_vegan": True ,
    "ingredients": ['salt', 'sugar', 'chocklet', 'eggs']
}

def add_ingredients(recipe, ing_to_add):
    recipe["ingredients"].append(ing_to_add)
    print(recipe["ingredients"])

def del_ingredients(recipe, ing_to_del):
    recipe["ingredients"].remove(ing_to_del)
    print(recipe["ingredients"])

def add_orders (recipe, add_order):
    current_orders = int(recipe["number_of_orders"])
    updated_orders = current_orders + add_order
    recipe ["number_of_orders"] = updated_orders
    print (recipe ["number_of_orders"])

def print_recipe (recipe):
    print (f"this is my favorit recipe: {recipe["title"]}")
    if recipe["is_vegan"]:
        print ("the dish is vegan.")
    else: print ("the dish is non vegan.")
    print (f"ingrediants: {recipe ["ingredients"]}")

add_orders(recipe, 5)
add_ingredients(recipe , "cinnamon")
print ()
print_recipe(recipe)