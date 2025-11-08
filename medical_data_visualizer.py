import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('data/medical_examination.csv')

# 2
df['overweight'] = np.where((df['weight'] / ((df['height'] / 100) ** 2)) > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['id', 'cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                     var_name='Categoria', value_name='Valor')


    # 6
    df_cat_grouped = df_cat.groupby(['cardio', 'Categoria', 'Valor']).size().reset_index(name='total')
    

    # 7
    sns.catplot(data=df_cat_grouped, 
                x='Categoria', 
                y='total', 
                hue='Valor', 
                col='cardio',
                kind='bar', 
                height=6, 
                aspect=1.5, 
                palette={0: 'blue', 1: 'orange'})

    plt.subplots_adjust(top=0.85)
    plt.suptitle('Distribuição das Características Categóricas por Cardio', fontsize=16)


    # 8
    fig = plt.gcf()


    # 9
    fig.savefig('images/Medicalcatplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &  # Pressão diastólica não maior que a sistólica
        (df['height'] >= df['height'].quantile(0.025)) &  # Altura maior que o percentil 2,5
        (df['height'] <= df['height'].quantile(0.975)) &  # Altura menor que o percentil 97,5
        (df['weight'] >= df['weight'].quantile(0.025)) &  # Peso maior que o percentil 2,5
        (df['weight'] <= df['weight'].quantile(0.975))     # Peso menor que o percentil 97,5
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # 14
    fig, ax = plt.subplots(figsize=(12, 9), dpi=100)

    # 15
    sns.heatmap(corr, annot=True, cmap='flare', fmt='.1f', linewidths=0.5, vmin=-0.1, vmax=0.30, mask=mask, ax=ax)

    # 11: Ajustando os títulos e rótulos
    ax.set_title('Mapa de Calor - Correlação entre as variáveis', fontsize=16)  # Título da figura
    ax.set_xlabel('Variáveis')  # Rótulo do eixo X
    ax.set_ylabel('Variáveis')  # Rótulo do eixo Y
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)  # Rótulos do eixo X na posição reta
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)  # Rótulos do eixo Y na posição reta

    # 12: Exibindo a grade para facilitar a leitura do gráfico
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

    # 13: Exibindo o gráfico
    plt.tight_layout()  # Ajustando o layout para não cortar partes do gráfico

    # 16
    fig.savefig('images/Medicalheatmap.png')
    return fig

print(draw_cat_plot())
print(draw_heat_map())