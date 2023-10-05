def soma_recursiva(seq):
    # Caso base: se a sequência estiver vazia, a soma é 0.
    if len(seq) == 0:
        return 0
    # Caso recursivo: a soma é o primeiro elemento da sequência mais a soma dos restantes.
    else:
        return seq[0] + soma_recursiva(seq[1:])

# Exemplo de uso:
sequencia = [1, 2, 3, 4, 5]
resultado = soma_recursiva(sequencia)
print("A soma da sequência é:", resultado)