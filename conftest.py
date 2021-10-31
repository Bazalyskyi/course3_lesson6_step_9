import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    browser = None
    if language_name == "ru":
        print("\nstart chrome browser for test english language..")
        browser = webdriver.Chrome()
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru,ru_Ru'})
        browser = webdriver.Chrome(options=options)
        link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        browser.get(link)
    elif language_name == "es":
        print("\nstart chrome browser for test russian language..")
        browser = webdriver.Chrome()
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es,es_Sp'})
        browser = webdriver.Chrome(options=options)
        link = f"http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
        browser.get(link)
    else:
        raise pytest.UsageError("--language should be en or ru")
    yield browser
    print("\nquit browser..")
    browser.quit()
    
    


