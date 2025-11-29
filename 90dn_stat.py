import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('Таблица -Радуга -квалы_2025-11-29_08-13-49.xlsx', sheet_name='Chart data')

df_direct = pd.read_excel('Таблица_общая -Радуга -неделя_2025-11-29_08-38-46.xlsx', sheet_name='Chart data')

# Если объединение по Period1 и CampaignId
df_merged = df.merge(df_direct, on=['Period1', 'CampaignId'], how='left')

# print(df_merged.head())

df_merged = df_merged.iloc[:-1]

months_dict = {
    'January': 'Январь',
    'February': 'Февраль',
    'March': 'Март',     
    'April': 'Апрель',
    'May': 'Май',
    'June': 'Июнь',
    'July': 'Июль',
    'August': 'Август',
    'September': 'Сентябрь',
    'October': 'Октябрь',
    'November': 'Ноябрь',
    'December': 'Декабрь'
}

df_merged['Period1'] = pd.to_datetime(df_merged['Period1'], format='%Y-%m-%d %H:%M:%S')
df_merged['CampaignId'] = df_merged['CampaignId'].astype(str).replace('\.0', '', regex=True)

print(df_merged) 

line = '='*150 + '\n'
print(line)

df_merged['month'] = df_merged['Period1'].dt.month_name().map(months_dict)

# print(df)

print(df_merged[df_merged['Квал лиды'] == 0]) 
print(line)
# group_compaign = df_merged.groupby('CampaignId')['Расход'].mean()

# print(group_compaign.head())
df_merged['CPA Замер'] = np.where(
    df_merged['Замер'] != 0,
    df_merged['Расход'] / df_merged['Замер'], #true
    df_merged['Расход']    #false
) 
df_merged['CPA Замер'] = df_merged['CPA Замер'].replace([np.inf, -np.inf], 0).fillna(0).round(0).astype(int)

# if df_merged['Договор'] != 0:
#     df_merged['CPA Договор'] = df_merged['Расход'] / df_merged['Договор']
# else:
#     df_merged['CPA Договор'] = df_merged['Расход']    

df_merged['CPA Договор'] = np.where(
    df_merged['Договор'] != 0,
    df_merged['Расход'] / df_merged['Договор'], #true
    df_merged['Расход']    #false
)
   
df_merged['CPA Договор'] = df_merged['CPA Договор'].replace([np.inf, -np.inf], 0).fillna(0).round(0).astype(int)

group_compaign = df_merged.groupby('CampaignId').agg({
    'Договор': 'median',
    'Замер': 'mean',
    'Расход': 'mean',
    'Квал лиды': 'mean',
    'Лиды': 'mean',
    'CPA Замер': 'mean',
    'CPA Договор': 'mean'
}).round(0).astype(int).reset_index()

print(group_compaign)
print(line)
print(group_compaign)
print(line)

# df_merged['CampaignId'].hist()
# plt.show()

# group_compaign.set_index('CampaignId')[['CPA Замер', 'CPA Договор']].plot(kind='bar')
# plt.xlabel('CampaignId')
# plt.ylabel('Количество')
# plt.title('Статистика по кампаниям')
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()

stats = df_merged["Замер"].describe()
print(stats)
print(line)

stats = df_merged["Договор"].describe()
print(stats)
print(line)

stats = df_merged["Расход"].describe()
print(stats)
print(line)

stats = df_merged["Квал лиды"].describe()
print(stats)
print(line)

stats = df_merged["Лиды"].describe()
print(stats)
print(line)


quantiles = df_merged["Замер"].quantile([0.25, 0.5, 0.75])
print(f"Quantile: 0.25: {quantiles[0.25]}, Quantile: 0.5: {quantiles[0.5]}, Quantile: 0.75: {quantiles[0.75]}")
 

Q1, Q2, Q3 = df_merged["Замер"].quantile([0.25, 0.5, 0.75])
 

IQR = Q3 - Q1
print(f"IQR: {IQR}") 

plt.figure(figsize=(15, 6))

df_melted = df_merged.melt(id_vars=['CampaignId'], value_vars=['Замер', 'Договор', 'Расход'], var_name='Метрика', value_name='Значения')

sns.boxplot(x='Метрика', y='Значения', data=df_melted)
plt.title('Boxplot для метрик')
plt.show()
