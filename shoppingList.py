from collections import defaultdict

'''
    Lists of ingredient categories
'''
proteinas = [
    "frango", "peru", "vaca", "porco", "atum", "salmão", "bacalhau", 
    "pescada", "dourada", "robalo", "carneiro", "cabrito", "cordeiro", 
    "pato", "coelho", "javali", "veado", "alheira", "chouriço", "salsicha", 
    "fiambre", "presunto", "lulas", "polvo", "chocos", "camarão", "lagosta", 
    "lagostim", "sardinha", "carapau", "truta", "espadarte", "linguado", 
    "maruca", "raia", "garoupa", "mero", "anchova", "cavala", "tilápia", 
    "solha", "enguia"
]

hidratos = [
    "arroz", "massa", "batata", "quinoa", "feijão", "pão", "cuscuz", "lentilhas", "grão-de-bico",
    "milho", "batata-doce", "farinha", "cevada", "trigo", "aveia", "tapioca", "mandioca", 
    "amido de milho", "farro", "espelta", "sorgo", "inhame", "polenta", "ervilhas", "pasta",
    "bulgur", "arroz integral", "arroz selvagem", "batata-inglesa", "batata-rena", "batata-palha"
]

laticinios = [
    "iogurte", "queijo", "cottage", "leite", "manteiga", "nata", "creme de leite", 
    "requeijão", "queijo fresco", "queijo flamengo", "queijo de cabra", 
    "queijo de ovelha", "queijo de vaca", "queijo da serra", "parmesão", 
    "mozzarella", "cheddar", "brie", "camembert", 
    "gorgonzola", "queijo azul", "ricota", "mascarpone", 
    "feta", "gouda", "edam", "emmental", 
    "roquefort", "gruyère"
]

frutas = [
    "abacate", "maçã", "frutas", "morangos", "banana", "laranja", 
    "pera", "ananás", "manga", "kiwi", "melancia", "melão", "ameixa", 
    "pêssego", "nectarina", "cereja", "uvas", "framboesas", 
    "amoras", "mirtilos", "tangerina", "limão", "lima", "maracujá", 
    "papaia", "figo", "damasco", "toranja", "groselha", "goiaba", 
    "cajú", "caqui", "carambola", "physalis"
    ]

legumes = [
    "espinafres", "cogumelos", "cenouras", "brócolos", "pepino", "cebola", 
    "courgete", "húmus", "guacamole", "salada", "alface", "tomate", 
    "pimento", "batata", "batata-doce", "beterraba", "abóbora", "espargos", 
    "feijão-verde", "ervilhas", "milho", "nabo", "alho-francês", "aipo", 
    "rabanete", "escarola", "endívia", "chuchu", "grelos", "rúcula", 
    "agrião", "couve", "couve-flor", "couve-de-bruxelas", "couve-roxa", 
    "rabanete", "alcachofra", "beringela", "funcho", "nabos", "alho"
]

frutos_secos = [
    "nozes",
    "amendoins",
    "amêndoas",
    "avelãs",
    "castanhas-do-pará",
    "castanhas de caju",
    "pistácios",
    "macadâmias",
    "pinhões",
    "castanhas"
]



'''
    Function to categorize ingredient based on its name
'''
def categorize_ingredient(item):
    if any(keyword in item for keyword in proteinas):
        return "Proteína"
    elif any(keyword in item for keyword in hidratos):
        return "hidratos"
    elif any(keyword in item for keyword in laticinios):
        return "Laticínios"
    elif any(keyword in item for keyword in frutas):
        return "Frutas"
    elif any(keyword in item for keyword in legumes):
        return "Legumes"
    elif any(keyword in item for keyword in frutos_secos):
        return "Frutos Secos"
    else:
        return "Outros"
def generate_shopping_list(weekly_meals, num_people=1):
    shopping_list = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    
    for day, meals in weekly_meals.items():
        for meal in meals.values():
            for ingredient in meal['ingredients']:
                item = ingredient['item']
                quantity = ingredient['quantity'] * num_people
                unit = ingredient['unit']
                category = categorize_ingredient(item)
                shopping_list[category][item][unit] += quantity
    
    return shopping_list

def save_shopping_list(shopping_list, filename="shopping_list.txt"):
    with open(filename, 'w') as file:
        for category, items in shopping_list.items():
            file.write(f"\n------------------------------------[ {category} ]\n")
            for item, quantities in items.items():
                for unit, quantity in quantities.items():
                    file.write(f" - {item}: {quantity} {unit} ,\n")

'''
    Test function to generate and save shopping list
'''
def test_generate_and_save_shopping_list():
    # Exemplo de dados de refeições semanais para teste
    example_weekly_meals = {
        "Segunda": {
            "Pequeno-Almoço": {
                "meal": "Café + Omelete de 3 ovos com espinafres, cogumelos e queijo feta",
                "calories": 223,
                "ingredients": [
                    {"item": "café", "quantity": 1, "unit": "xícara"},
                    {"item": "ovos", "quantity": 3, "unit": "unidades"},
                    {"item": "espinafres", "quantity": 50, "unit": "g"},
                    {"item": "cogumelos", "quantity": 50, "unit": "g"},
                    {"item": "queijo feta", "quantity": 30, "unit": "g"}
                ]
            },
            "Lanche da Manhã": {
                "meal": "Iogurte grego com mel e amêndoas",
                "calories": 178,
                "ingredients": [
                    {"item": "iogurte grego", "quantity": 200, "unit": "g"},
                    {"item": "mel", "quantity": 1, "unit": "colher de sopa"},
                    {"item": "amêndoas", "quantity": 30, "unit": "g"}
                ]
            }
        }
    }

    num_people = 2  # Número de pessoas para o plano de refeições
    shopping_list = generate_shopping_list(example_weekly_meals, num_people)
    save_shopping_list(shopping_list)
    print("\nLista de compras gerada:")
    for category, items in shopping_list.items():
        print(f"\n------------------------------------[ {category} ]")
        for item, quantities in items.items():
            for unit, quantity in quantities.items():
                print(f"- {item}: {quantity} {unit} ,")

'''
    Main function
'''
if __name__ == "__main__":
    test_generate_and_save_shopping_list()
