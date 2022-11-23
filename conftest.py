from datetime import datetime
import pytest
import testit
from playwright.sync_api import Playwright
from pathlib import Path

BASE_DIR = f'{Path(__file__).resolve(strict=True).parent}/'


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },

    }


@pytest.fixture()
def browser(playwright: Playwright):
    with testit.step('Открытие браузера Google Chrome'):
        browser = playwright.chromium.launch(
            args=[
                '--disable-dev-shm-usage',
                '--disable-gpu',
            ],
            chromium_sandbox=False,
            headless=True,
        )
    yield browser
    with testit.step('Закрытие браузера Google Chrome'):
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call) -> None:
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            if call.excinfo is not None and "page" in item.funcargs:
                context = item.funcargs['context']
                page = context.pages[-1]  # Последнее открытое окно
            else:
                print('Fail to take screenshot')
                return
            file_name = f'{datetime.now().strftime("%d-%m_%H.%M.%S")}.png'
            page.screenshot(path=BASE_DIR + file_name)
            testit.addAttachments(BASE_DIR + file_name)
        except Exception as e:
            print(f'Fail to take screenshot: {e}')
