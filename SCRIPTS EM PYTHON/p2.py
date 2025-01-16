usuarios = {}
produtos = [("001", "Notebook", 3500.00), 
           ("002", "Mouse", 50.00), 
           ("003", "Teclado", 120.00)]
carrinhos = {}
 
def cadastrar_usuario():
   print("Cadastro de Usuário:")
   username = input("Informe o nome de usuário: ")
   senha = input("Informe a senha: ")
   if username in usuarios:
       print("Usuário já cadastrado!")
   else:
       usuarios[username] = senha
       carrinhos[username] = []
       print("Usuário cadastrado com sucesso!")
 
def login():
   print("Login de Usuário:")

   username = input("Usuário: ")
   senha = input("Senha: ")
   if username in usuarios and usuarios[username] == senha:
       print("Login realizado com sucesso!")
       return username
   else:
       print("Usuário ou senha inválidos!")
       return None
 
def buscar_produtos():
   print("\nProdutos disponíveis:")
   for codigo, nome, preco in produtos:
       print(f"Código: {codigo} | Produto: {nome} | Preço: R$ {preco:.2f}")
 
def montar_carrinho(usuario):
   print("\nMontar Carrinho:")
   buscar_produtos()
   codigo = input("Digite o código do produto para adicionar ao carrinho: ")
   produto = next((p for p in produtos if p[0] == codigo), None)
   if produto:
       carrinhos[usuario].append(produto)
       print(f"Produto {produto[1]} adicionado ao carrinho!")
   else:
       print("Produto não encontrado!")
 
def consultar_carrinho(usuario):
   print("\nCarrinho de Compras:")
   if not carrinhos[usuario]:
       print("Seu carrinho está vazio.")
   else:
       total = 0
       for _, nome, preco in carrinhos[usuario]:
           print(f"Produto: {nome} | Preço: R$ {preco:.2f}")
           total += preco
       print(f"Total: R$ {total:.2f}")
 
def pagamento(usuario):
   print("\nPagamento:")
   consultar_carrinho(usuario)
   if carrinhos[usuario]:
       print("Pagamento realizado com sucesso!")
       carrinhos[usuario].clear()
   else:
       print("Seu carrinho está vazio. Adicione produtos antes de pagar.")
 
def menu(usuario):
   while True:
       print("\nMenu de Opções:")
       print("1. Buscar Produtos")
       print("2. Montar Carrinho")
       print("3. Consultar Carrinho")
       print("4. Realizar Pagamento")
       print("5. Sair")
       opcao = input("Escolha uma opção: ")
       if opcao == "1":
           buscar_produtos()
       elif opcao == "2":
           montar_carrinho(usuario)
       elif opcao == "3":
           consultar_carrinho(usuario)
       elif opcao == "4":
           pagamento(usuario)
       elif opcao == "5":
           print("Saindo...")
           break
       else:
           print("Opção inválida!")
 
while True:
   print("\nBem-vindo à Loja Virtual!")
   print("1. Login")
   print("2. Cadastro")
   print("3. Sair")
   escolha = input("Escolha uma opção: ")
   if escolha == "1":
       usuario_logado = login()
       if usuario_logado:
           menu(usuario_logado)
   elif escolha == "2":
       cadastrar_usuario()
   elif escolha == "3":
       print("Saindo da Loja Virtual. Até mais!")
       break
   else:
       print("Opção inválida!")
 
