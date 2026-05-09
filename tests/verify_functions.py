import asyncio
import os
import random
import string
from playwright.async_api import async_playwright

def get_random_email(role):
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{role}_{random_str}@isctem.ac.mz"

async def run_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        print("Starting functional tests with new accounts...")

        # 1. Test Registration and Admin Dashboard
        admin_email = get_random_email('admin')
        print(f"Registering new admin: {admin_email}")
        await page.goto('http://localhost:8080/registo.html')
        await page.fill('#regNome', 'Admin Teste')
        await page.fill('#regEmail', admin_email)
        await page.fill('#regSenha', 'admin123')
        await page.fill('#regConfirmarSenha', 'admin123')
        await page.select_option('#regFuncao', 'Admin')
        await page.fill('#adminKey', 'isctem2026admin')
        await page.click('button[type="submit"]')

        # Redirection to login first according to registo.html logic
        await page.wait_for_url('**/index.html', timeout=10000)
        print("✅ Admin registration successful. Logging in...")

        await page.fill('#email', admin_email)
        await page.fill('#password', 'admin123')
        await page.click('#submitBtn')
        await page.wait_for_url('**/dashboard_admin.html', timeout=10000)
        print("✅ Admin login and redirection successful.")
        await page.screenshot(path='test-results/01_new_admin_dashboard.png')

        # 2. Test Gestor Registration
        gestor_email = get_random_email('gestor')
        print(f"Registering new gestor: {gestor_email}")
        await page.goto('http://localhost:8080/registo.html')
        await page.fill('#regNome', 'Gestor Teste')
        await page.fill('#regEmail', gestor_email)
        await page.fill('#regSenha', 'gestor123')
        await page.fill('#regConfirmarSenha', 'gestor123')
        await page.select_option('#regFuncao', 'Gestor')
        await page.click('button[type="submit"]')
        await page.wait_for_url('**/index.html', timeout=10000)

        await page.fill('#email', gestor_email)
        await page.fill('#password', 'gestor123')
        await page.click('#submitBtn')
        await page.wait_for_url('**/dashboard_gestor.html', timeout=10000)
        print("✅ Gestor registration and redirection successful.")
        await page.screenshot(path='test-results/02_new_gestor_dashboard.png')

        # 3. Test Docente Registration
        docente_email = get_random_email('docente')
        print(f"Registering new docente: {docente_email}")
        await page.goto('http://localhost:8080/registo.html')
        await page.fill('#regNome', 'Docente Teste')
        await page.fill('#regEmail', docente_email)
        await page.fill('#regSenha', 'docente123')
        await page.fill('#regConfirmarSenha', 'docente123')
        await page.select_option('#regFuncao', 'Docente')
        await page.click('button[type="submit"]')
        await page.wait_for_url('**/index.html', timeout=10000)

        await page.fill('#email', docente_email)
        await page.fill('#password', 'docente123')
        await page.click('#submitBtn')
        await page.wait_for_url('**/dashboard_docente.html', timeout=10000)
        print("✅ Docente registration and redirection successful.")
        await page.screenshot(path='test-results/03_new_docente_dashboard.png')

        await browser.close()

if __name__ == "__main__":
    os.makedirs('test-results', exist_ok=True)
    asyncio.run(run_tests())
