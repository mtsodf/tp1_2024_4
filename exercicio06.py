# Exercício 06
"""
Escreva uma função para contar a quantidade de vogais em uma string. Adicione documentação a função usando docstrings no início da função
"""


def contar_vogais(uma_string):
    # Escreva seu código aqui
    pass


def main():
    # Não mexa nessa função

    testes = [
        ("hello", 2),
        ("world", 1),
        ("", 0),
        ("AEIOU", 5),
        ("bcdfg", 0),
        ("Python Programming", 4),
        ("12345", 0),
        ("aeiouAEIOU", 10),
        ("Vogais e Consoantes", 7),
    ]

    acertos = 0
    erros = 0

    for entrada, esperado in testes:
        try:
            resultado = contar_vogais(entrada)
            if resultado == esperado:
                acertos += 1
            else:
                erros += 1
                print(f"Erro: ({entrada}) = {resultado}, esperado {esperado}")
        except:
            print(f"Erro: ({entrada}). Lançamento de exceção")
            erros += 1
            import traceback

            traceback.print_exc()

    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")


if __name__ == "__main__":
    main()
