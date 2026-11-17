arquivo_principal = "main.py"

while_true = """O loop while True mantém o programa em execução até que o usuário escolha sair.
A cada iteração, o menu é exibido e a opção escolhida direciona para a funcionalidade correspondente.
Quando a opção 0 é selecionada, o programa encerra."""

bugs = {
    "bug_1": {
        "problema": "Entrada de opção não numérica no menu.",
        "causa": "Conversão direta com int(input()) sem tratamento de exceção.",
        "solucao": "Uso de try/except para tratar entradas inválidas e continuar o loop."
    },
    "bug_2": {
        "problema": "Cadastro com ID duplicado.",
        "causa": "Validação de duplicidade ausente antes de salvar.",
        "solucao": "Verificação com if any(...) antes de adicionar o registro."
    },
    "bug_3": {
        "problema": "Arquivos de persistência ausentes ou corrompidos.",
        "causa": "Leitura de JSON antes da criação da pasta/arquivo.",
        "solucao": "Criação automática da pasta data e reset do arquivo em caso de conteúdo inválido."
    }
}

github_link = "___________________"

checklist_publicacao = [
    "Repositório criado no GitHub",
    "Arquivo README.md preenchido",
    "Arquivo .gitignore configurado",
    "Código testado localmente",
    "Arquivos desnecessários removidos ou ignorados",
    "Branch principal definida",
    "Commit inicial realizado",
    "Push concluído"
]
