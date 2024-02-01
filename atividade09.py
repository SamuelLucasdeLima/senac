
agenda = []

# Função para adicionar um contato
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contato = {"Nome": nome, "Telefone": telefone, "Email": email}
    agenda.append(contato)
    print("Contato adicionado com sucesso!")

# listar todos os contatos
def listar_contatos():
    if not agenda:
        print("A agenda está vazia.")
    else:
        for contato in agenda:
            print(f"Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}")

#  contato por nome
def pesquisar_contato():
    nome = input("Digite o nome do contato que deseja pesquisar: ")
    encontrado = False
    for contato in agenda:
        if contato["Nome"].lower() == nome.lower():
            print(f"Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}")
            encontrado = True
            break
    if not encontrado:
        print("Contato não encontrado na agenda.")

# Loop principal do programa
while True:
    print("\nMenu:")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Pesquisar Contato")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1/2/3/4): ")
    
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        pesquisar_contato()
    elif opcao == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
