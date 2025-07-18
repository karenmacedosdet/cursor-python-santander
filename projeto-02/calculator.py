"""Calculadora simples interativa."""


def calcular(operacao, num1, num2):
    """Calcula o resultado da operação entre dois números."""
    try:
        if operacao == 'adição':
            return num1 + num2
        elif operacao == 'subtração':
            return num1 - num2
        elif operacao == 'multiplicação':
            return num1 * num2
        elif operacao == 'divisão':
            try:
                return num1 / num2
            except ZeroDivisionError:
                return 'Erro: divisão por zero.'
        else:
            return 'Operação inválida.'
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    while True:
        operacao = input(
            "Digite a operação (adição, subtração, multiplicação, divisão) "
            "ou 'saída' para encerrar: "
        ).strip().lower()
        if operacao == 'saída':
            print("Programa encerrado.")
            break
        if operacao not in [
            'adição', 'subtração', 'multiplicação', 'divisão'
        ]:
            print("Operação inválida. Tente novamente.")
            continue
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números válidos.")
            continue
        resultado = calcular(operacao, num1, num2)
        print(f"Resultado: {resultado}")

    # Testes
    print(calcular('adição', 1, 2))
    print(calcular('subtração', 1, 2))
    print(calcular('multiplicação', 1, 2))
    print(calcular('divisão', 1, 2))
    print(calcular('divisão', 1, 0))
    print(calcular('divisão', 1, 'a'))

    