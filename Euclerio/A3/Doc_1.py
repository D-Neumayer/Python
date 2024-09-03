import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Carregar datasets
obesity_df = pd.read_csv('Euclerio\A3\obesity-cleaned.csv')
gdp_df = pd.read_csv('Euclerio\A3\GDP.csv')

# Verificar colunas do DataFrame de obesidade
print("Colunas do DataFrame de obesidade:")
print(obesity_df.columns)

# Verificar colunas do DataFrame de PIB
print("Colunas do DataFrame de PIB:")
print(gdp_df.columns)

# Renomear colunas para facilitar o uso
obesity_df.rename(columns={'Obesity (%)': 'Obesity'}, inplace=True)
gdp_df.rename(columns={' GDP_pp ': 'GDP'}, inplace=True)

# Limpeza da coluna 'Obesity' para manter apenas os números
obesity_df['Obesity'] = obesity_df['Obesity'].str.extract(
    r'(\d+\.\d+)').astype(float)

# Verificar se a coluna 'Obesity' existe
if 'Obesity' not in obesity_df.columns:
    raise ValueError(
        "A coluna 'Obesity' não foi encontrada no DataFrame de obesidade.")

# Converter colunas numéricas em gdp_df
for col in gdp_df.columns:
    gdp_df[col] = pd.to_numeric(gdp_df[col], errors='coerce')

# Interpolação no dataset de PIB
gdp_df = gdp_df.interpolate(method='linear', axis=0)

# 1. Percentual médio de obesidade por sexo na América do Norte em 2010
if 'Country' in obesity_df.columns and 'Year' in obesity_df.columns:
    obesity_df['Region'] = np.where(obesity_df['Country'].isin(
        ['Canada', 'United States', 'Mexico']), 'North America', 'Other')
    north_america_2010 = obesity_df[(
        obesity_df['Region'] == 'North America') & (obesity_df['Year'] == 2010)]
    mean_obesity_2010 = north_america_2010.groupby('Sex')['Obesity'].mean()
    print("Percentual médio de obesidade por sexo na América do Norte em 2010:")
    print(mean_obesity_2010)
else:
    print("As colunas 'Country' ou 'Year' não foram encontradas no DataFrame de obesidade.")

# 2. Crescimento do PIB
gdp_growth = gdp_df.diff().mean()

# Preparar a figura para múltiplos gráficos
fig, axes = plt.subplots(3, 2, figsize=(20, 18))

# 3. Gráfico de obesidade por ano
if 'Year' in obesity_df.columns and 'Obesity' in obesity_df.columns and 'Sex' in obesity_df.columns:
    sns.lineplot(data=obesity_df, x='Year',
                 y='Obesity', hue='Sex', ax=axes[0, 0])
    axes[0, 0].set_title('Obesidade ao longo dos anos')
else:
    print("Colunas necessárias para o gráfico de obesidade por ano não encontradas.")

# 4. Dados entre homens e mulheres
if 'Sex' in obesity_df.columns and 'Year' in obesity_df.columns and 'Obesity' in obesity_df.columns:
    obesity_by_sex = obesity_df.groupby(['Year', 'Sex'])[
        'Obesity'].mean().unstack()

    # Plotando gráfico comparativo
    obesity_by_sex.plot(kind='line', ax=axes[0, 1])
    axes[0, 1].set_title('Percentual de Obesidade por Sexo ao Longo dos Anos')
    axes[0, 1].set_ylabel('Percentual de Obesidade')
    axes[0, 1].set_xlabel('Ano')
else:
    print("Colunas necessárias para o gráfico de obesidade por sexo não encontradas.")

# 5. Função para calcular taxa de aumento


def calculate_rate_increase(df, year):
    data_year = df[df['Year'] == year]
    top3_increase = data_year.nlargest(3, 'Obesity')
    top3_decrease = data_year.nsmallest(3, 'Obesity')
    return top3_increase, top3_decrease


top3_2010_increase, top3_2010_decrease = calculate_rate_increase(
    obesity_df, 2010)
top3_2016_increase, top3_2016_decrease = calculate_rate_increase(
    obesity_df, 2016)

print("Top 3 países com maior aumento em 2010:\n",
      top3_2010_increase[['Country', 'Obesity']])
