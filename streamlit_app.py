from datetime import date

import pandas as pd
import streamlit as st


#carregar os dados
@st.cache_data #decorator
def carregar_dados():
    casas = pd.read_csv("houses_to_rent_v2.csv")
    return casas

dados = carregar_dados()
#print(dados['city'])

st.write("""
# Casas para Aluguel 
""")

# prepara as visualizações = filtros
st.sidebar.header("Filtros")

#filtro por cidades
cidades_unicas = list(dados['city'].unique())
lista_cidades = st.sidebar.multiselect("Cidades", cidades_unicas)

#filtro por area
menor_area = int(dados.area.min())
maior_area = int(dados.area.max())
intervalo_data_area = st.sidebar.slider("Selecione a area", 
                                   min_value=menor_area, 
                                   max_value=2000,
                                   value=(menor_area, 2000))

#filtro por salas
menor_sala= int(dados.rooms.min())
maior_sala = int(dados.rooms.max())
intervalo_data_sala = st.sidebar.slider("Selecione quantas salas", 
                                   min_value=menor_sala, 
                                   max_value=maior_sala,
                                   value=(menor_sala, maior_sala))
#filtro por banheiros
menor_banheiro= int(dados.bathroom.min())
maior_banheiro = int(dados.bathroom.max())
intervalo_data_banheiro = st.sidebar.slider("Selecione quantos banheiros", 
                                   min_value=menor_banheiro, 
                                   max_value=maior_banheiro,
                                   value=(menor_banheiro, maior_banheiro))
#filtro por vages de estacionamento
#intervalo_data_vaga_estacionamento = st.sidebar.slider("Selecione quantas vagas de estacionamento", 
#                                   min_value=0, 
#                                   max_value=20,
#                                   value=(0, 20))

#dados = dados.loc[intervalo_data[0]:intervalo_data[1]]
#print(lista_cidades)
#pagina principal dados
#print(dados)

dados = dados.query("city in @lista_cidades")
dados = dados.query(f"area >= {intervalo_data_area[0]} and area <= {intervalo_data_area[1]}")
dados = dados.query(f"rooms >= {intervalo_data_sala[0]} and rooms <= {intervalo_data_sala[1]}")
dados = dados.query(f"bathroom >= {intervalo_data_banheiro[0]} and bathroom <= {intervalo_data_banheiro[1]}")
#dados = dados.query(f""parking spaces" >= {intervalo_data_vaga_estacionamento[0]} and "parking spaces" <= {intervalo_data_vaga_estacionamento[1]}")
#print(dados)
#metricas básicas
col1, col2, col3 = st.columns(3)
col1.metric("Preço médio da seleção", 'R$ {:.2f}'.format(dados['rent amount (R$)'].mean()))
col2.metric("Impostos médios da seleção", 'R$ {:.2f}'.format(dados['property tax (R$)'].mean()))
col3.metric("Média de seguro da seleção", 'R$ {:.2f}'.format(dados['fire insurance (R$)'].mean()))

st.dataframe(dados)
