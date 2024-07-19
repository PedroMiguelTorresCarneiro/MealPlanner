import random

'''
    Night snack options with calories and ingredients (dictionary)
'''
options = [
    {
        "meal": "1 ovo cozido + fiambre", 
        "calories": 110, 
        "ingredients": [
            {"item": "ovo", "quantity": 1, "unit": "unidade"},
            {"item": "fiambre", "quantity": 2, "unit": "fatia"}
        ]
    },
    {
        "meal": "Iogurte natural com manteiga de amendoim", 
        "calories": 132, 
        "ingredients": [
            {"item": "iogurte natural", "quantity": 120, "unit": "g"},
            {"item": "manteiga de amendoim", "quantity": 10, "unit": "g"}
        ]
    },
    {
        "meal": "Queijo fresco com doce de nmorango 0% açúcares", 
        "calories": 122, 
        "ingredients": [
            {"item": "queijo fresco", "quantity": 1, "unit": "unidade"},
            {"item": "doce de morango 0%", "quantity": 20, "unit": "g"}
        ]
    },
    {
        "meal": "Queijo com marmelada", 
        "calories": 193, 
        "ingredients": [
            {"item": "queijo", "quantity": 1, "unit": "fatia"},
            {"item": "marmelada", "quantity": 1, "unit": "fatia"}
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
