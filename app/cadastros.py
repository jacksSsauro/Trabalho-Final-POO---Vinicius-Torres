from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def _ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


@dataclass
class Cliente:
    id: int
    nome: str
    email: str


@dataclass
class Produto:
    id: int
    nome: str
    preco: float


class CadastroClientes:
    def __init__(self, arquivo: str = "clientes.json") -> None:
        _ensure_data_dir()
        self.arquivo = DATA_DIR / arquivo
        self._clientes = self._carregar()

    def _carregar(self) -> list[Cliente]:
        if not self.arquivo.exists():
            self.arquivo.write_text("[]", encoding="utf-8")
            return []

        try:
            with self.arquivo.open("r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            self.arquivo.write_text("[]", encoding="utf-8")
            return []

        if not isinstance(dados, list):
            return []

        clientes: list[Cliente] = []
        for item in dados:
            try:
                clientes.append(Cliente(**item))
            except TypeError:
                continue
        return clientes

    def salvar(self) -> None:
        with self.arquivo.open("w", encoding="utf-8") as arquivo:
            json.dump([asdict(cliente) for cliente in self._clientes], arquivo, ensure_ascii=False, indent=2)

    def cadastrar(self, nome: str, email: str, id_cliente: int) -> Cliente:
        nome_limpo = nome.strip()
        email_limpo = email.strip()

        if not nome_limpo or not email_limpo:
            raise ValueError("Nome e e-mail são obrigatórios.")

        if any(cliente.id == id_cliente for cliente in self._clientes):
            raise ValueError(f"Já existe um cliente com o ID {id_cliente}.")

        cliente = Cliente(id=id_cliente, nome=nome_limpo, email=email_limpo)
        self._clientes.append(cliente)
        self.salvar()
        return cliente

    def listar(self) -> list[Cliente]:
        return list(self._clientes)

    def buscar(self, termo: str) -> list[Cliente]:
        termo = termo.lower().strip()
        if not termo:
            return self.listar()

        resultado: list[Cliente] = []
        for cliente in self._clientes:
            if termo in cliente.nome.lower() or termo in cliente.email.lower() or termo == str(cliente.id):
                resultado.append(cliente)
        return resultado


class CadastroProdutos:
    def __init__(self, arquivo: str = "produtos.json") -> None:
        _ensure_data_dir()
        self.arquivo = DATA_DIR / arquivo
        self._produtos = self._carregar()

    def _carregar(self) -> list[Produto]:
        if not self.arquivo.exists():
            self.arquivo.write_text("[]", encoding="utf-8")
            return []

        try:
            with self.arquivo.open("r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            self.arquivo.write_text("[]", encoding="utf-8")
            return []

        if not isinstance(dados, list):
            return []

        produtos: list[Produto] = []
        for item in dados:
            try:
                produtos.append(Produto(**item))
            except TypeError:
                continue
        return produtos

    def salvar(self) -> None:
        with self.arquivo.open("w", encoding="utf-8") as arquivo:
            json.dump([asdict(produto) for produto in self._produtos], arquivo, ensure_ascii=False, indent=2)

    def cadastrar(self, nome: str, preco: float, id_produto: int) -> Produto:
        nome_limpo = nome.strip()
        if not nome_limpo:
            raise ValueError("Nome do produto é obrigatório.")

        if any(produto.id == id_produto for produto in self._produtos):
            raise ValueError(f"Já existe um produto com o ID {id_produto}.")

        produto = Produto(id=id_produto, nome=nome_limpo, preco=float(preco))
        self._produtos.append(produto)
        self.salvar()
        return produto

    def listar(self) -> list[Produto]:
        return list(self._produtos)

    def buscar(self, termo: str) -> list[Produto]:
        termo = termo.lower().strip()
        if not termo:
            return self.listar()

        resultado: list[Produto] = []
        for produto in self._produtos:
            if termo in produto.nome.lower() or termo == str(produto.id):
                resultado.append(produto)
        return resultado


# Função utilitária para manter a estrutura do projeto mais simples.
def mostrar_dados(dados: list[Any]) -> None:
    if not dados:
        print("Nenhum registro encontrado.")
        return

    for item in dados:
        print(item)
