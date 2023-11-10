#exemplo de Series
import numpy as np
import pandas as pd
dados = ("muito bom", "bom", "normal", "ruim", "pessimo")
indices = (5,4,3,2,1)

x = pd.Series(data=dados, index=indices)
print(x)

print(x[5:3])

#Series: a partir de um dicionário
avaliacaoDict = {5:"muito bacana", 
                4:"bacaninha",
                3:"normal", 
                2:"ruim",
                1:"pessimo"}

avaliacaoSeries = pd.Series(avaliacaoDict)
print(avaliacaoSeries)

#declarando todos os valores iguais
valorIgual = pd.Series(5, index=indices)
print(valorIgual)

#DataFrame
x = pd.DataFrame([2,3,4,5,6], columns = ["numeros"])
print(x)

#com duas colunas
print(pd.DataFrame({"nomes": ["amanda", "carol", "andre", "claudia"], "idades":[23,23,30,50]}))
y = pd.DataFrame({"nomes": ["amanda", "carol", "andre", "claudia"], "idades":[23,23,30,50]})

#soma todos os valores de uma coluna
print(y["idades"].sum())

#criando novas colunas
y["sexo"] = ["feminino", "feminino","masculino","feminino",]
print(y)

y["idade x 2"] = y["idades"] * 2
print(y)