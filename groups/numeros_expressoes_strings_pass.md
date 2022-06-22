# **Comando Pass**
### Descrição Simplificada:
O comando pass é um comando nulo. Basicamente, ele não realiza nenhuma operação.



### Descrição Detalhada:

#### Uso

Como este comando não resulta em nenhuma operação ou alteração, ele é usado para "pular" alguma etapa do código.

**Exemplo:**
Abaixo, temos um trecho de código incompleto:

- `entrada`
~~~~~python
1   print('Vou contar até 4, olha só: ')
2   lista = [1, 2, 4]
3   for i in lista:
4       if i == 4:
5           ##print('3')
6       print(i)
7   print('Viu?')
~~~~~
Falta acrescentar o que acontece na linha 5. Tentar rodar um código com partes incompletas, como a do exemplo acima, pode resultar em vários erros, dependendo do caso. 
- `saída`
        
        File "C:/Users/exemplo.py", line 6
        print(i)
        ^
        IndentationError: expected an indented block

        Process finished with exit code 1
    
Por isso, utilizar o comando pass neste trecho seria o indicado, para que o as outras partes do código rodem, e a parte incompleta seja "passada".

- `entrada`
~~~~~python
1   print('Vou contar até 4, olha só: ')
2   lista = [1, 2, 4]
3   for i in lista:
4       if i == 4:
5       pass
6       print(i)
7   print('Viu?')
~~~~~
- `saída`

        "C:\Users\exemplo.py"
        Vou contar até 4, olha só: 
        1
        2
        4
        Viu?

Desta forma, ainda que falte o "print('3')" na linha 5, que faria com que a saída fosse 
    
    Vou contar até 4, olha só:
    1
    2
    3
    4
    Viu?
    
, ainda obtemos uma saída, sem receber nenhuma mensagem de erro devido a um trecho ainda não implementado.






