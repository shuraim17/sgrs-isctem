from playwright.sync_api import sync_playwright
import uuid

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        test_id = str(uuid.uuid4())[:8]
        email = f"test_{test_id}@isctem.ac.mz"
        email_sec = f"sec_{test_id}@gmail.com"

        print(f"1. A registar utilizador de teste: {email}")
        page.goto("http://localhost:8080/registo.html")
        page.fill("#regEmail", email)
        page.fill("#regTel", "841234567")
        page.fill("#regEmailSec", email_sec)
        page.fill("#regNome", "Utilizador Teste")
        page.fill("#regSenha", "teste123")
        page.fill("#regConfirmarSenha", "teste123")
        page.select_option("#regFuncao", "Docente")

        page.screenshot(path="v1_registo_preenchido.png")
        page.click("button[type='submit']")

        # Esperar redirecionamento para login
        try:
            page.wait_for_url("**/index.html", timeout=10000)
            print("Utilizador registado com sucesso.")
        except:
            print("Erro ou demora no registo. Verifique o screenshot v1_registo_erro.png")
            page.screenshot(path="v1_registo_erro.png")
            browser.close()
            return

        print("2. A testar recuperação de acesso...")
        page.fill("#email", email)
        page.click("#recoverLink")

        try:
            page.wait_for_selector("#modalRecuperacao", state="visible", timeout=5000)
            print("Modal de escolha de recuperação apareceu!")

            # Verificar se os dados mascarados estão lá
            tel_text = page.inner_text("#displayTel")
            email_sec_text = page.inner_text("#displayEmailSec")
            print(f"Dados mascarados: Tel={tel_text}, EmailSec={email_sec_text}")

            page.screenshot(path="v2_recovery_modal.png")

            # Testar clique no email secundário
            page.click("#btnRecuperarEmailSec")
            page.wait_for_timeout(1000)
            page.screenshot(path="v3_recovery_triggered.png")
            print("Fluxo de recuperação por email secundário testado.")

        except Exception as e:
            print(f"Erro no teste de recuperação: {e}")
            page.screenshot(path="v2_recovery_error.png")

        browser.close()

if __name__ == "__main__":
    run_verification()
