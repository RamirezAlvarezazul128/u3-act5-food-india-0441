import pandas as pd
import matplotlib.pyplot as plt
# Ramirez Azul NC 0441
# 1. Leer el archivo CSV comida pais india
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ,comida india 0441 ---")
print(df_food_india)
print("\n--- Mostrar Nombre comida + ingredientes 0441---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- tiempo de cocinado mostrar 10 registros con head 0441 ---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)


