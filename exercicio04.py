"""
Exercício: Criação de Funções em Python com *args

Objetivo:
Crie uma função chamada `calcular_media` que receba uma quantidade arbitrária de números como parâmetros e retorne a média aritmética desses números.

Instruções:
1. Defina uma função chamada `calcular_media` que aceite uma quantidade arbitrária de parâmetros usando `*args`.
2. Calcule a média aritmética dos números fornecidos.
3. Retorne o valor da média.

Exemplos:
- calcular_media(10, 20, 30) deve retornar 20.0
- calcular_media(5, 7, 9, 11) deve retornar 8.0
- calcular_media(2, 4, 6, 8, 10) deve retornar 6.0

Dicas:
- Lembre-se de usar a divisão para calcular a média.
- Certifique-se de que a função retorne um valor do tipo float.
- Use a função `len` para obter a quantidade de números fornecidos.

Boa sorte!
"""


# Escreva sua função aqui
def calcular_media(*args):
    pass


# Teste sua função com os exemplos fornecidos
print(calcular_media(10, 20, 30))  # Esperado: 20.0
print(calcular_media(5, 7, 9, 11))  # Esperado: 8.0
print(calcular_media(2, 4, 6, 8, 10))  # Esperado: 6.0
