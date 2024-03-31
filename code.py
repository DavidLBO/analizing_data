import pandas as pd

tabela = pd.read_csv("cancelamentos_sample.csv")
tabela = tabela.drop("CustomerID", axis=1)
display(tabela)

# IDENTIFICANDO E REMOVENDO VALORES VAZIOS
display(tabela.info())
tabela = tabela.dropna()
display(tabela.info())

# QUANTAS PESSOAS CANCELARAM?
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))

# QUAL A DIVISÃO ENTRE AS OPÇÕES DE CONTRATO?
display(tabela["duracao_contrato"].value_counts(normalize=True).map("{:.2%}".format))
display(tabela["duracao_contrato"].value_counts())

# ANALISANDO AS INFORMAÇÕES PARA OS CONTRATOS MENSAIS
display(tabela.groupby("duracao_contrato").mean(numeric_only=True))

# PRATICAMENTE TODOS OS CONTRATOS MENSAIS CANCELARAM

# VAMOS SIMULAR A SITUAÇÃO CASO A EMPRESA RETIRE O CONTRATO MENSAL
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
display(tabela)
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))

display(tabela["assinatura"].value_counts(normalize=True))
display(tabela.groupby("assinatura").mean(numeric_only=True))
# VALORES DE CANCELAMENTO MUITO PARECIDOS PARA ACHAR UMA INFORMAÇÃO VIÁVEL


# FUNCIONA COMO ESPERADO APENAS PARA ARQUIVOS .ipynb
import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou", width=600)
    grafico.show()



tabela = tabela[tabela["ligacoes_callcenter"]<5]
tabela = tabela[tabela["dias_atraso"]<=20]
display(tabela)
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))

# COM ISSO TEMOS UMA QUEDA DE 56% PARA 18% NA TAXA DE CANCELAMENTO
# OUTROS AJUSTES PODERIAM SER FEITOS COM IDADE OU TOTAL GASTO, 
# MAS A VIABILIDADE DESSAS ALTERAÇÕES DEIXARIA A DESEJAR
