# Planeador de Refeições

Este programa Python gera:

    - um plano de refeições semanal(com um limite de calorias diário). 
    - uma lista de compras para o plano de refeições gerado
    - uma imagem png com a tabela semanal de refeições

## Funcionalidades

1. **Refeições Diárias**: Cria um plano de refeições para um dia com base num limite de calorias diário.
2. **Refeições Semanais**: Cria um plano de refeições para toda a semana.
3. **Criação de Tabela**: Combina as refeições diárias em uma tabela que é salva como uma imagem.
4. **Lista de Compras**: Gera uma lista de compras com base no plano de refeições semanal e com uma variável para controlar o numero de pessoas a seguir o plano.

## Estrutura do Código

### Importações
---
- **Imports :**
    - `random`, 
    - `pandas`, 
    - `matplotlib.pyplot`, 
    - `textwrap`
- **Módulos personalizados :** 
    - `breakfast`:
        - Módulo para gerar um pequeno almoço   
    - `snack`:
        - Módulo para gerar um snack 
    - `lunch`:
        - Módulo para gerar um almoço
    - `dinner`:
        - Módulo para gerar um jantar
    - `night_snack`:
        - Módulo para gerar um snack noturno
    - `shoppingList`:
        - Módulo para gerar:
            - lista de compras
            - exportar para um txt a lista de compras

### Funções
---
- **`breakfast()`**
    - Obtém um pequeno almoço usando o módulo breakfast
- **`snack()`**
    - Obtém um snack usando o módulo snack
- **`lunch()`**
    - Obtém um almoço usando o módulo lunch
- **`dinner()`**
    - Obtém um jantar usando o módulo dinner
- **`night_snack()`**
    - Obtém um snack usando o módulo night_snack

- **`daily_meal(calorie_limit=1800)`**
    - Gera uma refeição diária com base no limite de calorias. Retorna um dicionário com as refeições do dia.
- **`weekly_meal(calorie_limit=1800)`**
    - Gera um plano de refeições semanal. Retorna um dicionário com as refeições de cada dia da semana.
- **`wrap_text(text, width=30)`**
    - Enrola o texto para facilitar a exibição na tabela.
- **`create_combined_df(calorie_limit=1800)`**
    - Cria um DataFrame combinado com o plano de refeições semanal e formata para visualização.
- **`save_table_as_image(df, filename="meal_plan.png")`**: 
    - Salva o DataFrame como uma imagem PNG.

## Definir os parametros 
- **`calorie_limit`** : Variável para definir o limite de calorias diário
- **`num_people`** : Número de pessoas que vão seguir a dieta de forma emitir uma lista de compras atualizada

```python
print("Refeições semanais:")
combined_df = create_combined_df(calorie_limit=1800) # Limite de Calorias diário
save_table_as_image(combined_df)

weekly_meals = weekly_meal(calorie_limit=1800)
num_people = 2  # Número de pessoas para o plano de refeições
shopping_list = generate_shopping_list(weekly_meals, num_people)
save_shopping_list(shopping_list)
```
---
## Executar
```python
python meal_planner.py
```