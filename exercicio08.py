# Exercício 08
"""
A sequencia de fibonacci é uma sequencia de números inteiros onde cada número é a soma dos dois números anteriores.
Os dois primeiros números da sequencia são 0 e 1.
Ou seja, a sequencia começa com 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Escreva uma função para calcular a soma dos n primeiros números da sequencia de fibonacci.

Exemplo:
    fibonacci_soma(0) deve retornar 0
    fibonacci_soma(1) deve retornar 1
    fibonacci_soma(2) deve retornar 2
    fibonacci_soma(3) deve retornar 4
    fibonacci_soma(4) deve retornar 7
    fibonacci_soma(5) deve retornar 12


Dica: Utilize a função implementada no exercicio07.py para calcular o n-ésimo número da sequencia de fibonacci.
"""


def fibonacci_soma(n):
    # Escreva seu código aqui
    pass


def main():
    # Teste sua função com os exemplos fornecidos
    print(f"fibonacci_soma(0) = {fibonacci_soma(0)}")  # Esperado: 0
    print(f"fibonacci_soma(1) = {fibonacci_soma(1)}")  # Esperado: 1
    print(f"fibonacci_soma(2) = {fibonacci_soma(2)}")  # Esperado: 2
    print(f"fibonacci_soma(3) = {fibonacci_soma(3)}")  # Esperado: 4
    print(f"fibonacci_soma(4) = {fibonacci_soma(4)}")  # Esperado: 7
    print(f"fibonacci_soma(5) = {fibonacci_soma(5)}")  # Esperado: 12


if __name__ == "__main__":
    main()
