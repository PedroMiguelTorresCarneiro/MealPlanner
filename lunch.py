import random

'''
    Lunch protein options with calories and ingredients (dictionary)
'''
protein_options = [
    {
        "protein": "Peito de Frango", 
        "calories": 220, 
        "ingredients": [{"item": "peito de frango", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Carne picada de frango e chouriço", 
        "calories": 280, 
        "ingredients": [{"item": "carne picada com chouriço", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Coxas de Frango", 
        "calories": 220, 
        "ingredients": [{"item": "coxas de frango", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Bifes de Peru", 
        "calories": 220, 
        "ingredients": [{"item": "peito de peru", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Bife de Vaca", 
        "calories": 384, 
        "ingredients": [{"item": "bife de vaca", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Bife de Atum", 
        "calories": 262, 
        "ingredients": [{"item": "bife de atum", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Salmão", 
        "calories": 398, 
        "ingredients": [{"item": "salmão", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Bacalhau", 
        "calories": 190, 
        "ingredients": [{"item": "bacalhau", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Pescada", 
        "calories": 176, 
        "ingredients": [{"item": "pescada", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Dourada", 
        "calories": 190, 
        "ingredients": [{"item": "dourada", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Lulas", 
        "calories": 170, 
        "ingredients": [{"item": "robalo", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Lombo de Porco", 
        "calories": 298, 
        "ingredients": [{"item": "lombo de porco", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Febras de Porco", 
        "calories": 290, 
        "ingredients": [{"item": "febras de porco", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Rojões de Porco", 
        "calories": 360, 
        "ingredients": [{"item": "febras de porco", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Hamburguer de mistura de carne", 
        "calories": 360, 
        "ingredients": [{"item": "febras de porco", "quantity": 200, "unit": "g"}]
    }

]

'''
    Lunch carb options with calories and ingredients (dictionary)
'''
carb_options = [
    {
        "carb": "Arroz Branco", 
        "calories": 195, 
        "ingredients": [{"item": "arroz branco", "quantity": 150, "unit": "g"}]
    },
    {
        "carb": "Massa", 
        "calories": 186, 
        "ingredients": [{"item": "massa", "quantity": 150, "unit": "g"}]
    },
    {
        "carb": "Batata", 
        "calories": 154, 
        "ingredients": [{"item": "batata doce", "quantity": 200, "unit": "g"}]
    },
    {
        "carb": "Cuscus", 
        "calories": 168, 
        "ingredients": [{"item": "Cuscus", "quantity": 150, "unit": "g"}]
    },
    {
        "carb": "Feijão Preto e arroz branco", 
        "calories": 169, 
        "ingredients": [
            {"item": "feijão preto", "quantity": 60, "unit": "g"},
            {"item": "arroz branco", "quantity": 90, "unit": "g"}
        ]
    },
    {
        "carb": "Puré de batata(saquetas)", 
        "calories": 260, 
        "ingredients": [
            {"item": "puré", "quantity": 1, "unit": "saqueta"},
            {"item": "leite", "quantity": 125, "unit": "ml"}
        ]
    }
    
]

'''
   Function to get lunch
'''
def getLunch():
    protein_choice = random.choice(protein_options)
    carb_choice = random.choice(carb_options)
    return {
        "meal": f"Salada + {protein_choice['protein']} e {carb_choice['carb']}",
        "calories": 150 + protein_choice["calories"] + carb_choice["calories"],  # Assuming salad adds 0 calories
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
