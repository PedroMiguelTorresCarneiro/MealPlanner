import random

'''
    Snack options with calories and ingredients (dictionary)
'''
options = [
    {
        "meal": "Iogurte grego com mel e amêndoas", 
        "calories": 178, 
        "ingredients": [
            {"item": "iogurte grego", "quantity": 200, "unit": "g"},
            {"item": "mel", "quantity": 1, "unit": "colher de sopa"},
            {"item": "amêndoas", "quantity": 30, "unit": "g"}
        ]
    },
    {
        "meal": "Maçã com manteiga de amendoim", 
        "calories": 190, 
        "ingredients": [
            {"item": "maçã", "quantity": 1, "unit": "unidade"},
            {"item": "manteiga de amendoim", "quantity": 2, "unit": "colheres de sopa"}
        ]
    },
    {
        "meal": "Cenouras com húmus", 
        "calories": 140, 
        "ingredients": [
            {"item": "cenouras", "quantity": 100, "unit": "g"},
            {"item": "húmus", "quantity": 50, "unit": "g"}
        ]
    },
    {
        "meal": "Queijo cottage com frutas", 
        "calories": 125, 
        "ingredients": [
            {"item": "queijo cottage", "quantity": 200, "unit": "g"},
            {"item": "frutas", "quantity": 50, "unit": "g"}
        ]
    },
    {
        "meal": "Biscoitos de arroz com abacate", 
        "calories": 130, 
        "ingredients": [
            {"item": "biscoitos de arroz", "quantity": 2, "unit": "unidades"},
            {"item": "abacate", "quantity": 1, "unit": "unidade"}
        ]
    }
]

'''
   Function to get snack
'''
def getSnack():
    snack_choice = random.choice(options)
    return snack_choice

'''
    Test function to get snack
'''
def test_getSnack():
    print("\nTeste de Lanche:")
    snack = getSnack()
    print(snack)
    print("\n")

'''
    Main function
'''
if __name__ == "__main__":
    test_getSnack()
