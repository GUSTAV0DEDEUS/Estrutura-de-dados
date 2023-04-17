# Fila circular
> Lição do Lobiano, matéria estrutura de dados

Descrição: Uma fila circular e caracterizada por ser preenchida de forma que o último item é adicionado até chegar ao limite da fila, com isso ao retirar o primeiro esse local passa a ser preenchido com o ultimo e o inicio sendo +1.

[Aula explicando esse conceito de maneira simples](https://www.youtube.com/watch?v=QCb6k2nik5k&ab_channel=ProfessorIsidro)

## Código
> Variáveis de ambiente (fila [], int inicio, int fim, int quantidade e int tamanho = 10)

Começamos com o código, a lógica por trás da fila e a seguinte:

- A lista contém no máximo 10 itens 
-  Ao remover o inicio, o fim devera ocupar esse novo local
- Ao sair do sistema listar
- Percorrer essa fila e mostrar o começo dela
```python
if(quantidade != tamanho):
    valor = int(input("Adicionar: "))
    fim = int((fim) % tamanho)
    fila.insert(fim, valor)
    quantidade += 1
    fim += 1
  else:
    print("Fila cheia")
    
```
### Descrição
Esse código funciona por causa do fim sendo igual a 0 adiciono ao primeiro índice do fila(array), depois adiciono 1 ao fim e a quantidade. O if serve para validar o tamanho do array, ou seja, quando quantidade for igual a tamanho(10), a função adicionar retorna o else(fila cheia)

```python
  if(len(fila) == 0):
    print("Não a itens a remover")
  else:
    remover = (inicio) % quantidade
    item = fila.pop(remover)
    print("Item removido: "+str(item))
    quantidade -= 1
    inicio += 1
```
### Descrição
Nesse caso temos o inicio sendo igual 0, com isso a função pop remove o índice, depois incrementamos ao inicio + 1 e diminuímos a quantidade - 1, com isso podemos adicionar mais elementos até atingir o tamanho total.

```pyton
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
```
### Descrição
> O professor mandou mostrar o inicio e fim da fila por isso o if.

A função listar percorre a quantidade da fila, para retornar na cli os items da fila(array)