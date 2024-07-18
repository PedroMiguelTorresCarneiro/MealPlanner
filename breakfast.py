import random

'''
    Breakfast options with calories and ingredients (dictionary)
'''
options = [
    {
        "meal": "Omelete de 3 ovos com espinafres, cogumelos e queijo feta", 
        "calories": 223, 
        "ingredients": ["3 ovos", "espinafres", "cogumelos", "queijo feta"]
    },
    {
        "meal": "Batido de espinafres, abacate, iogurte grego e proteína em pó", 
        "calories": 213, 
        "ingredients": ["espinafres", "abacate", "iogurte grego", "proteína em pó"]
    },
    {
        "meal": "Iogurte grego com frutos vermelhos e sementes de chia", 
        "calories": 190, 
        "ingredients": ["iogurte grego", "frutos vermelhos", "sementes de chia"]
    },
    {
        "meal": "Torrada de abacate com ovo escalfado", 
        "calories": 260, 
        "ingredients": ["abacate", "ovo", "pão"]
    },
    {
        "meal": "Papas de aveia com morangos fatiados", 
        "calories": 196, 
        "ingredients": ["aveia", "morangos"]
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
        "calories": meal["calories"] ,  # Assuming coffee adds 0 calories
        "ingredients": ["café"] + meal["ingredients"] 
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
