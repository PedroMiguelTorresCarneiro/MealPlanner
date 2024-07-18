import random

'''
    Snack options with calories and ingredients (dictionary)
'''
options = [
    {
        "meal": "Iogurte grego com mel e amêndoas", 
        "calories": 178, 
        "ingredients": ["iogurte grego", "mel", "amêndoas"]
    },
    {
        "meal": "Maçã com manteiga de amendoim", 
        "calories": 190, 
        "ingredients": ["maçã", "manteiga de amendoim"]
    },
    {
        "meal": "Cenouras com húmus", 
        "calories": 140, 
        "ingredients": ["cenouras", "húmus"]
    },
    {
        "meal": "Queijo cottage com frutas", 
        "calories": 125, 
        "ingredients": ["queijo cottage", "frutas"]
    },
    {
        "meal": "Biscoitos de arroz com abacate", 
        "calories": 130, 
        "ingredients": ["biscoitos de arroz", "abacate"]
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
