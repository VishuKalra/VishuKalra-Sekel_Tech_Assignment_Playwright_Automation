import pytest #for testing framework
import time #to set dealy
from playwright.sync_api import sync_playwright #for browser automation
def browser (page): #Setup browser
    with sync_playwright () as p:
        browser = p.chromium.launch(slow_mo=5000)
        context = browser.new_context()
        page = context.new_page()
        yield browser
        context.close()
        browser()
def test_vaild_inputs (page):
    #login script
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)
    page.fill("input[name='username']","Admin") 
    time.sleep(2)
    page.fill("input[placeholder='Password']","admin123")
    time.sleep(2)
    page.click("button[type='submit']")
    time.sleep(2)
    #search script start from here

    page.click("//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")
    time.sleep(2)
    page.fill("//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input","Vishwanath777")
    time.sleep(2)
    page.click("form i")
    time.sleep(2)
    page.get_by_role("option[name='Admin']").click()
    time.sleep(2)
    page.fill("input[placeholder='Type for hints...']","Orange Test")
    time.sleep(2)
    page.get_by_role("option[name='Orange Test']").dblclick(),f"user is edited/delted by someone:please create new user with same deatils to check this script"
    page.click("//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]")
    time.sleep(2)
    page.get_by_role("option[name='Enabled']").dblclick()
    time.sleep(2)
    page.get_by_role("button[name=' Search ']").dblclick()
    time.sleep(5)
    result = page.locator("//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span").text_content()
    assert "(1) Record Found" in result,"User is deleted by someone"
    time.sleep(5)
    page.click("//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div/button[2]")
    time.sleep(5)
    assert page.url=="https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser/58"
    time.sleep(2)
    
