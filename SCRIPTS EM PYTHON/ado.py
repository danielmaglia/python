usuarios = {}  
produtos = {   
    1: ('Camiseta', 49.90),
    2: ('Calça Jeans', 99.90),
    3: ('Tênis', 199.90),
    4: ('Relógio', 299.90)
}
carrinhos = {}  
compras = {}    

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite uma senha para o usuário: ")
    id_usuario = len(usuarios) + 1  
    usuarios[id_usuario] = {'nome': nome, 'senha': senha}
    print(f"Usuário {nome} cadastrado com sucesso!\n")
    return id_usuario

def login_usuario():
    print("Faça login")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    for id_usuario, usuario in usuarios.items():
        if usuario['nome'] == nome and usuario['senha'] == senha:
            print(f"Bem-vindo, {nome}!\n")
            return id_usuario
    print("Usuário ou senha incorretos. Tente novamente.")
    return None

def buscar_produto():
    print("Produtos disponíveis:")
    for id_produto, produto in produtos.items():
        nome, preco = produto
        print(f"ID: {id_produto} - {nome} - R${preco:.2f}")
    print("\n")

def adicionar_ao_carrinho(id_usuario):
    if id_usuario not in carrinhos:
        carrinhos[id_usuario] = {'produtos': [], 'total': 0.0}
    
    while True:
        buscar_produto()
        id_produto = int(input("Digite o ID do produto que você deseja adicionar ao carrinho (0 para sair): "))
        if id_produto == 0:
            break
        if id_produto in produtos:
            quantidade = int(input(f"Digite a quantidade de {produtos[id_produto][0]}: "))
            carrinhos[id_usuario]['produtos'].append((id_produto, quantidade))
            carrinhos[id_usuario]['total'] += produtos[id_produto][1] * quantidade
            print(f"Produto {produtos[id_produto][0]} adicionado ao carrinho.\n")
        else:
            print("Produto inválido. Tente novamente.")

def realizar_pagamento(id_usuario):
    if id_usuario not in carrinhos or len(carrinhos[id_usuario]['produtos']) == 0:
        print("Carrinho vazio. Adicione produtos ao carrinho primeiro.\n")
        return
    
    total = carrinhos[id_usuario]['total']
    print(f"Total do carrinho: R${total:.2f}")
    pagamento = float(input("Digite o valor para pagamento: R$"))
    if pagamento >= total:
        troco = pagamento - total
        print(f"Compra realizada com sucesso! Seu troco é R${troco:.2f}")
        
        if id_usuario not in compras:
            compras[id_usuario] = []
        for produto_id, quantidade in carrinhos[id_usuario]['produtos']:
            nome_produto = produtos[produto_id][0]
            compras[id_usuario].append({
                'produto': nome_produto,
                'quantidade': quantidade,
                'total': produtos[produto_id][1] * quantidade
            })
        
        carrinhos[id_usuario] = {'produtos': [], 'total': 0.0}
    else:
        print("Valor insuficiente. Tente novamente.\n")

def consultar_compras(id_usuario):
    if id_usuario not in compras or len(compras[id_usuario]) == 0:
        print("Você ainda não fez nenhuma compra.\n")
        return
    
    print("Histórico de compras:")
    for compra in compras[id_usuario]:
        print(f"Produto: {compra['produto']} - Quantidade: {compra['quantidade']} - Total: R${compra['total']:.2f}")
    print("\n")

def main():
    print("Bem-vindo à Loja Virtual!\n")
    id_usuario = None
    while True:
        print("1. Cadastro de Usuário")
        print("2. Login de Usuário")
        print("3. Buscar Produtos")
        print("4. Montar Carrinho de Compras")
        print("5. Realizar Pagamento")
        print("6. Consultar Compras")
        print("7. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            id_usuario = login_usuario()
        elif opcao == 3:
            buscar_produto()
        elif opcao == 4:
            if id_usuario is not None:
                adicionar_ao_carrinho(id_usuario)
            else:
                print("Faça login primeiro.\n")
        elif opcao == 5:
            if id_usuario is not None:
                realizar_pagamento(id_usuario)
            else:
                print("Faça login primeiro.\n")
        elif opcao == 6:
            if id_usuario is not None:
                consultar_compras(id_usuario)
            else:
                print("Faça login primeiro.\n")
        elif opcao == 7:
            print("Saindo da loja virtual...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
