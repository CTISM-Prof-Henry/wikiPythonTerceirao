
# Estruturas de Dados
## Sets (Conjuntos) 
#### Simplificado:
* dados inumerados, ou seja, não possui ordem fixa.
* Podem ser realizadas operações matemáticas como união, intersecção e diferença
Utilizações comuns:
* verificar existências de objetos dentro de conjuntos diferentes
* eliminar objetos duplicados

#### Expandido: 
Os conjuntos são definições de uma coleção de dados que não possuem sequência pré definida e também são mutáveis, assim, podendo adicionar mais itens dentro da coleção ao longo do código python. Os sets também possibilitam operações matemáticas como a união, intersecção, diferença e diferença simétrica de conjuntos. Veja os exemplos:

### INTERSECÇÃO:
```
sorvete = {'creme', 'chocolate', 'avela', 'chocomenta', 'blue ice'}  # definindo o primeiro conjunto
print('Conjunto Sorvete: ',sorvete)  # mostrando na tela
milk_shake = {'chocolate', 'morango', 'baunilha', 'flocos', 'avela'}  # definindo o segundo conjunto
print('Conjunto Milk Shake', milk_shake)  # mostrando na tela
sabores_em_comun = sorvete.intersection(milk_shake)  # realizando a intersecção dos conjuntos (itens em comun)
print('Sabores em Comum: ', sabores_em_comun)  # mostrando na tela o resultado da união
```
## Saida de tela:
```
Conjunto Sorvete:  {'avela', 'chocolate', 'blue ice', 'creme', 'chocomenta'}
Conjunto Milk Shake {'baunilha', 'flocos', 'avela', 'morango', 'chocolate'}
Sabores em Comum:  {'avela', 'chocolate
```
## UNIÃO:

```sorvete = {'creme', 'chocolate', 'avela', 'chocomenta', 'blue ice'}  # definindo o primeiro conjunto
print('Conjunto Sorvete: ',sorvete)  # mostrando na tela
milk_shake = {'chocolate', 'morango', 'baunilha', 'flocos', 'avela'}  # definindo o segundo conjunto
print('Conjunto Milk Shake', milk_shake)  # mostrando na tela
todos_os_sabores = sorvete.union(milk_shake)  # realizando a uniao dos conjuntos (juntando todos os itens sem repetir os que sao de ambos)
print('Sabores em Comum: ', todos_os_sabores)  # mostrando na tela o resultado da união
```
## SAIDA: 
```
Conjunto Sorvete:  {'chocomenta', 'chocolate', 'creme', 'blue ice', 'avela'}
Conjunto Milk Shake {'flocos', 'baunilha', 'chocolate', 'morango', 'avela'}
Sabores em Comum:  {'chocomenta', 'flocos', 'creme', 'baunilha', 'chocolate', 'morango', 'blue ice', 'avela'}
```
## DIFERENÇA:
```
sorvete = {'creme', 'chocolate', 'avela', 'chocomenta', 'blue ice'}  # definindo o primeiro conjunto
print('Conjunto Sorvete: ', sorvete)  # mostrando na tela
milk_shake = {'chocolate', 'morango', 'baunilha', 'flocos', 'avela'}  # definindo o segundo conjunto
print('Conjunto Milk Shake', milk_shake)  # mostrando na tela
diferença = sorvete.difference(milk_shake)  # realizando a diferença dos conjuntos
print('Diferença: ', diferença)  # mostrando na tela o resultado da união
```
## saída de tela: 
```
Conjunto Sorvete:  {'chocomenta', 'blue ice', 'avela', 'creme', 'chocolate'}
Conjunto Milk Shake {'morango', 'avela', 'baunilha', 'flocos', 'chocolate'}
Diferença:  {'chocomenta', 'blue ice', 'creme'}
```
## Adicionando ou removendo itens:
```
sorvete = {'creme', 'chocolate', 'avela', 'chocomenta', 'blue ice'}  # definindo o primeiro conjunto
print('Conjunto Sorvete: ', sorvete)  # mostrando na tela
milk_shake = {'chocolate', 'morango', 'baunilha', 'flocos', 'avela'}  # definindo o segundo conjunto
print('Conjunto Milk Shake', milk_shake)  # mostrando na tela
sorvete.add('napolitano')  # Adicionando o novo sabor com o comando add
print('Com o sabor novo: ', sorvete)  # mostrando na tela
sorvete.remove('creme')  # removendo um sabor com o comando remove
print('Sem o sabor creme', sorvete
```
## saída de tela: 
```
Conjunto Sorvete:  {'blue ice', 'chocomenta', 'avela', 'chocolate', 'creme'}
Conjunto Milk Shake {'morango', 'flocos', 'baunilha', 'avela', 'chocolate'}
Com o sabor novo:  {'blue ice', 'napolitano', 'chocomenta', 'avela', 'chocolate', 'creme'}
Sem o sabor creme {'blue ice', 'napolitano', 'chocomenta', 'avela', 'chocolate'}
```

