"""
Escreva uma função para que dado uma lista de alunos e suas notas, retorne apenas os alunos que foram aprovados
Os alunos e as notas serão representados como uma lista de listas de duas posições onde a primeira é o nome do aluno
e a segunda é a nota dele, como no exemplo abaixo:

alunos_e_notas = [
["Isaac Newton", 9.0],
["Einstein", 7.0],
["Thomas Edison", 5.5],
["Richard Feymann", 7.2],
["Euclides", 7.0],
]

Para o aluno ser aprovado ele deve obter nota maior que ou igual a 7.0
"""


def encontrar_alunos_aprovados(alunos_e_notas):
    return None


def main():
    # Exemplos de entrada e valores esperados
    testes = [
        (
            [
                ["Isaac Newton", 9.0],
                ["Einstein", 7.0],
                ["Thomas Edison", 5.5],
                ["Richard Feymann", 7.2],
                ["Euclides", 7.0],
            ],
            ["Isaac Newton", "Einstein", "Richard Feymann", "Euclides"],
        ),
        ([["Marie Curie", 8.5], ["Nikola Tesla", 6.0], ["Galileo Galilei", 7.5]], ["Marie Curie", "Galileo Galilei"]),
        ([["Ada Lovelace", 10.0], ["Alan Turing", 6.9]], ["Ada Lovelace"]),
        ([["Charles Darwin", 7.0], ["Gregor Mendel", 7.1]], ["Charles Darwin", "Gregor Mendel"]),
        ([["Leonardo da Vinci", 6.0], ["Aristotle", 5.0]], []),
    ]

    acertos = 0
    erros = 0

    for entrada, esperado in testes:
        try:
            resultado = encontrar_alunos_aprovados(entrada)
            if resultado == esperado:
                acertos += 1
            else:
                erros += 1
                print(f"Erro: encontrar_alunos_aprovados({entrada}) = {resultado}, esperado {esperado}")
        except Exception as e:
            print(f"Erro: encontrar_alunos_aprovados({entrada}). Lançamento de exceção")
            import traceback

            traceback.print_exc()
            erros += 1

    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")


if __name__ == "__main__":
    main()
