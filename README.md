# Automação de testes — Amazon Brasil

Projeto acadêmico da disciplina Garantia da Qualidade de Software. Os testes de interface são implementados em Python com Playwright e pytest.

## Casos de teste automatizados

- **CT-001 — Busca por produto:** pesquisa por `Kindle Paperwhite` e verifica se os resultados incluem produtos relacionados.
- **CT-005 — Detalhes do produto:** abre um resultado correspondente e verifica a exibição do título e de um preço.

## Pré-requisitos

- Python 3.11 ou superior instalado.
- Visual Studio Code com a extensão Python da Microsoft.
- Conexão com a internet.

## Preparar o ambiente (Windows)

No terminal do VS Code, na pasta do projeto:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
```

Esses comandos instalam as dependências no ambiente virtual sem precisar ativá-lo manualmente.

## Executar os testes

Com o ambiente preparado, execute:

```powershell
.\.venv\Scripts\python.exe -m pytest -v --headed
```

A opção `--headed` abre a janela do navegador durante a execução. Para executar sem mostrar a janela, remova essa opção.

## Evidências

Quando cada teste chega ao final com sucesso, uma captura de tela é gravada na pasta `evidencias/`:

- `CT-001_busca_produto.png`
- `CT-005_detalhes_produto.png`

## Observações

A Amazon pode alterar sua interface, exibir verificações de acesso ou não apresentar os mesmos resultados em todas as sessões. Nesses casos, a execução pode exigir revisão dos seletores ou adaptação do caso de teste. Não tente contornar verificações de segurança do site. Confirme também se a Amazon atende à regra da disciplina de não utilizar sites já usados nos exercícios práticos em sala.
