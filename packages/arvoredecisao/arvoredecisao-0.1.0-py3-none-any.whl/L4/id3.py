import pandas as pd
import numpy as np
from math import log2

# Carregar dataset Titanic
df = pd.read_csv("train.csv")

# Remover colunas que não ajudam no ID3 (identificação)
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

# Tratar valores faltantes (simples: moda para Embarked, mediana para Age)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Fare"].fillna(df["Fare"].median(), inplace=True)

# Discretizar Age em categorias
df["AgeGroup"] = pd.cut(
    df["Age"], bins=[0, 12, 18, 40, 60, 100],
    labels=["Criança", "Adolescente", "Adulto", "Meia-idade", "Idoso"]
)

# Discretizar Fare (tarifa) em 4 faixas de frequência
df["FareGroup"] = pd.qcut(df["Fare"], q=4, labels=["Muito Baixo", "Baixo", "Alto", "Muito Alto"])

# Transformar Sex em categórico

def entropia(y):
    valores, contagens = np.unique(y, return_counts=True)
    probs = contagens / contagens.sum()
    return -np.sum(probs * np.log2(probs))
def ganho_informacao(X, y, atributo):
    valores, contagens = np.unique(X[atributo], return_counts=True)
    entropia_filhos = 0
    
    for v, c in zip(valores, contagens):
        y_filho = y[X[atributo] == v]
        entropia_filhos += (c / len(y)) * entropia(y_filho)
    
    return entropia(y) - entropia_filhos
def id3(X, y, atributos, profundidade=0):
    # Caso base: todas as instâncias são da mesma classe
    if len(np.unique(y)) == 1:
        return np.unique(y)[0]
    
    # Caso base: sem atributos disponíveis
    if len(atributos) == 0:
        return y.mode()[0]  # Classe majoritária
    
    # Escolher o melhor atributo pelo ganho de informação
    ganhos = [ganho_informacao(X, y, attr) for attr in atributos]
    melhor_attr = atributos[np.argmax(ganhos)]
    
    # Criar nó da árvore
    arvore = {melhor_attr: {}}
    
    # Criar ramos para cada valor do atributo
    for v in np.unique(X[melhor_attr]):
        X_sub = X[X[melhor_attr] == v].drop(columns=[melhor_attr])
        y_sub = y[X[melhor_attr] == v]
        
        if len(y_sub) == 0:
            arvore[melhor_attr][v] = y.mode()[0]  # classe majoritária
        else:
            novos_atributos = [a for a in atributos if a != melhor_attr]
            arvore[melhor_attr][v] = id3(X_sub, y_sub, novos_atributos, profundidade+1)
    
    return arvore
X = df[["Pclass", "Sex", "AgeGroup", "SibSp", "Parch", "FareGroup", "Embarked"]]
y = df["Survived"]

atributos = list(X.columns)

arvore_titanic = id3(X, y, atributos)
print(arvore_titanic)
