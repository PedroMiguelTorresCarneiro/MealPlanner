import random

'''
    Breakfast options with calories and ingredients (dictionary)
'''
options = [
    {
        "meal": "Omelete de 3 ovos com espinafres, cogumelos e queijo feta", 
        "calories": 223, 
        "ingredients": [
            {"item": "ovos", "quantity": 3, "unit": "unidades"},
            {"item": "espinafres", "quantity": 50, "unit": "g"},
            {"item": "cogumelos", "quantity": 50, "unit": "g"},
            {"item": "queijo feta", "quantity": 30, "unit": "g"}
        ]
    },
    {
        "meal": "Batido de espinafres, abacate, iogurte grego e proteína em pó", 
        "calories": 213, 
        "ingredients": [
            {"item": "espinafres", "quantity": 50, "unit": "g"},
            {"item": "abacate", "quantity": 1, "unit": "unidade"},
            {"item": "iogurte grego", "quantity": 200, "unit": "g"},
            {"item": "proteína em pó", "quantity": 30, "unit": "g"}
        ]
    },
    {
        "meal": "Iogurte grego com frutos vermelhos e sementes de chia", 
        "calories": 190, 
        "ingredients": [
            {"item": "iogurte grego", "quantity": 200, "unit": "g"},
            {"item": "frutos vermelhos", "quantity": 50, "unit": "g"},
            {"item": "sementes de chia", "quantity": 10, "unit": "g"}
        ]
    },
    {
        "meal": "Torrada de abacate com ovo escalfado", 
        "calories": 260, 
        "ingredients": [
            {"item": "abacate", "quantity": 1, "unit": "unidade"},
            {"item": "ovo", "quantity": 1, "unit": "unidade"},
            {"item": "pão", "quantity": 2, "unit": "fatias"}
        ]
    },
    {
        "meal": "Papas de aveia com morangos fatiados", 
        "calories": 196, 
        "ingredients": [
            {"item": "aveia", "quantity": 50, "unit": "g"},
            {"item": "morangos", "quantity": 100, "unit": "g"}
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
            "ingredients": [{"item": "café", "quantity": 1, "unit": "xícara"}] + meal["ingredients"]
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
