# Exercício 15
"""
Escreva uma função para cálculo da mediana e outra função para o cálculo da média.
A função que calcula a mediana deve receber uma lista de números e retornar a mediana.
A função que calcula a média deve receber uma lista de números e retornar a média.

A mediana é o valor que separa a metade maior e a metade menor de um conjunto de dados.
Caso a quantidade de valores seja ímpar a mediana é o valor central, caso contrário é a média dos dois valores centrais.

Por exemplo:
mediana([1, 2, 3, 4, 5]) -> 3
mediana([1, 2, 3, 4, 5, 6]) -> 3.5


A média é o valor obtido pela soma de todos os valores dividido pela quantidade de valores.

Dica: Para o calculo da mediana, utilize é mais fácil ordenar a lista de números.
"""


def mediana(lista):
    # Escreva seu código aqui
    pass


def media(lista):
    # Escreva seu código aqui
    pass


def main():
    # Teste suas funções com os exemplos fornecidos
    listas = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 10, 12], [1, 2, 3, 4, 100]]

    for lista in listas:
        print(f"Lista: {lista} | Mediana: {mediana(lista)} | Média: {media(lista)}")


if __name__ == "__main__":
    main()
