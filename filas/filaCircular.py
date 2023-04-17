# Tamanho máximo de 10 inteiros
# listar() mostrando apenas os elementos
# válidos começando de INI até FIM e imprimindo quantidade

# Erros segundo o gpt
"""
1- O método "remover" está removendo o índice do elemento ao invés do próprio elemento. X
2- O cálculo do índice "remover" no método "remover" está incorreto. Deveria ser (inicio)
% tamanho ao invés de (inicio + 1) % quantidade. X
3- A variável "quantidade" não está sendo atualizada corretamente no método "remover". 
Deveria ser quantidade -= 1 ao invés de quantidade = quantidade - 1. X
4- A variável "fim" não está sendo atualizada corretamente no método "adicionar". 
Deveria ser fim = (fim + 1) % tamanho ao invés de fim += 1. X
5- O método "adicionar" não está tratando o caso de a fila estar cheia corretamente. 
Deveria imprimir uma mensagem informando que a fila está cheia e retornar ao menu, 
sem tentar adicionar um novo elemento. X
6- O tamanho máximo da fila está definido como 10, mas não está sendo verificado
em nenhum lugar do código. Se o usuário tentar adicionar um elemento quando a 
fila estiver cheia, o código vai gerar uma exceção.
"""

fila = []
inicio = 0
fim = 0
quantidade = 0
tamanho = 10
opcao = 0

def menu():
  global opcao
  print ("\nMenu")
  print (41 * "=")
  print ("Digite 0 para sair")
  print ("Digite 1 para adicionar")
  print ("Digite 2 para remover")
  print ("Digite 3 para listar")
  opcao = int(input("Digite o valor: "))
  if (opcao == 0):
    listar()
    print("\nAté mais")
  else:
    if(opcao == 1):
      adicionar()
    elif(opcao == 2):
      remover()
    elif(opcao == 3):
      listar()
    else:
      print("Selecione alguma das opções!")
      menu()

def listar():
  global fila
  global inicio
  global fim
  global quantidade
  print (41*"=")
  print("Listar")
  print (41*"=")
  if(len(fila) == 0):
    print("Fila Vazia!")
  else:
    linha = ""
    for i in range(0, 10):
      if(i == inicio):
        linha += ("   0|" )
        continue
      if(i == fim):
        linha += ("  10|" )
        continue
      linha += ("   i|")
    print(linha)
    linha = ""
    for i in range(0, quantidade):
      linha += ("%4d|"%fila[i])
    print(linha)
  menu()
  
def remover():
  global fila
  global inicio
  global quantidade
  print (41*"=")
  print("Remover")
  print (41*"=")
  if(len(fila) == 0):
    print("Não a itens a remover")
  else:
    remover = (inicio) % quantidade
    item = fila.pop(remover)
    print("Item removido: "+str(item))
    quantidade -= 1
    inicio += 1
  menu()
  
def adicionar():
  global fila
  global inicio
  global fim
  global quantidade
  global tamanho
  print (41*"=")
  print("Adicionar")
  print (41*"=")
  if(quantidade != tamanho):
    valor = int(input("Adicionar: "))
    fim = int((fim) % tamanho)
    fila.insert(fim, valor)
    quantidade += 1
    fim += 1
  else:
    print("Fila cheia")
    
  menu()
  
menu()