import random
import pandas as pd
import matplotlib.pyplot as plt
import textwrap
import breakfast as b
import snack as s
import lunch as l
import dinner as d
import night_snack as ns
from shoppingList import generate_shopping_list, save_shopping_list

# Funções de refeição
def breakfast():
    return b.getBreakfast()

def snack():
    return s.getSnack()

def lunch():
    return l.getLunch()

def dinner():
    return d.getDinner()

def night_snack():
    return ns.getNightSnack()

# Função para gerar refeições diárias
def daily_meal():
    breakfast_meal = breakfast()
    return {
        "Pequeno-Almoço": breakfast_meal,
        "Lanche da Manhã": snack(),
        "Almoço": lunch(),
        "Lanche da Tarde": snack(),
        "Jantar": dinner(),
        "Lanche Noturno": night_snack()
    }

def weekly_meal():
    days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    return {day: daily_meal() for day in days}

def wrap_text(text, width=30):
    return "\n".join(textwrap.wrap(text, width))

def create_combined_df():
    weekly_meals = weekly_meal()
    combined_meals = {"Refeição": []}
    days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    
    for meal_type in weekly_meals[days[0]].keys():
        combined_meals["Refeição"].append(f"{meal_type}")

        for day in days:
            if f"{day}" not in combined_meals:
                combined_meals[f"{day}"] = []
            meal_info = weekly_meals[day][meal_type]
            meal_text = f"{meal_info['meal']} ({meal_info['calories']} cal)"
            meal_text_wrapped = wrap_text(meal_text)
            combined_meals[f"{day}"].append(meal_text_wrapped)
    
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

    # Ajustar largura das colunas, altura das linhas e cores das células
    for key, cell in the_table.get_celld().items():
        cell.set_text_props(wrap=True)
        cell.set_height(0.1)  # Definir a altura das linhas
        cell.set_fontsize(10)
        cell.set_text_props(ha='left', va='center')  # Ajustar o alinhamento horizontal e vertical
        
        if key[0] == 0:
            cell.set_fontsize(12)
            cell.set_text_props(weight='bold')
            cell.set_facecolor('#90EE90')  # Verde claro para o cabeçalho das refeições
        if key[1] == -1:
            cell.set_text_props(weight='bold')
            cell.set_facecolor('#90EE90')  # Verde claro para os dias da semana
        
        if key[1] >= 0:
            cell.set_width(0.2)  # Definir a largura das colunas

    plt.savefig(filename, bbox_inches='tight', dpi=300)  # Salvar a tabela como imagem
    plt.close()

# Exemplos de uso
print("Refeições semanais:")
combined_df = create_combined_df()
print(combined_df)
save_table_as_image(combined_df)

weekly_meals = weekly_meal()
num_people = 2  # Número de pessoas para o plano de refeições
shopping_list = generate_shopping_list(weekly_meals, num_people)
save_shopping_list(shopping_list)
#print("\nLista de compras:")
#for item, quantities in shopping_list.items():
#    for unit, quantity in quantities.items():
#        print(f"{item}: {quantity} {unit}")
