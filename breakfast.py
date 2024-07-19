import random

'''
    Breakfast options with calories and ingredients (dictionary)
'''
options = [
    {
        "meal": "Ovos estrelados com pão e fiambre", 
        "calories": 473, 
        "ingredients": [
            {"item": "ovos", "quantity": 2, "unit": "unidade"},
            {"item": "pão", "quantity": 1, "unit": "unidade"},
            {"item": "fiambre", "quantity": 4, "unit": "fatia"},
            {"item": "azeite", "quantity": 7, "unit": "g"}
        ]
    },
    {
        "meal": "Panquecas de proteina com iogurte natural e fruta", 
        "calories": 358, 
        "ingredients": [
            {"item": "panquecas", "quantity": 50, "unit": "g"},
            {"item": "fruta", "quantity": 1, "unit": "unidade"},
            {"item": "iogurte natural", "quantity": 60, "unit": "g"},
            {"item": "pasta proteica de chocolate", "quantity": 10, "unit": "g"}
        ]
    },
    {
        "meal": "Papas de aveia com fruta e cacau", 
        "calories": 257, 
        "ingredients": [
            {"item": "aveia", "quantity": 25, "unit": "g"},
            {"item": "fruta", "quantity": 1, "unit": "unidade"},
            {"item": "leite magro/aveia", "quantity": 80, "unit": "ml"},
            {"item": "pasta proteica de chocolate", "quantity": 10, "unit": "g"}
        ]
    },
    {
        "meal": "Pão torrado com manteiga e fiambre", 
        "calories": 247, 
        "ingredients": [
            {"item": "pão", "quantity": 1, "unit": "unidade"},
            {"item": "manteiga", "quantity": 10, "unit": "g"},
            {"item": "fiambre", "quantity": 2, "unit": "fatia"}
        ]
    }
]

'''
   Function to get breakfast
'''
def getBreakfast(alwaysCoffee=True):
    meal = random.choice(options)
    
    if alwaysCoffee:
        return {
            "meal": f"Café + {meal['meal']}",
            "calories": meal["calories"],  # Assuming coffee adds 0 calories
            "ingredients": [{"item": "café", "quantity": 3, "unit": "g"}] + meal["ingredients"]
        }
    else:
        return meal

'''
    Test function to get breakfast
'''
def test_getBreakfast():
    print("\nTeste com alwaysCoffee=True:")
    breakfast_with_coffee = getBreakfast(alwaysCoffee=True)
    print(breakfast_with_coffee)
    
    print("\nTeste com alwaysCoffee=False:")
    breakfast_without_coffee = getBreakfast(alwaysCoffee=False)
    print(breakfast_without_coffee)
    print("\n")

'''
    Main function
'''
if __name__ == "__main__":
    test_getBreakfast()
