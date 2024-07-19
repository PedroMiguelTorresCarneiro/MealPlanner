import random

'''
    Dinner protein options with calories and ingredients (dictionary)
'''
protein_options = [
    {
        "protein": "Peito de Frango", 
        "calories": 220, 
        "ingredients": [{"item": "peito de frango", "quantity": 200, "unit": "g"}]
    },
    {
        "protein": "Bifes de Peru", 
        "calories": 220, 
        "ingredients": [{"item": "peito de peru", "quantity": 200, "unit": "g"}]
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
        "protein": "Carne picada de frango e chouriço", 
        "calories": 280, 
        "ingredients": [{"item": "carne picada com chouriço", "quantity": 200, "unit": "g"}]
    }
]

'''
    Dinner carb options with calories and ingredients (dictionary)
'''
carb_options = [
    {
        "carb": "Fruta", 
        "calories": 80, 
        "ingredients": [{"item": "fruta", "quantity": 1, "unit": "unidade"}]
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
                {"item": "cenoura", "quantity": 2, "unit": "unidade"},
                {"item": "couve-flor congelada", "quantity": 250, "unit": "g"},
                {"item": "cebola", "quantity": 1, "unit": "unidade"},
                {"item": "courgette", "quantity": 0.5, "unit": "unidade"},
                {"item": "brócolos congelados", "quantity": 250, "unit": "g"}
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
