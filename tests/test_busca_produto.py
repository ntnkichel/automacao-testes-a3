from pathlib import Path

from playwright.sync_api import Page, expect

URL_BASE = "https://www.amazon.com.br/"
TERMO_PRODUTO = "Kindle Paperwhite"
TERMO_SEM_RESULTADO = "Test123Guilherme"

EVIDENCIAS = Path(__file__).resolve().parents[1] / "evidencias"
EVIDENCIAS.mkdir(parents=True, exist_ok=True)


def pesquisar_produto(page: Page, termo: str) -> None:
    """Abre a Amazon e pesquisa o termo informado."""
    page.goto(URL_BASE, wait_until="domcontentloaded")

    campo_busca = page.locator("#twotabsearchtextbox")
    expect(campo_busca).to_be_visible(timeout=15_000)

    campo_busca.fill(termo)
    campo_busca.press("Enter")


def test_ct001_buscar_produto_por_nome(page: Page) -> None:
    """CT-001: pesquisa Kindle Paperwhite e valida os resultados."""
    pesquisar_produto(page, TERMO_PRODUTO)

    resultados = page.locator(
        '[data-component-type="s-search-result"]'
    )
    expect(resultados.first).to_be_visible(timeout=20_000)

    textos = resultados.all_text_contents()

    encontrou_produto = any(
        "kindle" in texto.lower()
        and "paperwhite" in texto.lower()
        for texto in textos[:10]
    )

    assert encontrou_produto, (
        "Nenhum dos 10 primeiros resultados apresentou "
        "os termos Kindle e Paperwhite."
    )

    page.screenshot(
        path=str(EVIDENCIAS / "CT-001_busca_produto.png"),
        full_page=True,
    )


def test_ct002_buscar_produto_inexistente(page: Page) -> None:
    """CT-002: pesquisa um termo sem resultados e valida a mensagem."""
    pesquisar_produto(page, TERMO_SEM_RESULTADO)

    mensagem_sem_resultados = page.get_by_text(
        "Nenhum resultado para sua consulta de pesquisa.",
        exact=False,
    )

    expect(mensagem_sem_resultados).to_be_visible(timeout=20_000)

    page.screenshot(
        path=str(EVIDENCIAS / "CT-002_busca_sem_resultados.png"),
        full_page=True,
    )