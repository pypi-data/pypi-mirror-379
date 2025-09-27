import pandas as pd
import numpy as np

# Carregar dataset Titanic
df = pd.read_csv("train.csv")
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

# Tratar valores faltantes
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Fare"].fillna(df["Fare"].median(), inplace=True)

# Converter sexo para numérico (0 = homem, 1 = mulher)
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

# ---------- Funções CART ----------

# Índice de Gini
def gini(y):
    valores, contagens = np.unique(y, return_counts=True)
    probs = contagens / contagens.sum()
    return 1 - np.sum(probs**2)

# Gini ponderado após split
def gini_split(y_left, y_right):
    n = len(y_left) + len(y_right)
    return (len(y_left)/n) * gini(y_left) + (len(y_right)/n) * gini(y_right)

# Encontrar melhor split para atributo contínuo
def melhor_split_continuo(X_col, y):
    valores = np.sort(X_col.unique())
    melhor_gini, melhor_limiar = 1, None
    
    for i in range(len(valores) - 1):
        limiar = (valores[i] + valores[i+1]) / 2
        y_left = y[X_col <= limiar]
        y_right = y[X_col > limiar]
        g = gini_split(y_left, y_right)
        if g < melhor_gini:
            melhor_gini, melhor_limiar = g, limiar
    
    return melhor_gini, melhor_limiar

# Encontrar melhor split para atributo categórico
def melhor_split_categorico(X_col, y):
    melhor_gini, melhor_categoria = 1, None
    for cat in np.unique(X_col):
        y_left = y[X_col == cat]
        y_right = y[X_col != cat]
        g = gini_split(y_left, y_right)
        if g < melhor_gini:
            melhor_gini, melhor_categoria = g, cat
    return melhor_gini, melhor_categoria

# Construção da árvore CART
def cart(X, y, atributos, profundidade=0, max_profundidade=5, min_samples=5):
    # Caso base: folha pura ou poucas amostras
    if len(np.unique(y)) == 1:
        return np.unique(y)[0]
    if len(y) < min_samples or profundidade == max_profundidade:
        return y.mode()[0]

    melhor_attr, melhor_split, melhor_valor = None, 1, None
    is_continuous = False

    for attr in atributos:
        if np.issubdtype(X[attr].dtype, np.number):
            g, limiar = melhor_split_continuo(X[attr], y)
            if g < melhor_split:
                melhor_attr, melhor_split, melhor_valor = attr, g, limiar
                is_continuous = True
        else:
            g, cat = melhor_split_categorico(X[attr], y)
            if g < melhor_split:
                melhor_attr, melhor_split, melhor_valor = attr, g, cat
                is_continuous = False

    if melhor_attr is None:
        return y.mode()[0]

    arvore = {melhor_attr: {}}

    if is_continuous:
        X_left, y_left = X[X[melhor_attr] <= melhor_valor], y[X[melhor_attr] <= melhor_valor]
        X_right, y_right = X[X[melhor_attr] > melhor_valor], y[X[melhor_attr] > melhor_valor]

        arvore[melhor_attr][f"<= {melhor_valor:.2f}"] = (
            cart(X_left, y_left, atributos, profundidade+1, max_profundidade, min_samples)
        )
        arvore[melhor_attr][f"> {melhor_valor:.2f}"] = (
            cart(X_right, y_right, atributos, profundidade+1, max_profundidade, min_samples)
        )
    else:
        X_left, y_left = X[X[melhor_attr] == melhor_valor], y[X[melhor_attr] == melhor_valor]
        X_right, y_right = X[X[melhor_attr] != melhor_valor], y[X[melhor_attr] != melhor_valor]

        arvore[melhor_attr][f"== {melhor_valor}"] = (
            cart(X_left, y_left, atributos, profundidade+1, max_profundidade, min_samples)
        )
        arvore[melhor_attr][f"!= {melhor_valor}"] = (
            cart(X_right, y_right, atributos, profundidade+1, max_profundidade, min_samples)
        )

    return arvore

# ---------- Rodar no Titanic ----------
X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = df["Survived"]

atributos = list(X.columns)
arvore_cart = cart(X, y, atributos)

print(arvore_cart)
