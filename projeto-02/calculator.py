"""Calculadora simples interativa."""


def calcular(operacao: str, num1: float, num2: float | str) -> float | str:
    """Calcula o resultado da operação entre dois números."""
    try:
        num2_float = float(num2)
        if operacao == "adição":
            return num1 + num2_float
        elif operacao == "subtração":
            return num1 - num2_float
        elif operacao == "multiplicação":
            return num1 * num2_float
        elif operacao == "divisão":
            try:
                return num1 / num2_float
            except ZeroDivisionError:
                return "Erro: divisão por zero."
        else:
            return "Operação inválida."
    except (TypeError, ValueError) as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    while True:
        operacao_input = (
            input(
                "Digite a operação (adição, subtração, multiplicação, "
                "divisão) ou 'saída' para encerrar: "
            )
            .strip()
            .lower()
        )
        if operacao_input == "saída":
            print("Programa encerrado.")
            break
        if operacao_input not in [
            "adição",
            "subtração",
            "multiplicação",
            "divisão",
        ]:
            print("Operação inválida. Tente novamente.")
            continue
        try:
            valor1 = float(input("Digite o primeiro número: "))
            valor2 = float(input("Digite o segundo número: "))
        except ValueError:
            print(
                "Entrada inválida. Certifique-se de digitar números válidos."
            )
            continue
        resultado = calcular(operacao_input, valor1, valor2)
        print(f"Resultado: {resultado}")

    # Testes
    print(calcular("adição", 1, 2))
    print(calcular("subtração", 1, 2))
    print(calcular("multiplicação", 1, 2))
    print(calcular("divisão", 1, 2))
    print(calcular("divisão", 1, 0))
    print(calcular("divisão", 1, "a"))
