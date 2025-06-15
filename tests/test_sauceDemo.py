
from playwright.sync_api import sync_playwright


def test_saucedemo():
    with sync_playwright() as sp:
        browser = sp.chromium.launch(headless=False,slow_mo=500)
        context = browser.new_context(viewport={"width":1200, "height":800})
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        assert "Swag Labs" in page.title()

        # Locate username and password
        user_name = page.locator("input[name='user-name']")
        pass_word = page.locator("input[name='password']")

        # Send keys to the username & paswd
        user_name.fill("standard_user")
        print("Username entered!!")
        pass_word.fill("secret_sauce")
        print("Password entered")


        # Locate Login btn and click it
        login_btn = page.locator("input[type='submit']")
        login_btn.click()
        print("Successfully logged!!!")

        assert "Products" in page.locator("body").inner_text()

        browser.close()