def mdc(X, Y):
    while Y:
        X, Y = Y, X % Y
    return X

def mmc(X, Y):
    return (X * Y) // mdc(X, Y)

X = 12
Y = 15
print(f"O MMC de {X} e {Y} é:", mmc(X, Y))