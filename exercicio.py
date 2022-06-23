# 3. Crie um algoritmo para uma loja de tintas, o mesmo deve conter um dicionário, que tenha como chaves 
# as seguintes cores: azul, amarelo, verde e vermelho e como valores os respectivos tons para cada cor: 
# 6 tons, 3 tons, 4 tons e 3 tons. Mostre uma exceção para caso o usuário solicite uma cor que não esteja 
# dentre as disponíveis e outra para caso seja pedido um tom diferente dos possíveis na cor em específico.

def main():
    estoqueCores = {
        "azul" : ['1','2','3','4','5','6'],
        "amarelo" : ['1','2','3'],
        "verde" : ['1','2','3','4'],
        "vermelho" : ['1','2','3'],
    }
    try:
        corSolicitada = str(input("Temos azul, amarelo, verde e vermelho no estoque\nDigite a cor desejada: "))
        if corSolicitada not in estoqueCores.keys():
            raise KeyError
        tomSolicitado = str(input("Esta cor possui os tons: %s \nDigite o tom desejado: " %estoqueCores[corSolicitada]))
        if tomSolicitado not in estoqueCores[corSolicitada]:
            raise NameError
    except KeyError:
        print("a cor solicitada não está no estoque")
    except NameError:
        print("o tom solicitado não está no estoque")
    else:
        print("Obrigado, excelente escolha")
        
if __name__ == '__main__':
    main()