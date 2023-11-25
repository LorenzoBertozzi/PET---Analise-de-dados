#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#%%
import os
print(os.listdir('CSV'))

df1 = pd.read_csv('CSV\Avaliação Pré Minicurso Introdução ao LaTeX (respostas) - Respostas ao formulário 1.csv')
df2 = pd.read_csv('CSV\Avaliação Pós Minicurso Introdução ao LaTeX (respostas) - Respostas ao formulário 1.csv')

df_merged = pd.merge(df1, df2, on=['Endereço de e-mail','Nome Completo:','Qual seu curso? '], how='inner')
df_merged = df_merged.drop('Carimbo de data/hora_y', axis=1)

df_merged.head()

#%%
dados_tecnico = df_merged.loc[df_merged['Qual seu curso? '].str.contains('técnico')]
dados_engenharia = df_merged.loc[df_merged['Qual seu curso? '].str.contains('Engenharia')]

#%%
dados_engenharia.head()

#%%COMPARAÇÂO DE NIVEL
print(df_merged['1 - Como você julga seu nível de conhecimento atual sobre o tema do minicurso que você esta fazendo?'].mean())
print(df_merged['4- Como você julga seu nível de conhecimento na acerca do tema após o minicurso:'].mean())

#%% MEDIA DE MOTIVAÇÂO 
print(df_merged['2 - O quanto motivado você esta para realizar esse minicurso?'].mean())
