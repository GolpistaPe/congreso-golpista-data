import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv ('data/investigaciones.csv')
df.head()

df = pd.read_csv ('data/investigaciones-limpio.csv')
df.head()
df[['TIPO DE DELITO','DETALLE']]=df['DELITO'].str.split('(',n=1,expand=True)
df.head()

texto = [texto for texto in df["TIPO DE DELITO"]]
print(texto)

Lista = []

for i in texto:
    i = i.strip()
    Lista.append(i)

for i in (sorted(set(Lista))):
  print(i)

df["TIPO DE DELITO"] = Lista


df.groupby(['APELLIDOS Y NOMBRE','TIPO DE DELITO'])['TIPO DE DELITO'].count()

ConDelito = df.groupby(['APELLIDOS Y NOMBRE','TIPO DE DELITO'])[['TIPO DE DELITO']].count()
ConDelito.head(20)

ConDelito.columns

plt.rcParams['figure.figsize'] = (30,6)
ConDelito['TIPO DE DELITO'].unstack(1).plot(kind='bar', stacked=True)
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left")
