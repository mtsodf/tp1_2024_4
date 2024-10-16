# Exercício 10
"""
Função para verificar se uma lista está ordenada:
Crie uma função que verifique se uma lista de números está em ordem crescente.
Retorne True se estiver ou False se não estiver.
"""


def esta_ordenada(lista):
    # Escreva seu código aqui
    pass


def main():
    # Teste sua função com os exemplos fornecidos
    print(esta_ordenada([1, 2, 3, 4, 5, 6]))  # Esperado: True
    print(esta_ordenada([1, 2, 3, 5, 4, 6]))  # Esperado: False
    print(esta_ordenada([1, 2, 3, 4, 6, 5]))  # Esperado: False
    print(esta_ordenada([1, 2, 3, 4, 5, 5]))  # Esperado: True
    print(esta_ordenada([1]))  # Esperado: True
    print(esta_ordenada([]))  # Esperado: True


if __name__ == "__main__":
    main()
