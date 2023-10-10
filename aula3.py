valor1 = 1
valor2 = 2
valor3 = 3

if (valor1 < valor2 and valor1 < valor3):
    print("valor 1 é o menor valor")

    ##########################################
# Defina as variáveis A e B como True ou False
1 = [True, False]
2 = [True, False]

# Cabeçalho da tabela verdade
print("1   2   Resultado")

# Loop através de todas as combinações possíveis de A e B
for a in 1:
    for b in 2:
        resultado = a or b  # Operação lógica "OR" entre A e B
        print(f"{a}   {b}   {resultado}")
