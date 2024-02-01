
from associação import Escritor, Computador, MaquinaDeDatilografia

def main():
    nome_escritor = input("Digite o nome do escritor: ")
    marca_computador = input("Digite a marca do computador: ")
    ano_maquina = int(input("Digite o ano da máquina de datilografia: "))

    escritor = Escritor(nome_escritor)
    computador = Computador(marca_computador)
    maquinaDeDatilografia = MaquinaDeDatilografia(ano_maquina)

    print(f"Escritor: {escritor.getNome()}")
    print(f"Marca do Computador: {computador.getMarca()}")
    print(f"Ano da Máquina de Datilografia: {maquinaDeDatilografia.getAnoDeFabricacao()}")

    escolha = input("Escolha 1 para usar o computador ou 2 para usar a máquina de datilografia: ")
    if escolha == "1":
        escritor.setInstrumentoDeTrabalho(computador)
    elif escolha == "2":
        escritor.setInstrumentoDeTrabalho(maquinaDeDatilografia)
    else:
        print("Escolha inválida. Usando o computador por padrão.")

    instrumento = escritor.getInstrumentoDeTrabalho()
    if instrumento:
        instrumento.escrever()
    else:
        print("Nenhum instrumento definido.")

if __name__ == "__main__":
    main()
