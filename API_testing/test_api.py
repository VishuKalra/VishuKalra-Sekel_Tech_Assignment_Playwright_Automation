import pytest
from playwright.sync_api import sync_playwright
def test_get_api (playwright:sync_playwright):
    context = playwright.request.new_context()
    response = context.get("https://opensource-demo.orangehrmlive.com/web")
    assert response.status == 200
   