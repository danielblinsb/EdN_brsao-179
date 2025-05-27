def soma(a, b):
    return a + b

def mult(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def square_sum(a ,b):
    return (a + b) ** 2

def execute_op(a, b, func):
    return func(a, b)

# Valores de entrada
a = 2
b = 3

# Execução das operações com saídas explicativas
res_soma = execute_op(a, b, soma)
print(f"Soma de {a} + {b} = {res_soma}")

res_mult = execute_op(a, b, mult)
print(f"Multiplicação de {a} * {b} = {res_mult}")

res_sub = execute_op(a, b, sub)
print(f"Subtração de {a} - {b} = {res_sub}")

res_div = execute_op(a, b, div)
print(f"Divisão de {a} / {b} = {res_div:.2f}")

res_square_sum = execute_op(a, b, square_sum)
print(f"(Soma de {a} + {b})² = {res_square_sum}")

# Resumo final
print("\nResumo das operações:")
print(f"→ Soma: {res_soma}")
print(f"→ Multiplicação: {res_mult}")
print(f"→ Subtração: {res_sub}")
print(f"→ Divisão: {res_div:.2f}")
print(f"→ Quadrado da soma: {res_square_sum}")

