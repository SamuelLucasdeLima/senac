
contatos = {
    'Bob': {'telefone': '987-654-3210', 'email': 'bob@email.com'},
    'Alice': {'telefone': '123-456-7890', 'email': 'alice@email.com'}
}

#atividade 01

#print(contatos['Alice'])

#atividade 02

contatos["Samuel"]={'telefone': '123-654-3210', 'email': 'Samuel@email.com'}
contatos["Judison"]={'telefone': '123-789-3210', 'email': 'Judison@email.com'}
contatos["Kayo"]={'telefone': '123-654-1234', 'email': 'Kayo@email.com'}
contatos["Gabriel"]={'telefone': '789-654-9999', 'email': 'Gabriel@email.com'}
#print(contatos['Samuel'])

#atividade 03

#contatos['Bob']={'email': 'Novobob@email.com'}

#print(contatos)

#atividade 04

#del contatos ['Alice']
#print(contatos['Alice'])

#atividade 05

# Obter as chaves (nomes) em ordem alfabética
nomes_em_ordem = sorted(contatos.keys())

# Exibir os nomes em ordem alfabética
for nome in nomes_em_ordem:
    print(nome)


#atividade 05