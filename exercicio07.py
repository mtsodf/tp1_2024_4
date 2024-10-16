# Exercício 07
"""
A sequencia de fibonacci é uma sequencia de números inteiros onde cada número é a soma dos dois números anteriores.
Os dois primeiros números da sequencia são 0 e 1.
Ou seja, a sequencia começa com 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Escreva uma função que receba um número inteiro n e calcule o n-ésimo número da sequencia de fibonacci.

Exemplo:
    fibonacci(0) deve retornar 0
    fibonacci(1) deve retornar 1
    fibonacci(2) deve retornar 1
    fibonacci(3) deve retornar 2
    fibonacci(4) deve retornar 3
    fibonacci(5) deve retornar 5
"""


def fibonacci(n):
    # Escreva seu código aqui
    pass


def main():
    # Teste sua função com os exemplos fornecidos
    print(f"fibonacci(0) = {fibonacci(0)}")  # Esperado: 0
    print(f"fibonacci(1) = {fibonacci(1)}")  # Esperado: 1
    print(f"fibonacci(2) = {fibonacci(2)}")  # Esperado: 1
    print(f"fibonacci(3) = {fibonacci(3)}")  # Esperado: 2
    print(f"fibonacci(4) = {fibonacci(4)}")  # Esperado: 3
    print(f"fibonacci(5) = {fibonacci(5)}")  # Esperado: 5


if __name__ == "__main__":
    main()
