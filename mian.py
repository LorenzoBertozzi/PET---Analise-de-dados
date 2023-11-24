#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn  as sns

#%%
import os
print(os.listdir('CSV'))
diretorio = 'CSV'
arquivos_combinados = pd.DataFrame()

for arquivo in  os.listdir(diretorio + "/"):
    #print(arquivo)
    dados = pd.read_csv("CSV/" + arquivo)
    arquivos_combinados = pd.concat([arquivos_combinados,dados], ignore_index=True)

arquivos_combinados.to_csv('CSV/arquivos_combinados.csv', index=False)

dados_combinados = pd.read_csv('CSV/arquivos_combinados.csv')
dados_combinados = dados_combinados.apply(lambda x: x.astype(str).str.lower())
dados_combinados.head()
#%%

dados_tecnico = dados_combinados.loc[dados_combinados['Qual seu curso? '].str.contains('técnico')]
dados_engenharia = dados_combinados.loc[dados_combinados['Qual seu curso? '].str.contains('engenharia')]

#%%
dados_engenharia.head()

# %%
#efetividade do minicuruso
tabela_efetividade = pd.DataFrame()
tabela_efetividade = pd.merge(dados_engenharia['4 -  Quanto você avalia suas expectativas em relação ao curso.'],dados_engenharia['7- O quanto suas expectativas foram atendidas nesse minicurso?'],on=dados_engenharia, how='outer',indicator=True)

tabela_efetividade.head()

#nesse caso todos os campos da coluna 7 estao vazios!!

