# Exercício 13
"""
Desenvolva uma função que receba uma string (senha) e verifique se ela é considerada "forte" 
(contendo pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais).
"""


def verificar_senha(senha):
    # Escreva seu código aqui
    pass


def main():
    # Teste sua função com os exemplos fornecidos
    senhas = [
        "AbTp9!fok",
        "AbTp9 fok",
        "AbTp9!foo",
        "AbTp9!fo",
        "AbTp9!fokA",
        "AbTp9!fokA1",
        "AbTp9!fokA1@",
        "AbTp9!fokA1@#",
    ]

    for senha in senhas:
        resultado = verificar_senha(senha)
        print(f"Senha: {senha:<15} | Forte: {resultado}")


if __name__ == "__main__":
    main()
