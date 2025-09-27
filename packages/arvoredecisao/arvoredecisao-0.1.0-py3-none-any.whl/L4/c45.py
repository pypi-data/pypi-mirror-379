import pandas as pd
import numpy as np

# Carregar dataset Titanic
df = pd.read_csv("train.csv")
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

# Tratar valores faltantes
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Fare"].fillna(df["Fare"].median(), inplace=True)

# Converter Sex para categórico (0/1)
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

# Função de entropia
def entropia(y):
    valores, contagens = np.unique(y, return_counts=True)
    probs = contagens / contagens.sum()
    return -np.sum(probs * np.log2(probs))

# Ganho de informação
def ganho_informacao(y, X_col):
    valores, contagens = np.unique(X_col, return_counts=True)
    entropia_filhos = 0
    for v, c in zip(valores, contagens):
        y_filho = y[X_col == v]
        entropia_filhos += (c / len(y)) * entropia(y_filho)
    return entropia(y) - entropia_filhos

# SplitInfo para Gain Ratio
def split_info(X_col):
    valores, contagens = np.unique(X_col, return_counts=True)
    probs = contagens / contagens.sum()
    return -np.sum(probs * np.log2(probs))

def gain_ratio(y, X_col):
    ig = ganho_informacao(y, X_col)
    si = split_info(X_col)
    return ig / si if si != 0 else 0

# Encontrar melhor split para atributos contínuos
def melhor_split_continuo(X_col, y):
    valores = np.sort(X_col.unique())
    melhores = []
    melhor_gain = -1
    melhor_limiar = None
    
    # Testa limiares médios entre valores consecutivos
    for i in range(len(valores) - 1):
        limiar = (valores[i] + valores[i+1]) / 2
        X_bin = (X_col <= limiar).astype(int)  # cria atributo binário
        gr = gain_ratio(y, X_bin)
        if gr > melhor_gain:
            melhor_gain = gr
            melhor_limiar = limiar
    
    return melhor_gain, melhor_limiar

# Implementação C4.5
def c45(X, y, atributos, profundidade=0):
    # Caso base: todas instâncias da mesma classe
    if len(np.unique(y)) == 1:
        return np.unique(y)[0]
    
    # Caso base: sem atributos
    if len(atributos) == 0:
        return y.mode()[0]
    
    melhor_attr, melhor_gain, melhor_limiar = None, -1, None
    is_continuous = False
    
    # Escolhe melhor atributo
    for attr in atributos:
        if np.issubdtype(X[attr].dtype, np.number) and len(X[attr].unique()) > 10:
            # Contínuo → buscar limiar
            gr, limiar = melhor_split_continuo(X[attr], y)
            if gr > melhor_gain:
                melhor_attr, melhor_gain, melhor_limiar = attr, gr, limiar
                is_continuous = True
        else:
            # Categórico
            gr = gain_ratio(y, X[attr])
            if gr > melhor_gain:
                melhor_attr, melhor_gain = attr, gr
                melhor_limiar = None
                is_continuous = False
    
    if melhor_attr is None:
        return y.mode()[0]
    
    arvore = {melhor_attr: {}}
    
    if is_continuous:
        # Dois ramos: <= limiar e > limiar
        X_left, y_left = X[X[melhor_attr] <= melhor_limiar], y[X[melhor_attr] <= melhor_limiar]
        X_right, y_right = X[X[melhor_attr] > melhor_limiar], y[X[melhor_attr] > melhor_limiar]
        
        arvore[melhor_attr][f"<= {melhor_limiar:.2f}"] = (
            y_left.mode()[0] if len(y_left) == 0 
            else c45(X_left, y_left, [a for a in atributos if a != melhor_attr], profundidade+1)
        )
        arvore[melhor_attr][f"> {melhor_limiar:.2f}"] = (
            y_right.mode()[0] if len(y_right) == 0 
            else c45(X_right, y_right, [a for a in atributos if a != melhor_attr], profundidade+1)
        )
    else:
        # Categórico → ramos por valor
        for v in np.unique(X[melhor_attr]):
            X_sub = X[X[melhor_attr] == v].drop(columns=[melhor_attr])
            y_sub = y[X[melhor_attr] == v]
            arvore[melhor_attr][v] = (
                y.mode()[0] if len(y_sub) == 0 
                else c45(X_sub, y_sub, [a for a in atributos if a != melhor_attr], profundidade+1)
            )
    
    return arvore

# Rodar C4.5
X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = df["Survived"]
atributos = list(X.columns)

arvore_c45 = c45(X, y, atributos)
print(arvore_c45)
