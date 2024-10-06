"""
Complete a funcao calcular_divisores abaixo. A função deve receber um número inteiro e retornar a lista
com todos os divisores do menor para o maior.
"""


def calcular_divisores(n):
    return None


if __name__ == "__main__":
    # Não mexa nessa função

    testes = [
        (1, [1]),
        (6, [1, 2, 3, 6]),
        (15, [1, 3, 5, 15]),
        (28, [1, 2, 4, 7, 14, 28]),
        (100, [1, 2, 4, 5, 10, 20, 25, 50, 100]),
    ]

    acertos = 0
    erros = 0

    for entrada, esperado in testes:
        try:
            resultado = calcular_divisores(entrada)
            if resultado == esperado:
                acertos += 1
            else:
                erros += 1
                print(f"Erro: calcular_divisores({entrada}) = {resultado}, esperado {esperado}")
        except:
            print(f"Erro: calcular_divisores({entrada}). Lançamento de exceção")
            erros += 1
            import traceback

            traceback.print_exc()

    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")
