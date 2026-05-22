"""
PROJETO: Amazon Sales & Reviews Analytics
AUTOR: Tiago Almeida - Analista de Dados 
DESCRIÇÃO: Script de ETL e Análise Exploratória para base de dados de produtos Amazon.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data(path):
    """
    Carrega a base de dados e realiza o tratamento de tipos e limpeza de caracteres especiais.
    """
    print("Iniciando carregamento e limpeza...")
    df = pd.read_csv(path, delimiter=',')
    
    # Limpeza de colunas financeiras e conversão para Real Brasileiro
    exchange_rate = 0.052
    df['discounted_price'] = (df['discounted_price'].str.replace('₹', '').str.replace(',', '').astype(float) * exchange_rate).apply(lambda x: f"{x:.2f}".replace('.', ','))
    df['actual_price'] = (df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float) * exchange_rate).apply(lambda x: f"{x:.2f}".replace('.', ','))
    df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype(float) / 100
    
    #print(df['discount_percentage'].dtypes)

    # Tratamento de Ratings
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df['rating_count'] = df['rating_count'].str.replace(',', '').astype(float)
    
    # Tratamento de valores ausentes
    df = df.dropna(subset=['rating', 'rating_count'])
    
    # Engenharia de Atributos: Extração de Categoria Principal
    df['main_category'] = df['category'].apply(lambda x: x.split('|')[0])
    
    print("Limpeza concluída com sucesso.")
    return df

# Code para geração de insights e visualizações (comentado para evitar execução durante o processo de ETL)
'''
def generate_insights(df):
    """
    Realiza análises estatísticas e gera visualizações para o portfólio.
    """
    print("Gerando insights e visualizações...")
    
    # 1. Top Categorias por Faturamento Potencial
    plt.figure(figsize=(12,6))
    top_cats = df.groupby('main_category')['discounted_price'].sum().sort_values(ascending=False)
    sns.barplot(x=top_cats.values, y=top_cats.index, palette='viridis')
    plt.title('Faturamento Potencial por Categoria Principal')
    plt.xlabel('Soma de Preços com Desconto (₹)')
    plt.savefig('faturamento_categorias.png')
    
    # 2. Relação Preço vs Rating
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x='actual_price', y='rating', hue='main_category', alpha=0.6)
    plt.xscale('log')
    plt.title('Relação Preço Real (Log) vs Rating por Categoria')
    plt.savefig('preco_vs_rating.png')
    
    # 3. Distribuição de Descontos
    plt.figure(figsize=(10,6))
    sns.histplot(df['discount_percentage'], bins=20, kde=True, color='green')
    plt.title('Distribuição de Percentual de Desconto')
    plt.savefig('distribuicao_descontos.png')
'''

# Caminho CORRETO do arquivo de dados para leitura
CAMINHO_ENTRADA = r"C:\Users\TIAGO ALMEIDA\Downloads\Kaggle\sales_analytics_amazon\amazon.csv"


def export_data(df, output_path):
    """
    Exporta a base tratada para uso em ferramentas de BI (Power BI/Tableau).
    """
    df.to_csv(output_path, index=False)
    print(f"Base exportada para: {output_path}")

if __name__ == "__main__":
    DATA_PATH = CAMINHO_ENTRADA
    OUTPUT_PATH = r"C:\Users\TIAGO ALMEIDA\Downloads\Kaggle\sales_analytics_amazon\files\output\new_amazon.csv"
    
    df_amazon = load_and_clean_data(DATA_PATH)
    # generate_insights(df_amazon)
    export_data(df_amazon, OUTPUT_PATH)
    
    print("\n--- RESUMO DA ANÁLISE ---")
    print(f"Total de produtos analisados: {len(df_amazon)}")
    print(f"Rating médio da base: {df_amazon['rating'].mean():.2f}")
    print(f"Desconto médio aplicado: {df_amazon['discount_percentage'].mean()*100:.2f}%")
