from __future__ import annotations

from app.cadastros import Cliente, Produto


def gerar_relatorio_clientes(clientes: list[Cliente]) -> str:
    linhas = ["Relatório de clientes", "=" * 30]
    if not clientes:
        linhas.append("Nenhum cliente cadastrado.")
        return "\n".join(linhas)

    for cliente in clientes:
        linhas.append(f"ID: {cliente.id} | Nome: {cliente.nome} | E-mail: {cliente.email}")

    return "\n".join(linhas)


def gerar_relatorio_produtos(produtos: list[Produto]) -> str:
    linhas = ["Relatório de produtos", "=" * 30]
    if not produtos:
        linhas.append("Nenhum produto cadastrado.")
        return "\n".join(linhas)

    for produto in produtos:
        linhas.append(f"ID: {produto.id} | Nome: {produto.nome} | Preço: R$ {produto.preco:.2f}")

    return "\n".join(linhas)


def gerar_relatorio_geral(clientes: list[Cliente], produtos: list[Produto]) -> str:
    relatorio = [gerar_relatorio_clientes(clientes), "", gerar_relatorio_produtos(produtos)]
    return "\n".join(relatorio)
