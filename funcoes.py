import random

def rolar_dados(numero):

   lista = []

   for i in range(numero):
       lista.append(random.randint(1,6))
  
   return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar)
    
    dado = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado)
    del dados_rolados[dado_para_guardar]

    saida = [dados_rolados, dados_no_estoque]

    return saida

