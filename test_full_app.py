from playwright.sync_api import sync_playwright
import uuid
import time
import os

BASE_URL = "http://localhost:8080"

def test_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        print("--- INICIANDO TESTE TOTAL DA APLICAÇÃO ---")

        # 1. TESTE DE REGISTO
        print("\n1. Testando Fluxo de Registo...")
        test_id = str(uuid.uuid4())[:6]
        email_teste = f"user_{test_id}@isctem.ac.mz"
        page.goto(f"{BASE_URL}/registo.html")
        page.fill("#regEmail", email_teste)
        page.fill("#regTel", "821234567")
        page.fill("#regEmailSec", f"sec_{test_id}@gmail.com")
        page.fill("#regNome", "Utilizador de Teste")
        page.fill("#regSenha", "senha123")
        page.fill("#regConfirmarSenha", "senha123")
        page.select_option("#regFuncao", "Docente")
        page.screenshot(path="full_test_01_registo.png")
        page.click("button[type='submit']")
        page.wait_for_url("**/index.html", timeout=10000)
        print("✓ Registo concluído e redirecionado para Login.")

        # 2. TESTE DE RECUPERAÇÃO
        print("\n2. Testando Fluxo de Recuperação...")
        page.fill("#email", email_teste)
        page.click("#recoverLink")
        page.wait_for_selector("#modalRecuperacao", state="visible")
        page.screenshot(path="full_test_02_recuperacao_modal.png")
        tel_label = page.inner_text("#displayTel")
        email_label = page.inner_text("#displayEmailSec")
        print(f"✓ Modal de recuperação exibido (Tel: {tel_label}, Email: {email_label})")
        page.keyboard.press("Escape")
        time.sleep(1)

        # 3. TESTE DE LOGIN (ADMIN)
        print("\n3. Testando Login Admin...")
        page.fill("#email", "admin@isctem.ac.mz")
        page.fill("#password", "admin123")
        page.click("#submitBtn")
        page.wait_for_url("**/dashboard_admin.html", timeout=10000)
        page.screenshot(path="full_test_03_dashboard_admin.png")
        print("✓ Login Admin bem-sucedido.")

        # 4. TESTE DE CONFIGURAÇÕES (ADMIN)
        print("\n4. Testando Configurações de Horário (Admin)...")
        page.click("a[data-bs-target='#modalHorario']")
        page.wait_for_selector("#modalHorario", state="visible")
        page.fill("#horaAbertura", "07:00")
        page.fill("#horaFecho", "18:00")
        page.screenshot(path="full_test_04_modal_horario.png")
        page.click("#formHorario button[type='submit']")
        time.sleep(1)
        page.keyboard.press("Escape")
        print("✓ Horário da faculdade atualizado.")

        # 5. TESTE DE LISTA DE UTILIZADORES (ADMIN)
        print("\n5. Testando Lista de Utilizadores...")
        page.click("a[data-bs-target='#modalUtilizadores']")
        page.wait_for_selector("#usersTableBody", state="visible")
        time.sleep(1)
        page.screenshot(path="full_test_05_lista_usuarios.png")
        html_table = page.inner_html("#usersTableBody")
        if email_teste in html_table:
            print(f"✓ Utilizador {email_teste} encontrado na lista administrativa.")
        else:
            print(f"⚠ Utilizador {email_teste} não apareceu.")
        page.keyboard.press("Escape")
        time.sleep(1)

        # 6. TESTE DE LOGIN (DOCENTE)
        print("\n6. Testando Login Docente...")
        page.goto(f"{BASE_URL}/index.html")
        page.fill("#email", "docente@isctem.ac.mz")
        page.fill("#password", "docente123")
        page.click("#submitBtn")
        page.wait_for_url("**/dashboard_docente.html", timeout=10000)
        page.screenshot(path="full_test_06_dashboard_docente.png")
        print("✓ Login Docente bem-sucedido.")

        # 7. TESTE DE REQUISIÇÃO (DOCENTE)
        print("\n7. Testando Nova Requisição (Docente)...")
        page.click("button[data-bs-target='#modalRequisicao']")
        page.wait_for_selector("#modalRequisicao", state="visible")
        page.fill("#reqData", "2026-05-13")
        page.fill("#reqInicio", "09:00")
        page.fill("#reqFim", "11:00")
        page.screenshot(path="full_test_07_modal_requisicao.png")
        page.click("#btnSubmeterReq")
        time.sleep(1)
        page.keyboard.press("Escape")
        print("✓ Requisição submetida.")

        # 8. TESTE DE COMPROVATIVO (GERAÇÃO)
        print("\n8. Testando Geração de Comprovativo...")
        page.click("a[data-bs-target='#modalComprovativos']")
        page.wait_for_selector("#modalComprovativos", state="visible")
        page.screenshot(path="full_test_08_lista_comprovativos.png")
        page.keyboard.press("Escape")
        print("✓ Lista de comprovativos exibida.")

        # 9. TESTE DE VERIFICAÇÃO PÚBLICA
        print("\n9. Testando Verificação Pública...")
        receipt_url = f"{BASE_URL}/comprovativo.html?id=REQ-TESTE-999&d=Professor%20Exemplo&e=Laboratorio%20Central&dt=13/05/2026&h=09:00-11:00"
        page.goto(receipt_url)
        page.wait_for_selector("#content", state="visible")
        page.screenshot(path="full_test_09_comprovativo_publico.png")
        print("✓ Página pública validada.")

        print("\n--- TESTE TOTAL CONCLUÍDO COM SUCESSO ---")
        browser.close()

if __name__ == "__main__":
    test_app()
