import random

'''
    Lunch protein options with calories and ingredients (dictionary)
'''
protein_options = [
    {
        "protein": "Peito de Frango", 
        "calories": 165, 
        "ingredients": [{"item": "peito de frango", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Coxas de Frango", 
        "calories": 209, 
        "ingredients": [{"item": "coxas de frango", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Peito de Peru", 
        "calories": 135, 
        "ingredients": [{"item": "peito de peru", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Coxas de Peru", 
        "calories": 213, 
        "ingredients": [{"item": "coxas de peru", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Lombo de Vaca", 
        "calories": 250, 
        "ingredients": [{"item": "lombo de vaca", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Bife de Vaca", 
        "calories": 271, 
        "ingredients": [{"item": "bife de vaca", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Bife de Atum", 
        "calories": 184, 
        "ingredients": [{"item": "bife de atum", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Salmão", 
        "calories": 206, 
        "ingredients": [{"item": "salmão", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Bacalhau", 
        "calories": 82, 
        "ingredients": [{"item": "bacalhau", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Pescada", 
        "calories": 96, 
        "ingredients": [{"item": "pescada", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Dourada", 
        "calories": 82, 
        "ingredients": [{"item": "dourada", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Robalo", 
        "calories": 97, 
        "ingredients": [{"item": "robalo", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Lombo de Porco", 
        "calories": 242, 
        "ingredients": [{"item": "lombo de porco", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Febras de Porco", 
        "calories": 215, 
        "ingredients": [{"item": "febras de porco", "quantity": 200, "unit": "g"}]
    }
]

'''
    Lunch carb options with calories and ingredients (dictionary)
'''
carb_options = [
    {
        "carb": "Arroz Branco", 
        "calories": 130, 
        "ingredients": [{"item": "arroz branco", "quantity": 150, "unit": "g"}]
    },
    {
        "carb": "Massa Integral", 
        "calories": 124, 
        "ingredients": [{"item": "massa integral", "quantity": 150, "unit": "g"}]
    },
    {
        "carb": "Batata Doce", 
        "calories": 112, 
        "ingredients": [{"item": "batata doce", "quantity": 200, "unit": "g"}]
    },
    {
        "carb": "Quinoa", 
        "calories": 120, 
        "ingredients": [{"item": "quinoa", "quantity": 150, "unit": "g"}]
    },
    {
        "carb": "Feijão Preto", 
        "calories": 150, 
        "ingredients": [{"item": "feijão preto", "quantity": 150, "unit": "g"}]
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
        "ingredients": [{"item": "salada", "quantity": 1, "unit": "porção"}] + protein_choice["ingredients"] + carb_choice["ingredients"]
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
