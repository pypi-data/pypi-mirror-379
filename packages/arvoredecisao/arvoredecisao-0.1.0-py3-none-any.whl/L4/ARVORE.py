import pandas as pd

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.tree import DecisionTreeClassifier

import pickle
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from yellowbrick.classifier import ConfusionMatrix





base = pd.read_csv('restaurante.csv', sep=';')
base.head(3)
base.tail(2)
Classificação = base.columns[-1]
np.unique(base[Classificação], return_counts=True)
sns.countplot(x = base[Classificação]);
cols_label_encode = ['Alternativo', 'Bar', 'SexSab','fome', 'Cliente','Preco', 'Chuva', 'Res','Tempo']
base[cols_label_encode] = base[cols_label_encode].apply(LabelEncoder().fit_transform)
len(np.unique(base['Cliente']))
cols_onehot_encode = ['Tipo']
# Inicializar o OneHotEncoder (sparse_output=False retorna um array denso)
onehot = OneHotEncoder(sparse_output=False)

# Aplicar o OneHotEncoder apenas nas colunas categóricas
df_onehot = onehot.fit_transform(base[cols_onehot_encode])

# Obter os novos nomes das colunas após a codificação
nomes_das_colunas = onehot.get_feature_names_out(cols_onehot_encode)

# Criar um DataFrame com os dados codificados e as novas colunas
df_onehot = pd.DataFrame(df_onehot, columns=nomes_das_colunas)

# Combinar as colunas codificadas com as colunas que não foram transformadas
base_encoded= pd.concat([df_onehot, base.drop(columns=cols_onehot_encode)], axis=1)

base_encoded

base_encoded.shape

X_prev= base_encoded.iloc[:, :-1]
y_classe = base_encoded.iloc[:, -1]



X_prev
y_classe
y_classe.shape

X_treino, X_teste, y_treino, y_teste = train_test_split(X_prev, y_classe, test_size = 0.20, random_state = 42)
X_treino.shape
X_teste.shape
X_teste
y_treino
y_teste

with open('restaurante.pkl', mode = 'wb') as f:
  pickle.dump([X_treino, X_teste, y_treino, y_teste], f)



with open('restaurante.pkl', 'rb') as f:
  X_treino, X_teste, y_treino, y_teste = pickle.load(f)
  modelo = DecisionTreeClassifier(criterion='entropy')
Y = modelo.fit(X_treino, y_treino)
previsoes = modelo.predict(X_teste)
previsoes
y_teste

accuracy_score(y_teste,previsoes)

confusion_matrix(y_teste, previsoes)
cm = ConfusionMatrix(modelo)
cm.fit(X_treino, y_treino)
cm.score(X_teste, y_teste)
#print(classification_report(y_teste, previsoes))

previsores = X_treino.columns
figura, eixos = plt.subplots(nrows=1, ncols=1, figsize=(13,13))
tree.plot_tree(modelo, feature_names=previsores, class_names = modelo.classes_, filled=True);