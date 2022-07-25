# Comando Pass

## Descrição simplificada:

O comando pass é um comando nulo. Basicamente, ele não realiza nenhuma operação.

### Descrição detalhada:

#### Uso

Como este comando não resulta em nenhuma operação ou alteração, ele é usado para
"pular" alguma etapa do código.

**Exemplo:**
Abaixo, temos um trecho de código incompleto:

```python
print('Vou contar até 4, olha só: ')
lista = [1, 2, 4]
for i in lista:
    if i == 4:
        print(i)
print('Viu?')
```
Falta acrescentar o que acontece na linha 5. Tentar rodar um código com partes 
incompletas, como a do exemplo acima, pode resultar em vários erros, dependendo 
do caso. 

Saída:

```
File "C:/Users/exemplo.py", line 6
print(i)
^
IndentationError: expected an indented block

Process finished with exit code 1
```

Por isso, utilizar o comando pass neste trecho seria o indicado, para que o as 
outras partes do código rodem, e a parte incompleta seja "passada".

Código:
  
```python
print('Vou contar até 4, olha só: ')
lista = [1, 2, 4]
for i in lista:
   if i == 4:
   pass
   print(i)
print('Viu?')
```

- `saída`

```
Vou contar até 4, olha só: 
1
2
4
Viu?
```

Desta forma, ainda que falte o `print('3')` na linha 5, que faria com que a 
saída fosse: 

```    
Vou contar até 4, olha só:
1
2
3
4
Viu?
```
    
Ainda obtemos uma saída, e não uma mensagem de erro devido a um trecho ainda 
não implementado.


## Exercícios 

### Observe a imagem que representa a equação

![equacao](
https://github.com/CTISM-Prof-Henry/wikiPythonTerceirao/blob/main/images/equacaohoraria.png
)

Ao passar exercícios de revisão do 1º ano, o professor de física do CTISM solicitou que os 
alunos criassem um código que calculasse a Função horária da posição no Movimento Retilíeno Uniforme, para descobrir a posição final
de um ônibus do transporte coletivo de Santa Maria. Considerando:
* a posição inicial (So) é nula no instante t;
* a velocidade (v) de deslocamento deve ser pedida ao usuário em quilômetros por hora;
* o tempo (t) de viagem deve ser pedida ao usurário em horas.

**Calcule qual a posição final do ônibus no instante de tempo t e imprima na tela:**
* o valor e o tipo da variável da posição final
* o valor da velocidade;
* a quantidade de tempo.

 
#### 2. Observe abaixo um exemplo de uma conta de divisão simples:
![divisao](https://github.com/CTISM-Prof-Henry/wikiPythonTerceirao/blob/main/images/contadivisao.png)
##### Escreva um código que:
- Peça para o usuário um valor tipo int qualquer para A e B
- Utilizando formatação de strings, imprima na tela uma string mostrando:
    * o valor de x
    * o valor de y, com 3 casas após a vírgula
    * o resultado da divisão inteira de A por B

#### 3. Faça um programa que imprima na tela todas as turmas dos cursos técnicos integrados que tem no CTISM e seus números de identificação referentes. 
* Exemplo: Terceiro ano da informática: 433

#### O programa deve utilizar o método format( ) e a notação **.

# Resoluções: 
1.
```python
So = 0
v = float(input('Digite o valor da velocidade em km/h:'))
t = float(input('Digite a quantidade de horas da viagem:'))

S = So + (v * t)

print('A posição final é de:', S, 'km e o tipo de variável é:', type(S))
print('A velocidade era:', v, 'km/h e as horas da viagem foram:', t)
```~

2. 
```~~python
a = int(input('insira o valor de a:'))
b = int(input('insira o valor de b:'))

x = a%b
y = a/b
inteira = a//b

<<<<<<< HEAD
#Exercícios:
1. (sobre números)
2. (sobre strings)
3. 
=======
resultado = ('X é igual a %d, y é igual a %1.3f e o resultado da divisão inteira de A por B é %d')
print(resultado % (x, y, inteira))
``````

3.
```~python
turmas = {'primeiro_eletro': 411, 'segundo_eletro': 421, 'terceiro_eletro': 431,
          'primeiro_mec': 412, 'segundo_mec': 422, 'terceiro_mec': 432,
          'primeiro_info': 413, 'segundo_info': 423, 'terceiro_info': 433}

print('Eletrotécnica'
      '\nPrimeiro ano: {primeiro_eletro:d} \nSegundo ano: {segundo_eletro:d} '
      '\nTerceiro ano: {terceiro_eletro:d}'
      '\n\nMecânica'
      '\nPrimeiro ano: {primeiro_mec:d} \nSegundo ano: {segundo_mec:d} '
      '\nTerceiro ano: {terceiro_mec:d}'
      '\n\nInformática'
      '\nPrimeiro ano: {primeiro_info:d} \nSegundo ano: {segundo_info:d} '
      '\nTerceiro ano: {terceiro_info:d}'.format(**turmas))
```~
