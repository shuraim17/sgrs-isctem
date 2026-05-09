import asyncio
from playwright.async_api import async_playwright
import os
import subprocess
import time

async def run_tests():
    # Start the server
    server_process = subprocess.Popen(['python3', '-m', 'http.server', '8080'])
    time.sleep(2)  # Give the server time to start

    try:
        async with async_playwright() as p:
            # Setup directories
            os.makedirs('verification/functions', exist_ok=True)

            browser = await p.chromium.launch()

            # 1. Test Login - Admin
            page = await browser.new_page()
            await page.goto('http://localhost:8080/index.html')
            await page.fill('input[type="email"]', 'admin@isctem.ac.mz')
            await page.fill('input[type="password"]', 'admin123')
            await page.screenshot(path='verification/functions/01_login_admin_filled.png')
            await page.click('button[type="submit"]')
            await page.wait_for_url('**/dashboard_admin.html')
            await page.wait_for_timeout(1000) # Wait for animation
            await page.screenshot(path='verification/functions/02_dashboard_admin.png')

            # Test Admin User Management Modal
            await page.click('a:has-text("Utilizadores")')
            await page.wait_for_timeout(500)
            await page.screenshot(path='verification/functions/03_admin_users_list_modal.png')

            # Test "Novo" button inside the modal
            await page.click('button:has-text("+ Novo")')
            await page.wait_for_timeout(500)
            await page.screenshot(path='verification/functions/03b_admin_create_modal.png')

            # Close modals (escape twice since there are two stacked)
            await page.keyboard.press('Escape')
            await page.wait_for_timeout(300)
            await page.keyboard.press('Escape')

            await page.click('a:has-text("Sair")')
            await page.wait_for_url('**/index.html')

            # 2. Test Login - Gestor
            await page.fill('input[type="email"]', 'gestor@isctem.ac.mz')
            await page.fill('input[type="password"]', 'gestor123')
            await page.click('button[type="submit"]')
            await page.wait_for_url('**/dashboard_gestor.html')
            await page.wait_for_timeout(1000)
            await page.screenshot(path='verification/functions/04_dashboard_gestor.png')

            # Test Gestor Modal
            await page.click('a:has-text("Relatórios")')
            await page.wait_for_timeout(500)
            await page.screenshot(path='verification/functions/05_gestor_reports_modal.png')
            await page.keyboard.press('Escape')
            await page.click('a:has-text("Sair")')

            # 3. Test Login - Docente
            await page.wait_for_url('**/index.html')
            await page.fill('input[type="email"]', 'docente@isctem.ac.mz')
            await page.fill('input[type="password"]', 'docente123')
            await page.click('button[type="submit"]')
            await page.wait_for_url('**/dashboard_docente.html')
            await page.wait_for_timeout(1000)
            await page.screenshot(path='verification/functions/06_dashboard_docente.png')

            # Test Docente Modal
            await page.click('button:has-text("Nova Requisição")')
            await page.wait_for_timeout(500)
            await page.screenshot(path='verification/functions/07_docente_request_modal.png')
            await page.keyboard.press('Escape')

            # Test PDF Generation (Receipts modal)
            await page.click('a:has-text("Comprovativos")')
            await page.wait_for_timeout(500)
            await page.screenshot(path='verification/functions/08_docente_receipts_modal.png')
            await page.keyboard.press('Escape')

            await page.click('a:has-text("Sair")')

            # 4. Test Registration Page
            await page.goto('http://localhost:8080/registo.html')
            await page.wait_for_timeout(500)
            await page.screenshot(path='verification/functions/09_registration_page.png')

            # 5. Mobile Verification
            mobile_context = await browser.new_context(viewport={'width': 390, 'height': 844})
            mobile_page = await mobile_context.new_page()
            await mobile_page.goto('http://localhost:8080/index.html')
            await mobile_page.fill('input[type="email"]', 'admin@isctem.ac.mz')
            await mobile_page.fill('input[type="password"]', 'admin123')
            await mobile_page.click('button[type="submit"]')
            await mobile_page.wait_for_url('**/dashboard_admin.html')
            await mobile_page.wait_for_timeout(1000)
            await mobile_page.screenshot(path='verification/functions/10_mobile_dashboard.png')

            # Open Menu
            await mobile_page.click('#sidebarToggle')
            await mobile_page.wait_for_timeout(500)
            await mobile_page.screenshot(path='verification/functions/11_mobile_menu_open.png')

            await browser.close()
    finally:
        server_process.terminate()

if __name__ == '__main__':
    asyncio.run(run_tests())
