from app.cadastros import CadastroClientes, CadastroProdutos
from app.relatorios import gerar_relatorio_geral


def cadastrar_cliente(clientes: CadastroClientes) -> None:
    try:
        nome = input("Nome do cliente: ")
        email = input("E-mail do cliente: ")
        id_cliente = int(input("ID do cliente: "))
        cliente = clientes.cadastrar(nome, email, id_cliente)
        print(f"Cliente cadastrado com sucesso: {cliente.nome}")
    except ValueError as erro:
        print(f"Erro ao cadastrar cliente: {erro}")
    except Exception as erro:  # pragma: no cover - proteção final do fluxo
        print(f"Erro inesperado: {erro}")


def listar_clientes(clientes: CadastroClientes) -> None:
    registros = clientes.listar()
    if not registros:
        print("Nenhum cliente cadastrado.")
        return

    print("\nClientes cadastrados:")
    for cliente in registros:
        print(f"ID: {cliente.id} | Nome: {cliente.nome} | E-mail: {cliente.email}")


def buscar_cliente(clientes: CadastroClientes) -> None:
    termo = input("Digite o nome, ID ou e-mail para buscar: ")
    resultado = clientes.buscar(termo)
    if not resultado:
        print("Nenhum cliente encontrado.")
        return

    print("\nResultado da busca:")
    for cliente in resultado:
        print(f"ID: {cliente.id} | Nome: {cliente.nome} | E-mail: {cliente.email}")


def cadastrar_produto(produtos: CadastroProdutos) -> None:
    try:
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        id_produto = int(input("ID do produto: "))
        produto = produtos.cadastrar(nome, preco, id_produto)
        print(f"Produto cadastrado com sucesso: {produto.nome}")
    except ValueError as erro:
        print(f"Erro ao cadastrar produto: {erro}")
    except Exception as erro:  # pragma: no cover - proteção final do fluxo
        print(f"Erro inesperado: {erro}")


def listar_produtos(produtos: CadastroProdutos) -> None:
    registros = produtos.listar()
    if not registros:
        print("Nenhum produto cadastrado.")
        return

    print("\nProdutos cadastrados:")
    for produto in registros:
        print(f"ID: {produto.id} | Nome: {produto.nome} | Preço: R$ {produto.preco:.2f}")


def gerar_relatorio(clientes: CadastroClientes, produtos: CadastroProdutos) -> None:
    print(gerar_relatorio_geral(clientes.listar(), produtos.listar()))


def exibir_menu() -> None:
    print("\n=== Sistema de Cadastro ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Cadastrar produto")
    print("5 - Listar produtos")
    print("6 - Gerar relatório")
    print("0 - Sair")


def main() -> None:
    clientes = CadastroClientes()
    produtos = CadastroProdutos()

    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número de 0 a 6.")
            continue

        if opcao == 1:
            cadastrar_cliente(clientes)
        elif opcao == 2:
            listar_clientes(clientes)
        elif opcao == 3:
            buscar_cliente(clientes)
        elif opcao == 4:
            cadastrar_produto(produtos)
        elif opcao == 5:
            listar_produtos(produtos)
        elif opcao == 6:
            gerar_relatorio(clientes, produtos)
        elif opcao == 0:
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()
