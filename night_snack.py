import random

'''
    Night snack options with calories and ingredients (dictionary)
'''
options = [
    {
        "meal": "1 ovo cozido + 1/2 abacate", 
        "calories": 180, 
        "ingredients": ["ovo", "abacate"]
    },
    {
        "meal": "Palitos de cenoura e pepino com guacamole", 
        "calories": 150, 
        "ingredients": ["cenoura", "pepino", "guacamole"]
    },
    {
        "meal": "1 iogurte grego natural sem açúcar", 
        "calories": 100, 
        "ingredients": ["iogurte grego"]
    },
    {
        "meal": "Biscoitos de arroz com húmus", 
        "calories": 140, 
        "ingredients": ["biscoitos de arroz", "húmus"]
    },
    {
        "meal": "Queijo cottage com frutas", 
        "calories": 150, 
        "ingredients": ["queijo cottage", "frutas"]
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
