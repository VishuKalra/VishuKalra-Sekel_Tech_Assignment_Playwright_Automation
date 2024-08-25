
import pytest
import time
from playwright.sync_api import sync_playwright

def browser (page):
    with sync_playwright () as p:
        browser = p.chromium.launch(slow_mo=300)
        context = browser.new_context()
        page = context.new_page()
        yield browser
        context.close()
        browser.close()
def test_site_title(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expected_title = "OrangeHRM" 
    actual_title = page.title()
    assert actual_title == expected_title,f"title mismatch "

def test_valid_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill("input[name='username']","Admin")
    page.fill("input[placeholder='Password']","admin123")
    page.click("button[type='submit']")
    time.sleep(2)
    assert page.url=="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",f"Invalid Credentials: Not redirected to dashboard page"

def test_invalid_username (page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill("input[name='username']","Admin_Vk")
    page.fill("input[placeholder='Password']","admin123")
    page.click("button[type='submit']")
    assert page.url=="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",f"Username Validation missing"
    error_message = page.locator("div.oxd-alert.oxd-alert--error").text_content()
    assert "Invalid credentials" in error_message,"Error message does not match"

def test_invaild_password(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill("input[placeholder='Username']","Admin")
    page.fill("input[name='password']","Admin123")
    page.click("button[type='submit']")
    assert page.url=="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",f"Password validation are missing(sensitive)"
    error_message = page.locator("div.oxd-alert.oxd-alert--error").text_content()
    assert "Invalid credentials" in error_message,"Error message does not match"
    




