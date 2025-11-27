 

import pandas as pd

# Загружаем данные с указанием кодировки
df = pd.read_csv('dz.csv', sep=',', encoding='utf-8')  # Изменили разделитель на запятую

print("Первые 5 строк данных:")
print(df.head())

print("\nИнформация о DataFrame:")
print(df.info())

 
 
print(df[df["Salary"] > 100000])

group = df.groupby("City")['Salary'].mean()

print(group)

df_k = pd.read_csv('AgeDataset-V1.csv', sep=',', encoding='utf-8')
print("Первые 5 строк данных:")
print(df_k.head())
print(df_k.info())
print(df_k.describe())


group = df_k.groupby("Gender")['Age of death'].mean()

print(group)

