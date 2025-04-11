# Dados -  crie um arquivo csv

# | Mês | Vendas | Lucro |
# | --- | --- | --- |
# | Jan | 100 | 500 |
# | Fev | 120 | 600 |
# | Mar | 150 | 700 |
# | Abr | 180 | 800 |
# | Mai | 200 | 900 |

import pandas as pd
import matplotlib.pyplot as plt

# data = pd.DataFrame({
#     'Mês':['Jan','Fev','Mar','Abr','Mai'],
#     'Vendas':[100,120,150,180,200],
#     'Lucro':[500,600,700,800,900]
# })

# data.to_csv('vendas.csv', index=True)
# print ('Ação Realizada')


# 1. Gráfico de Pizza: Mostre a distribuição de vendas por mês.
# 2. Gráfico de Dispersão: Relacione vendas e lucro.
# 3. Gráfico de Barras: Compare vendas por mês.
# 4. Gráfico de Linha: Mostre a evolução do lucro ao longo dos meses.

# Carregar dados de arquivo Vendas.csv

def carregar_dados():
    df = pd.read_csv('vendas.csv')
    df = df.dropna() # Remover valores vazios
    df = df.drop_duplicates() # Remover valores duplicados
    return df

def mostrar_grafico_pizza(dados):

    if dados.empty:
        print ('Não existe dados!!!')
        return

    plt.xlabel('Mês')
    plt.ylabel('Vendas')
    plt.title('Distribuição de Vendas por Mês')
    plt.pie(dados['Vendas'], labels = dados['Mês'], autopct='%.1f%%')
    plt.show()
    return

def mostrar_grafico_barras(dados):

    if dados.empty:
        print ('Não existe dados!!!')
        return

    plt.xlabel('Vendas')
    plt.ylabel('Meses')
    plt.title('Comparação de Vendas por Meses')
    plt.bar(dados['Vendas'], dados['Mês'], color='blue')
    plt.show()
    return


def mostrar_grafico_dispersao(dados):

    if dados.empty:
        print ('Não existe dados!!!')
        return

    plt.xlabel('Lucros')
    plt.ylabel('Vendas')
    plt.title('Relação de Vendas e Lucro')
    plt.scatter(dados['Vendas'], dados['Lucro'], color='blue')
    plt.show()
    return

def mostrar_grafico_linha(dados):

    if dados.empty:
        print ('Não existe dados!!!')
        return

    plt.xlabel('Meses')
    plt.ylabel('Vendas')
    plt.title('Evolução de Vendas por Mês')
    plt.plot(dados['Mês'], dados['Vendas'], color='red')
    plt.show()
    return

dados_grafico = carregar_dados()
mostrar_grafico_pizza(dados_grafico)
mostrar_grafico_dispersao(dados_grafico)
mostrar_grafico_barras(dados_grafico)
mostrar_grafico_linha(dados_grafico)
    

