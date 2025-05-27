def calcular():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida. Use +, -, * ou /.")

            print(f"Resultado: {resultado}")
            break  # Encerra após operação bem-sucedida

        except ValueError as ve:
            print(f"Erro: {ve}")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

calcular()

