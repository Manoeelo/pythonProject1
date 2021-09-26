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
    apoiar_candidato('Fake', 999)

    #PLIM
    brincar_de_plim(100)