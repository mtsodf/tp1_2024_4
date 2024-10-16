# Exercício 09
"""
Função para encontrar números duplicados em uma lista:
Crie uma função que receba uma lista de números e retorne uma lista com os números que aparecem mais de uma vez.
A lista não pode ter elementos duplicados e a ordem dos números na lista de retorno deve ser a mesma ordem em que aparecem na lista original.
Adicione docstring para documentar a função.
"""


def encontrar_duplicados(lista):
    # Escreva seu código aqui
    pass


def main():
    # Teste sua função com os exemplos fornecidos
    print(encontrar_duplicados([1, 2, 3, 4, 5, 6]))  # Esperado: []
    print(encontrar_duplicados([1, 2, 3, 4, 5, 6, 1]))  # Esperado: [1]
    print(encontrar_duplicados([1, 2, 3, 4, 5, 6, 1, 2]))  # Esperado: [1, 2]
    print(encontrar_duplicados([1, 2, 3, 4, 5, 6, 1, 2, 3]))  # Esperado: [1, 2, 3]
    print(encontrar_duplicados([1, 2, 3, 4, 5, 6, 1, 2, 3, 4]))  # Esperado: [1, 2, 3, 4]


if __name__ == "__main__":
    main()
