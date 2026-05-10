from playwright.sync_api import sync_playwright
import time

BASE_URL = "http://localhost:8080"

def test_modal_clickability():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("A testar clicabilidade dos botões no modal de recuperação...")
        page.goto(f"{BASE_URL}/index.html")

        # Introduzir email para habilitar o link (usando o admin que já existe)
        page.fill("#email", "admin@isctem.ac.mz")
        page.click("#recoverLink")

        # Esperar o modal abrir
        page.wait_for_selector("#modalRecuperacao", state="visible")
        print("Modal aberto.")

        # Tentar clicar no botão de Email Secundário
        # Se o backdrop estivesse a bloquear, o Playwright falharia ou tentaria clicar no backdrop
        try:
            # Vamos usar force=False para garantir que o Playwright verifique se o elemento é realmente clicável
            page.click("#btnRecuperarEmailSec", timeout=5000)
            print("✓ Sucesso: Botão 'Email para ...' foi clicado sem obstruções.")
        except Exception as e:
            print(f"❌ Erro: O botão não pôde ser clicado. Razão: {e}")
            page.screenshot(path="debug_click_fail.png")

        browser.close()

if __name__ == "__main__":
    test_modal_clickability()
