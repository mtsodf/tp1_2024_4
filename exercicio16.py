# Exercício 16
"""
Um carro foi monitorado via gps para testes de desempenho de velocidade.
Ele viajou entre duas cidades A e B.
Com isso foram gerados os seguintes dados:
    - tempos: lista com o duração que o carro ficou em determinada velocidade (em segundos)
    - velocidades: lista com as respectivas velocidades relativas aos tempos anteriores(em km/h)

Por exemplo,
tempos = [120, 60]
velocidades = [80, 100]
significa que o carro ficou 120 segundos a 80 km/h e 60 segundos a 100 km/h.

Com base nessas listas calcule

a) O tempo de percuso total (em segundos)
b) A distância entre as duas cidades
c) A velocidade média do percurso
"""

import random

tempos = [random.uniform(60, 300) for _ in range(40)]
velocidades = [random.normalvariate(100, 20) for _ in range(40)]
velocidades = [v if v > 0 else 0 for v in velocidades]
