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





basesobreviventes = pd.read_csv('gender_submission.csv', sep=',')
baseteste = pd.read_csv('test.csv', sep=',')
basetreino = pd.read_csv('train.csv', sep=',')

Classificação = basetreino.columns[1]

basetreino["Title"] = basetreino["Name"].str.extract(r",\s*([^\.]*)\.")
baseteste["Title"] = baseteste["Name"].str.extract(r",\s*([^\.]*)\.")

# Extrair a letra da cabine
basetreino["Cabin"] = basetreino["Cabin"].astype(str).str[0]  # pega só a primeira letra
baseteste["Cabin"] = baseteste["Cabin"].astype(str).str[0]


le = LabelEncoder()
basetreino["Sex"] = le.fit_transform(basetreino["Sex"])
baseteste["Sex"] = le.transform(baseteste["Sex"])


cols_onehot_encode = ['Title','Cabin','Embarked']
# Inicializar o OneHotEncoder (sparse_output=False retorna um array denso)
onehot = OneHotEncoder(sparse_output=False, handle_unknown="ignore")

# Aplicar o OneHotEncoder apenas nas colunas categóricas
df_onehot = onehot.fit_transform(basetreino[cols_onehot_encode])

# Obter os novos nomes das colunas após a codificação
nomes_das_colunas = onehot.get_feature_names_out(cols_onehot_encode)

# Criar um DataFrame com os dados codificados e as novas colunas
df_onehot = pd.DataFrame(df_onehot, columns=nomes_das_colunas)

# Combinar as colunas codificadas com as colunas que não foram transformadas
basetreino = basetreino.drop(columns=cols_onehot_encode)  # remove a coluna original
base_encoded = basetreino.join(df_onehot)  # adiciona as novas colunas no final
baseteste = baseteste.merge(basesobreviventes, on="PassengerId", how="left")

df_onehot_teste = pd.DataFrame(
    onehot.transform(baseteste[cols_onehot_encode]),
    columns=onehot.get_feature_names_out(cols_onehot_encode),
  #  index=baseteste.index
)


baseteste = baseteste.drop(columns=cols_onehot_encode)
base_encoded_teste = baseteste.join(df_onehot_teste)

X_treino = base_encoded.drop(columns=["Survived", "PassengerId", "Name", "Ticket"])
y_treino = base_encoded["Survived"]

X_teste = base_encoded_teste.drop(columns=["Survived", "PassengerId", "Name", "Ticket"])
y_teste = base_encoded_teste["Survived"]


with open('resp.pkl', mode = 'wb') as f:
  pickle.dump([X_treino, X_teste, y_treino, y_teste], f)



with open('resp.pkl', 'rb') as f:
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
print(classification_report(y_teste, previsoes))

previsores = X_treino.columns
#figura, eixos = plt.subplots(nrows=1, ncols=1, figsize=(13,13))
tree.plot_tree(
    modelo,
    feature_names=previsores,
    class_names=[str(c) for c in modelo.classes_],
    filled=True
)
plt.show()
