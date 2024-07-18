import random

'''
    Dinner protein options with calories and ingredients (dictionary)
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
    Dinner carb options with calories and ingredients (dictionary)
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
   Function to get dinner
'''
def getDinner(includeSoup=True):
    protein_choice = random.choice(protein_options)
    carb_choice = random.choice(carb_options)
    
    if includeSoup:
        return {
            "meal": f"Sopa + {protein_choice['protein']} com {carb_choice['carb']}",
            "calories": 100 + protein_choice["calories"] + carb_choice["calories"],  # Assuming soup adds 100 calories
            "ingredients": ["cenoura", "couve-flor", "cebola", "courgete", "bróculos"] + protein_choice["ingredients"] + carb_choice["ingredients"]
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
