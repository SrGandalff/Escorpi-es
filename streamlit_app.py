# importando as bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd

# Estrutura a base inicial do painel

# Carregar os dados do Excel em um DataFrame pandas
dados_escorpioes = pd.read_excel('caminho/do/seu/arquivo.xlsx')

# Visualizar as primeiras linhas dos dados para verificar se foram carregados corretamente
print(dados_escorpioes.head())

# Logos e título, e possivelmente os containers

 # O banco possivelmente do google drive
