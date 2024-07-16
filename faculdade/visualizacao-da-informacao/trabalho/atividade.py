import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

csv_file_path = r'D:\codigos\faculdade\visualizacao-da-informacao\trabalho\world_internet_user.csv'

df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

df = df[df['Country'] != '_World']

df['Population'] = pd.to_numeric(df['Population'], errors='coerce')
df['Internet Users'] = pd.to_numeric(df['Internet Users'], errors='coerce')
df['% of Population'] = pd.to_numeric(df['% of Population'], errors='coerce')

region_map = {
    'Africa': 'África',
    'Asia': 'Ásia',
    'Europe': 'Europa',
    'Middle East': 'Oriente Médio',
    'Oceania': 'Oceania',
    'America': 'América',
}

df['Region'] = df['Region'].map(region_map)


region_totals = df.groupby('Region')['Internet Users'].sum()

# Gráfico de Setores
colors = plt.cm.Pastel1(range(len(region_totals)))[::-1]
plt.figure(figsize=(10, 6))
plt.pie(region_totals, labels=region_totals.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Distribuição do Número Total de Usuários de Internet por Região')
plt.axis('equal')
plt.tight_layout()
plt.show()

# Gráfico de Barras
top10_internet_users = df.nlargest(10, 'Internet Users')

country_map = {
    'China': 'China',
    'India': 'Índia',
    'United States': 'Estados Unidos',
    'Indonesia': 'Indonésia',
    'Brazil': 'Brasil',
    'Nigeria': 'Nigéria',
    'Bangladesh': 'Bangladesh',
    'Russia': 'Rússia',
    'Japan': 'Japão',
    'Pakistan': 'Paquistão',
    'Philippines': 'Filipinas',
    'Vietnam': 'Vietnã',
    'Thailand': 'Tailândia',
    'Malaysia': 'Malásia',
    'Myanmar': 'Mianmar',
    'Korea, South': 'Coreia do Sul',
    'Taiwan': 'Taiwan',
    'Uzbekistan': 'Uzbequistão',
    'Nepal': 'Nepal',
    'Kazakhstan': 'Cazaquistão',
    'Turkey': 'Turquia',
    'United Kingdom': 'Reino Unido',
    'Germany': 'Alemanha',
    'France': 'França',
    'Italy': 'Itália',
    'Spain': 'Espanha',
    'Ukraine': 'Ucrânia',
    'Poland': 'Polônia',
    'Netherlands': 'Países Baixos',
    'Egypt': 'Egito',
    'Kenya': 'Quênia',
    'South Africa': 'África do Sul',
    'Tanzania': 'Tanzânia',
    'Ethiopia': 'Etiópia',
    'Algeria': 'Argélia',
    'Morocco': 'Marrocos',
    'Uganda': 'Uganda',
    'Congo, Dem. Rep.': 'Congo',
    'Iran': 'Irã',
    'Saudi Arabia': 'Arábia Saudita',
    'Iraq': 'Iraque',
    'Australia': 'Austrália',
    'Mexico': 'México',
    'Colombia': 'Colômbia',
    'Canada': 'Canadá',
    'Venezuela': 'Venezuela',
    'Argentina': 'Argentina',
    'Peru': 'Perú',
    'Chile': 'Chile',
    'Ecuador': 'Equador'
}

top10_internet_users['Country'] = top10_internet_users['Country'].map(country_map)

top10_internet_users['Internet Users (Milhões)'] = top10_internet_users['Internet Users'] / 1e6

plt.figure(figsize=(10, 6))
bars = plt.barh(top10_internet_users['Country'].astype(str), top10_internet_users['Internet Users (Milhões)'], color='skyblue')
plt.xlabel('Número de Usuários de Internet (Milhões)')
plt.ylabel('País')
plt.title('Top 10 Países com Mais Usuários de Internet')

for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{int(bar.get_width())}', 
             va='center', ha='left', color='black', fontsize=10)

plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Gráfico Treemap
top50_internet_users = df.nlargest(50, 'Internet Users')


top50_internet_users['Country'] = top50_internet_users['Country'].map(country_map)


#top50_internet_users = top50_internet_users.dropna()

fig = px.treemap(top50_internet_users, path=['Region', 'Country'], values='Internet Users',
                 title='Distribuição dos 50 Países com Mais Usuários de Internet por Região',
                 color_discrete_sequence=px.colors.qualitative.Pastel)
fig.show()

