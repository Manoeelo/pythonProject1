# imports - bibliotecas
import pytest

# 2 - class - classes

# 3 - definitions - definições = métodos e funções

# Cada "def" é um metódo
def print_hi(name):
    print(f'Hi, {name}')

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2

def contagem_progressiva(fim):
    for num in range(fim): #repetir o bloco de zero até o fim
        print(num)         #exibi o número

#def contagem_regressiva(inicio, fim):

# forma 1
#def apoiar_candidato(nome, vezes):
 #   for num in range(vezes):
  #      contador = num + 1
   #     print(f'{contador} - {nome}')

#forma 2 (antigo)
#def apoiar_candidato(nome, vezes):
 #   for num in range(vezes):
  #      print(num + 1, ' - ', nome)

#forma 3 com 0 entre 1 a 9 if else para alinhamento de casas decimais e nome.
def apoiar_candidato(nome, vezes):
    for num in range(vezes):
        if num < 9:
            print(f'00{num + 1} - {nome}')
        elif num < 99:
            print(f'0{num + 1} - {nome}')
        else:
            print(f'{num + 1} - {nome}')

def brincar_de_plim(fim):
    for num in range(fim):
        if  num % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>9}'.format(num))

def exibir_dia_da_semana_if(num):
    print("IF")
    if num == 1:
        print('O dia é segunda')
    elif num == 2:
        print('O dia é terça')
    elif num == 3:
        print('O dia é quarta')
    elif num == 4:
        print('O dia é quinta')
    elif num == 5:
        print('O dia é sexta')
    elif num == 6:
        print('O dia é sábado')
    elif num == 7:
        print('O dia é domingo')
    else:
        print('Número inválido. Digite um número de 1 a 7')
''' Ativo na versão 3.10
def exibir_dia_da_semana_match(num):
    print('MATCH')
    match num:
        case 1:
            print('O dia é segunda')
            exit()
        case 2:
            print('O dia é terça')
            exit()
        case 3:
            print('O dia é quarta')
            exit()
        case 4:
            print('O dia é quinta')
            exit()
        case 5:
            print('O dia é sexta')
            exit()
        case 6:
            print('O dia é sábado')
            exit()
        case 7:
            print('O dia é domingo')
            exit()
        case _:
            print('Número inválido. Digite um número de 1 a 7')
            '''

def brinca_de_para_ou_continua():
    resposta = 'C' # aqui 'C' significa q continua

    #while resposta == 'C' or 'c':
    while resposta.upper() == 'C':
        resposta = input('Digite P para para ou C para continuar ')

    print('Você decidiu parar de brincar')

    # estrutura de identificação / execução de script
if __name__ == '__main__':
    print_hi('PyCharm')

    #chamar a função de cálculo da área do retângulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'O retângulo tem a área de {resultado} m²')

    #chamar a função de cálculo da área do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é de {resultado} m²')

    #chamar a função de cálculo de área do triángulo
    resultado = calcular_area_do_triangulo(6,7)
    print(f'a área do triángulo é de {resultado} m²')

    #executar uma contagem progressiva
    contagem_progressiva(10)

    #exibir o nome do candidato varias vezes.
    apoiar_candidato('Fake', 19)

    #PLIM
    brincar_de_plim(100)

    #exemplo de dia da semana com if - elif - else
    exibir_dia_da_semana_if(1)

    #exemplo de dia da semana com match - case
    #exibir_dia_da_semana_match(1)

    #exemplo com while - para ou continua
    brinca_de_para_ou_continua()