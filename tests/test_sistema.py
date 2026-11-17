import unittest
from pathlib import Path

from app.cadastros import CadastroClientes, CadastroProdutos
from app.relatorios import gerar_relatorio_clientes, gerar_relatorio_produtos


class TestSistemaCadastro(unittest.TestCase):
    def setUp(self):
        base_dir = Path(__file__).resolve().parent.parent / "data"
        base_dir.mkdir(parents=True, exist_ok=True)

        for arquivo in ["clientes_teste.json", "produtos_teste.json"]:
            caminho = base_dir / arquivo
            if caminho.exists():
                caminho.unlink()

        self.clientes = CadastroClientes(arquivo="clientes_teste.json")
        self.produtos = CadastroProdutos(arquivo="produtos_teste.json")

    def test_cadastrar_cliente(self):
        cliente = self.clientes.cadastrar("Ana", "ana@email.com", 1)
        self.assertEqual(cliente.nome, "Ana")
        self.assertEqual(len(self.clientes.listar()), 1)

    def test_cadastrar_produto(self):
        produto = self.produtos.cadastrar("Teclado", 120.0, 1)
        self.assertEqual(produto.nome, "Teclado")
        self.assertEqual(len(self.produtos.listar()), 1)

    def test_relatorio_clientes_vazio(self):
        relatorio = gerar_relatorio_clientes(self.clientes.listar())
        self.assertIn("Nenhum cliente cadastrado", relatorio)

    def test_relatorio_produtos_vazio(self):
        relatorio = gerar_relatorio_produtos(self.produtos.listar())
        self.assertIn("Nenhum produto cadastrado", relatorio)


if __name__ == "__main__":
    unittest.main()
