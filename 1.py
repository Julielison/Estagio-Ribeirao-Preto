def is_fibonacci(num):
    # Inicializa os primeiros números da sequência
    a, b = 0, 1
    
    # Verifica se o número informado é 0 ou 1, que fazem parte da sequência
    if num == 0 or num == 1:
        return True
    
    # Calcula a sequência até que o número informado seja encontrado ou até que a sequência ultrapasse o número
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    
    return False

# Entrada do usuário
num = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

# Verifica se o número pertence à sequência de Fibonacci e exibe a mensagem correspondente
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
