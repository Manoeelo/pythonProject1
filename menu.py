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
            print('{:0>3}'.format(num))


    #estrutura de identificação / execução de script

if __name__ == '__main__':
    continua = 'C'

    while continua.upper() != 'Z':
        print('########################################')
        print('#                                      #')
        print('#     M E N U   D E   O P Ç Õ E S      #')
        print('#                                      #')
        print('#    01 - Olá Mundo                    #')
        print('#    02 - Área do Retângulo            #')
        print('#    03 - Área do Quadrado             #')
        print('#    04 - Área do Triângulo            #')
        print('#    05 - Contagem Progressiva         #')
        print('#    06 - Apoiar Candidato             #')
        print('#    07 - Brincar de Plim              #')
        print('#                                      #')
        print('#    Z - Sair                          #')
        print('#                                      #')
        print('########################################')

    resposta = input('Escolha sua opção')
    print(f'A sua escolha foi {resposta}')

    if resposta.upper() != 'Z':
        if resposta == '1':
            print_hi('PyCharm')
        elif resposta == '2':
            resultado = calcular_area_do_retangulo(8,7)
            print(f'A área do retángulo é de {resultado} m²')
        elif resposta == '3':
            resultado = calcular_area_do_quadrado(7)
            print(f'A área do quadrado é de {resultado} m²')
        elif resposta == '4':
            resultado = calcular_area_do_triangulo(4,2)
            print(f'A área do triângulo é de {resultado} m²')
        elif resposta == '5':
            contagem_progressiva(fim)
        elif resposta == '6':
            apoiar_candidato('Fake', 4)
        elif resposta == '7':
            brincar_de_plim(7)
        else:
            print('opção inválida. Escolha uma opção de 1 a 7')
    else:
        print('Você escolheu sair, volte sempre!')