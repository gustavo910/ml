import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def marks_prediction(hrs):
    #lendo os modelos

    X=pd.read_csv("Linear_X_Train.csv")
    y=pd.read_csv("Linear_Y_Train.csv")

    #capturando os valores
    X=X.values
    y=y.values

    #criando o modelo
    model=LinearRegression()
    model.fit(X,y)


    X_test=np.array(hrs)
    X_test=X_test.reshape(1,-1)

#fazer a previsão do modelo de valor
    return model.predict(X_test)[0]
