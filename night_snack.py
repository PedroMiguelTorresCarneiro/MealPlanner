import random

'''
    Night snack options with calories and ingredients (dictionary)
'''
options = [
    {
        "meal": "1 ovo cozido + 1/2 abacate", 
        "calories": 180, 
        "ingredients": [
            {"item": "ovo", "quantity": 1, "unit": "unidade"},
            {"item": "abacate", "quantity": 0.5, "unit": "unidade"}
        ]
    },
    {
        "meal": "Palitos de cenoura e pepino com guacamole", 
        "calories": 150, 
        "ingredients": [
            {"item": "cenoura", "quantity": 100, "unit": "g"},
            {"item": "pepino", "quantity": 100, "unit": "g"},
            {"item": "guacamole", "quantity": 50, "unit": "g"}
        ]
    },
    {
        "meal": "1 iogurte grego natural sem açúcar", 
        "calories": 100, 
        "ingredients": [
            {"item": "iogurte grego", "quantity": 200, "unit": "g"}
        ]
    },
    {
        "meal": "Biscoitos de arroz com húmus", 
        "calories": 140, 
        "ingredients": [
            {"item": "biscoitos de arroz", "quantity": 2, "unit": "unidades"},
            {"item": "húmus", "quantity": 50, "unit": "g"}
        ]
    },
    {
        "meal": "Queijo cottage com frutas", 
        "calories": 150, 
        "ingredients": [
            {"item": "queijo cottage", "quantity": 200, "unit": "g"},
            {"item": "frutas", "quantity": 50, "unit": "g"}
        ]
    }
]

'''
   Function to get night snack
'''
def getNightSnack():
    night_snack_choice = random.choice(options)
    return night_snack_choice

'''
    Test function to get night snack
'''
def test_getNightSnack():
    print("\nTeste de Lanche Noturno:")
    night_snack = getNightSnack()
    print(night_snack)
    print("\n")

'''
    Main function
'''
if __name__ == "__main__":
    test_getNightSnack()