print("Top 3 países com menor aumento em 2010:\n",
      top3_2010_decrease[['Country', 'Obesity']])
print("Top 3 países com maior aumento em 2016:\n",
      top3_2016_increase[['Country', 'Obesity']])
print("Top 3 países com menor aumento em 2016:\n",
      top3_2016_decrease[['Country', 'Obesity']])

# 6. Extraindo informações sobre o Brasil
if 'Country' in obesity_df.columns and 'Year' in obesity_df.columns and 'Obesity' in obesity_df.columns and 'Sex' in obesity_df.columns:
    brazil_data = obesity_df[obesity_df['Country'] == 'Brazil']

    # Plotando gráfico de obesidade no Brasil
    sns.lineplot(data=brazil_data, x='Year',
                 y='Obesity', hue='Sex', ax=axes[1, 0])
    axes[1, 0].set_title('Obesidade no Brasil ao Longo dos Anos')
    axes[1, 0].set_ylabel('Percentual de Obesidade')
    axes[1, 0].set_xlabel('Ano')
else:
    print("Colunas necessárias para o gráfico de obesidade no Brasil não encontradas.")

# 7. Adaptar preenchendo os anos vazios
gdp_df['Year'] = pd.to_datetime(gdp_df['Year'], errors='coerce', format='%Y')
# Remove linhas onde 'Year' não pôde ser convertido para datetime
gdp_df = gdp_df.dropna(subset=['Year'])
gdp_df = gdp_df.set_index('Year')
gdp_df = gdp_df.resample('YE').mean().interpolate(
    method='linear').reset_index()

# Plotando gráfico de crescimento de PIB
if 'Year' in gdp_df.columns and 'GDP' in gdp_df.columns:
    sns.lineplot(data=gdp_df, x='Year', y='GDP', ax=axes[1, 1])
    axes[1, 1].set_title('Crescimento do PIB per Capita ao Longo dos Anos')
    axes[1, 1].set_ylabel('PIB per Capita')
    axes[1, 1].set_xlabel('Ano')
else:
    print("Colunas necessárias para o gráfico de crescimento do PIB não encontradas.")

# 8. Merge dos datasets para correlação
if 'Country' in obesity_df.columns and 'Year' in obesity_df.columns and 'Year' in gdp_df.columns and 'GDP' in gdp_df.columns:
    obesity_df['Year'] = pd.to_datetime(
        obesity_df['Year'], errors='coerce', format='%Y')
    merged_df = pd.merge(obesity_df, gdp_df, on=[
                         'Country', 'Year'], how='inner')

    # Remover valores NaN
    merged_df = merged_df.dropna(subset=['GDP', 'Obesity'])

    # Relação entre PIB e obesidade
if 'GDP' in merged_df.columns and 'Obesity' in merged_df.columns and 'Sex' in merged_df.columns:
    sns.scatterplot(data=merged_df, x='GDP', y='Obesity',
                    hue='Sex', ax=axes[2, 0])
    axes[2, 0].set_title('Relação entre PIB per Capita e Obesidade')
    axes[2, 0].set_xlabel('PIB per Capita')
    axes[2, 0].set_ylabel('Percentual de Obesidade')

    # 9. Relação entre PIB e obesidade no Brasil, EUA e Portugal
countries = ['Brazil', 'United States', 'Portugal']
country_data = merged_df[merged_df['Country'].isin(countries)]

if 'Year' in country_data.columns and 'Obesity' in country_data.columns and 'Country' in country_data.columns:
    sns.lineplot(data=country_data, x='Year', y='Obesity',
                 hue='Country', ax=axes[2, 1])
    axes[2, 1].set_title(
        'Relação entre PIB per Capita e Obesidade (Brasil, EUA, Portugal)')
    axes[2, 1].set_xlabel('Ano')
    axes[2, 1].set_ylabel('Percentual de Obesidade')
else:
    print("Colunas necessárias para mesclar os DataFrames não encontradas.")

# Ajustar layout
plt.tight_layout()

# Salvando a figura completa
plt.savefig('resultados.png')
plt.show()

# Salvando output em um arquivo CSV
output_filename = f"{datetime.now().strftime('%d_%m_%Y')}_A3_equipe_N.csv"
merged_df.to_csv(output_filename, index=False)
