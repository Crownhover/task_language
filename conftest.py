import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
#Добавление возможности выбора браузера не баг, а фича*

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    
    parser.addoption('--language',action='store', default="ru-RU")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("language")
    

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        print(f"\nstart {browser_name} browser for test..lang:{user_language}")

    elif browser_name == "firefox":
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
        print(f"\nstart {browser_name} browser for test..lang:{user_language}")
        
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox,default --language=ru")
    yield browser
    print("\nquit browser..")
    browser.quit()