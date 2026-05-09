import { test, expect } from '@playwright/test';

test.use({ viewport: { width: 375, height: 667 }, isMobile: true });

test('Mobile menu toggle works on Admin Dashboard', async ({ page }) => {
    // Mock session storage
    await page.addInitScript(() => {
        window.sessionStorage.setItem('loggedEmail', 'admin@isctem.ac.mz');
        window.sessionStorage.setItem('loggedFuncao', 'Admin');
    });

    await page.goto('http://localhost:8080/dashboard_admin.html');

    // Check if sidebar is hidden
    const sidebar = page.locator('#sidebar');
    await expect(sidebar).not.toBeVisible(); // Due to transform: translateX(-100%)

    // Click toggle
    const toggle = page.locator('#sidebarToggle');
    await toggle.click();

    // Check if sidebar is visible
    await expect(sidebar).toHaveClass(/active/);
    
    await page.screenshot({ path: 'verification/mobile_menu_open.png' });
});
