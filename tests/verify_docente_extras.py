
import asyncio
from playwright.async_api import async_playwright
import os

async def verify_docente_extras():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Setup output directory
        output_dir = "verification/docente_extras"
        os.makedirs(output_dir, exist_ok=True)

        print("Starting Docente Extras Verification...")

        # 1. Login as Docente
        await page.goto("http://127.0.0.1:8080/index.html")
        await page.fill("#email", "docente@isctem.ac.mz")
        await page.fill("#password", "docente123")
        await page.click("button[type='submit']")

        await page.wait_for_url("**/dashboard_docente.html")
        print("Logged in as Docente.")

        # 2. Check Histórico (Table should be visible on dashboard)
        await page.wait_for_selector("table")
        await page.screenshot(path=f"{output_dir}/01_historico_table.png")
        print("Captured Histórico Table.")

        # 3. Check Disponibilidade
        await page.click("text=Disponibilidade")
        await page.wait_for_selector("#modalDisponibilidade", state="visible")
        # Wait for grid to be built
        await page.wait_for_selector(".availability-grid .cell")
        await page.screenshot(path=f"{output_dir}/02_disponibilidade_modal.png")
        print("Captured Disponibilidade Modal.")

        # Close modal
        await page.click("#modalDisponibilidade .btn-close")
        await page.wait_for_selector("#modalDisponibilidade", state="hidden")

        # 4. Check Comprovativos
        await page.click("text=Comprovativos")
        await page.wait_for_selector("#modalComprovativos", state="visible")
        await page.screenshot(path=f"{output_dir}/03_comprovativos_modal.png")
        print("Captured Comprovativos Modal.")

        # 5. Check PDF Generation (opens new window)
        async with page.expect_popup() as popup_info:
            await page.click("text=PDF")
        popup = await popup_info.value
        await popup.wait_for_load_state()
        await popup.screenshot(path=f"{output_dir}/04_comprovativo_pdf.png")
        print("Captured Generated PDF/Comprovativo.")

        await browser.close()
        print("Verification complete.")

if __name__ == "__main__":
    import subprocess
    import time

    # Start server
    server = subprocess.Popen(["python3", "-m", "http.server", "8080"])
    time.sleep(2)

    try:
        asyncio.run(verify_docente_extras())
    finally:
        server.terminate()
