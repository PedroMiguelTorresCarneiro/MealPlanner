from collections import defaultdict

'''
    Function to generate a shopping list from a weekly meal plan and number of people
'''
def generate_shopping_list(weekly_meals, num_people=1):
    shopping_list = defaultdict(lambda: defaultdict(int))
    
    for day, meals in weekly_meals.items():
        for meal in meals.values():
            for ingredient in meal['ingredients']:
                item = ingredient['item']
                quantity = ingredient['quantity'] * num_people
                unit = ingredient['unit']
                shopping_list[item][unit] += quantity
    
    return shopping_list

'''
    Function to save shopping list to a file (default filename is shopping_list.txt)
'''
def save_shopping_list(shopping_list, filename="shopping_list.txt"):
    with open(filename, 'w') as file:
        for item, quantities in shopping_list.items():
            for unit, quantity in quantities.items():
                file.write(f"{item}: {quantity} {unit}\n")
