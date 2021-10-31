import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


supported_languages = {
    'العربيّة': 'ar',
    'català': 'ca',
    'česky': 'cs',
    'dansk': 'da',
    'Deutsch': 'de',
    'British English': 'en-gb',
    'Ελληνικά': 'el',
    'español': 'es',
    'suomi': 'fi',
    'français': 'fr',
    'italiano': 'it',
    '한국어': 'ko',
    'Nederlands': 'nl',
    'polski': 'pl',
    'Português': 'pt',
    'Português Brasileiro': 'pt-br',
    'Română': 'ro',
    'Русский': 'ru',
    'Slovensky': 'sk',
    'Українська': 'uk',
    '简体中文': 'zh-hans'
}

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help=f"""Choose language: {', '.join(supported_languages.keys())}""")





@pytest.fixture(scope="function")
def browser(request):

    language = request.config.getoption("language")
    if language in supported_languages.values():
        print("\nstart chrome browser for test english language..")
        browser = webdriver.Chrome()
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        browser.get(link)
    else:
        raise pytest.UsageError("--language must be from the list")
    yield browser
    print("\nquit browser..")
    browser.quit()
    
    


