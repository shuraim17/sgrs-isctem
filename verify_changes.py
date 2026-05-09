from playwright.sync_api import sync_playwright, expect
import os

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Verificar Página de Registo com Email Secundário
        print("A verificar registo.html...")
        page.goto("http://localhost:8080/registo.html")

        # Tirar screenshot do novo campo
        page.locator("#regEmailSec").scroll_into_view_if_needed()
        page.screenshot(path="verification_registo.png")
        print("Screenshot do registo guardado.")

        # 2. Verificar Página de Login e Modal de Recuperação
        print("A verificar index.html...")
        page.goto("http://localhost:8080/index.html")

        # Tentar abrir recuperação sem email
        page.click("#recoverLink")
        # Deve aparecer um toast de aviso (esperamos um pouco)
        page.wait_for_timeout(1000)
        page.screenshot(path="verification_login_initial.png")

        # Introduzir email e tentar recuperar
        page.fill("#email", "admin@isctem.ac.mz")
        page.click("#recoverLink")

        # Esperar pelo modal de escolha
        try:
            page.wait_for_selector("#modalRecuperacao", state="visible", timeout=5000)
            print("Modal de recuperação visível!")
            page.screenshot(path="verification_recovery_modal.png")
        except:
            print("Erro: Modal de recuperação não apareceu.")

        browser.close()

if __name__ == "__main__":
    # Garantir que o servidor está a correr (já deve estar do passo anterior)
    run_verification()
