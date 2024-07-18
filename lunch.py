import random

'''
    Lunch protein options with calories and ingredients (dictionary)
'''
protein_options = [
    {
        "protein": "Peito de Frango", 
        "calories": 165, 
        "ingredients": ["peito de frango"]
    },
    {
        "protein": "Coxas de Frango", 
        "calories": 209, 
        "ingredients": ["coxas de frango"]
    },
    {
        "protein": "Peito de Peru", 
        "calories": 135, 
        "ingredients": ["peito de peru"]
    },
    {
        "protein": "Coxas de Peru", 
        "calories": 213, 
        "ingredients": ["coxas de peru"]
    },
    {
        "protein": "Lombo de Vaca", 
        "calories": 250, 
        "ingredients": ["lombo de vaca"]
    },
    {
        "protein": "Bife de Vaca", 
        "calories": 271, 
        "ingredients": ["bife de vaca"]
    },
    {
        "protein": "Bife de Atum", 
        "calories": 184, 
        "ingredients": ["bife de atum"]
    },
    {
        "protein": "Salmão", 
        "calories": 206, 
        "ingredients": ["salmão"]
    },
    {
        "protein": "Bacalhau", 
        "calories": 82, 
        "ingredients": ["bacalhau"]
    },
    {
        "protein": "Pescada", 
        "calories": 96, 
        "ingredients": ["pescada"]
    },
    {
        "protein": "Dourada", 
        "calories": 82, 
        "ingredients": ["dourada"]
    },
    {
        "protein": "Robalo", 
        "calories": 97, 
        "ingredients": ["robalo"]
    },
    {
        "protein": "Lombo de Porco", 
        "calories": 242, 
        "ingredients": ["lombo de porco"]
    },
    {
        "protein": "Febras de Porco", 
        "calories": 215, 
        "ingredients": ["febras de porco"]
    }
]

'''
    Lunch carb options with calories and ingredients (dictionary)
'''
carb_options = [
    {
        "carb": "Arroz Branco", 
        "calories": 130, 
        "ingredients": ["arroz branco"]
    },
    {
        "carb": "Massa Integral", 
        "calories": 124, 
        "ingredients": ["massa integral"]
    },
    {
        "carb": "Batata Doce", 
        "calories": 112, 
        "ingredients": ["batata doce"]
    },
    {
        "carb": "Quinoa", 
        "calories": 120, 
        "ingredients": ["quinoa"]
    },
    {
        "carb": "Feijão Preto", 
        "calories": 150, 
        "ingredients": ["feijão preto"]
    }
]

'''
   Function to get lunch
'''
def getLunch():
    protein_choice = random.choice(protein_options)
    carb_choice = random.choice(carb_options)
    return {
        "meal": f"Salada com {protein_choice['protein']} e {carb_choice['carb']}",
        "calories": 0 + protein_choice["calories"] + carb_choice["calories"],  # Assuming salad adds 0 calories
        "ingredients": ["salada"] + protein_choice["ingredients"] + carb_choice["ingredients"]
    }

'''
    Test function to get lunch
'''
def test_getLunch():
    print("\nTeste de Almoço:")
    lunch = getLunch()
    print(lunch)
    print("\n")

'''
    Main function
'''
if __name__ == "__main__":
    test_getLunch()
