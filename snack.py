import random

'''
    Snack options with calories and ingredients (dictionary)
'''
options = [
    {
        "meal": "Iogurte natural com fruta e cornflakes 0%", 
        "calories": 222, 
        "ingredients": [
            {"item": "iogurte grego", "quantity": 125, "unit": "g"},
            {"item": "fruta", "quantity": 1, "unit": "unidade"},
            {"item": "cornflakes 0%", "quantity": 20, "unit": "g"}
        ]
    },
    {
        "meal": "Maçã com manteiga de amendoim", 
        "calories": 264, 
        "ingredients": [
            {"item": "maçã", "quantity": 1, "unit": "unidade"},
            {"item": "manteiga de amendoim", "quantity": 32, "unit": "g"}
        ]
    },
    {
        "meal": "Queijo com marmelada", 
        "calories": 193, 
        "ingredients": [
            {"item": "queijo", "quantity": 1, "unit": "fatia"},
            {"item": "marmelada", "quantity": 1, "unit": "fatia"}
        ]
    },
    {
        "meal": "Tostas com queijinho de barrar e fiambre + leite proteico", 
        "calories": 260, 
        "ingredients": [
            {"item": "tostas", "quantity": 4, "unit": "unidade"},
            {"item": "queijinho de barrar", "quantity": 1, "unit": "unidade"},
            {"item": "fiambre", "quantity": 4, "unit": "fatia"},
            {"item": "leite proteico", "quantity": 250, "unit": "g"}
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
