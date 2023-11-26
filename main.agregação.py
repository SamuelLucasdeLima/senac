
from agregação import CarrinhoDeCompras, Produto

def main():
    carrinho = CarrinhoDeCompras()

    while True:
        print("\nEscolha uma ação:")
        print("1. Adicionar produto ao carrinho")
        print("2. Listar produtos no carrinho")
        print("3. Calcular total da compra")
        print("4. Sair")

        escolha = input("Opção: ")

        if escolha == "1":
            nome_produto = input("Digite o nome do produto: ")
            preco_produto = float(input("Digite o preço do produto: "))
            produto = Produto(nome_produto, preco_produto)
            carrinho.inserirProduto(produto)
        elif escolha == "2":
            carrinho.listarProdutos()
        elif escolha == "3":
            total = carrinho.totalDaCompra()
            print("Total da compra: $", total)
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
