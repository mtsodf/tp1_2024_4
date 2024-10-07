"""
Você está desenvolvendo um código para um sistema de loteria.
Você deve implementar uma função para receber uma quantidade de jogos e o jogo sorteado e 
retornar a quantidade de acertos de cada jogo.
O vetor de jogos é uma lista de listas, onde cada lista representa um jogo e contém de 6 a 10 números inteiros.
O jogo sorteado é uma lista de 6 números inteiros.
Cada número de um jogo é um inteiro entre 1 e 60, inclusive.
A função deve retornar uma lista de inteiros, onde cada inteiro representa a quantidade de acertos de um jogo.
Exemplos:
    jogos = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
    sorteio = [1, 2, 3, 4, 5, 6]
    verificar_acertos(jogos, sorteio) deve retornar [6, 0]
"""


def verificar_acertos(jogos, sorteio):
    # Escreva seu código aqui
    pass


if __name__ == "__main__":
    jogos = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [1, 2, 3, 7, 8, 9]]
    sorteio = [1, 2, 3, 4, 5, 6]

    resultados = verificar_acertos(jogos, sorteio)

    if resultados == [6, 0, 3]:
        print("Passou no teste")
    else:
        print("Não passou no teste")
