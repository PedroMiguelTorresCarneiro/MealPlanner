import random
import pandas as pd
import matplotlib.pyplot as plt

protein = [
    "Peito de Frango", "Coxas de Frango", "Peito de Peru", "Coxas de Peru",
    "Lombo de Vaca", "Bife de Vaca", "Bife de Atum", "Salmão", "Bacalhau", 
    "Pescada", "Dourada", "Robalo", "Lombo de Porco", "feveras"
]

# Funções de refeição
def breakfast():
    options = [
        {"meal": "Omelete de 3 ovos \ncom espinafres, \ncogumelos e queijo feta", "calories": 223},
        {"meal": "Batido de espinafres,\n abacate, \niogurte grego \ne proteína em pó", "calories": 213},
        {"meal": "Iogurte grego \ncom frutos vermelhos \ne sementes de chia", "calories": 190},
        {"meal": "Torrada de abacate\n com ovo escalfado", "calories": 260},
        {"meal": "Papas de aveia \ncom morangos fatiados", "calories": 196}
    ]
    return f"café \n+ {random.choice(options)['meal']}"

def snack():
    options = [
        {"meal": "Iogurte grego \ncom mel e amêndoas", "calories": 178},
        {"meal": "Maçã com \nmanteiga de amendoim", "calories": 190},
        {"meal": "Cenouras \ncom húmus", "calories": 140},
        {"meal": "Queijo cottage\n com frutas", "calories": 125},
        {"meal": "Biscoitos de arroz\n com abacate", "calories": 130}
    ]
    return f"{random.choice(options)['meal']}"

def lunch(protein_choice):
    return f"salada +\n {protein_choice}"

def dinner(protein_choice):
    return f"sopa +\n {protein_choice}"

def night_snack():
    options = [
        {"meal": "1 ovo cozido +\n 1/2 abacate", "calories": 180},
        {"meal": "Palitos de cenoura \ne pepino com guacamole", "calories": 150},
        {"meal": "1 iogurte grego \nnatural sem açúcar", "calories": 100},
        {"meal": "Biscoitos de arroz\n com húmus", "calories": 140},
        {"meal": "Queijo cottage\n com frutas", "calories": 150}
    ]
    return f"{random.choice(options)['meal']}"

# Função para gerar refeições diárias
def daily_meal(name, protein_lunch, protein_dinner):
    return {
        "Pequeno-Almoço": breakfast(),
        "Lanche da Manhã": snack(),
        "Almoço": lunch(protein_lunch) + ("\n(200g)" ),
        "Lanche da Tarde": snack(),
        "Jantar": dinner(protein_dinner) + ("\n(200g)" ),
        "Lanche Noturno": night_snack()
    }

def weekly_meal():
    days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    protein_choices_lunch = [random.choice(protein) for _ in days]
    protein_choices_dinner = [random.choice(protein) for _ in days]
    return {day: daily_meal(" ", protein_lunch, protein_dinner) for day, protein_lunch, protein_dinner in zip(days, protein_choices_lunch, protein_choices_dinner)}
    
def create_combined_df():
    weekly_meals = weekly_meal()
    combined_meals = {"Refeição": []}
    days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    
    for meal_type in weekly_meals[days[0]].keys():
        combined_meals["Refeição"].append(f"{meal_type}")

        for day in days:
            if f"{day}" not in combined_meals:
                combined_meals[f"{day}"] = []
            combined_meals[f"{day}"].append(weekly_meals[day][meal_type])
    
    df = pd.DataFrame(combined_meals)
    df.set_index("Refeição", inplace=True)
    return df

def save_table_as_image(df, filename="meal_plan.png"):
    fig, ax = plt.subplots(figsize=(20, 12))  # Aumentar o tamanho da figura para melhor legibilidade
    ax.axis('tight')
    ax.axis('off')

    the_table = ax.table(cellText=df.values,
                         colLabels=df.columns,
                         rowLabels=df.index,
                         cellLoc='center',
                         loc='center')

    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.scale(1.0, 1.5)  # Aumentar o tamanho das linhas e ajustar o tamanho da tabela

    # Ajustar largura das colunas e altura das linhas
    for key, cell in the_table.get_celld().items():
        cell.set_text_props(wrap=True)
        cell.set_height(0.1)  # Definir a altura das linhas
        if key[0] == 0:
            cell.set_fontsize(12)
            cell.set_text_props(weight='bold')
        if key[1] == -1:
            cell.set_text_props(weight='bold')
        if key[1] >= 0:
            cell.set_width(0.2)  # Definir a largura das colunas

    plt.savefig(filename, bbox_inches='tight', dpi=300)  # Salvar a tabela como imagem
    plt.close()

# Exemplos de uso
print("Refeições semanais:")
combined_df = create_combined_df()
print(combined_df)
save_table_as_image(combined_df)
 