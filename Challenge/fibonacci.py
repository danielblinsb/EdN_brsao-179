def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

# Defina o valor de n
n = 10

# Chama a função para gerar a sequência
resultado = fibonacci(n)

# Exibe o resultado formatado
print("Sequência de Fibonacci:")
print(resultado)

