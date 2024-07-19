import random

'''
    Dinner protein options with calories and ingredients (dictionary)
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
    Dinner carb options with calories and ingredients (dictionary)
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
   Function to get dinner
'''
def getDinner(includeSoup=True):
    protein_choice = random.choice(protein_options)
    carb_choice = random.choice(carb_options)
    
    if includeSoup:
        return {
            "meal": f"Sopa + {protein_choice['protein']} com {carb_choice['carb']}",
            "calories": 100 + protein_choice["calories"] + carb_choice["calories"],  # Assuming soup adds 100 calories
            "ingredients": [
                {"item": "cenoura", "quantity": 100, "unit": "g"},
                {"item": "couve-flor", "quantity": 100, "unit": "g"},
                {"item": "cebola", "quantity": 50, "unit": "g"},
                {"item": "courgete", "quantity": 100, "unit": "g"},
                {"item": "brócolos", "quantity": 100, "unit": "g"}
            ] + protein_choice["ingredients"] + carb_choice["ingredients"]
        }
    else:
        return {
            "meal": f"{protein_choice['protein']} com {carb_choice['carb']}",
            "calories": protein_choice["calories"] + carb_choice["calories"],
            "ingredients": protein_choice["ingredients"] + carb_choice["ingredients"]
        }

'''
    Test function to get dinner
'''
def test_getDinner():
    print("\nTeste de Jantar com Sopa:")
    dinner_with_soup = getDinner(includeSoup=True)
    print(dinner_with_soup)
    
    print("\nTeste de Jantar sem Sopa:")
    dinner_without_soup = getDinner(includeSoup=False)
    print(dinner_without_soup)
    print("\n")

'''
    Main function
'''
if __name__ == "__main__":
    test_getDinner()
