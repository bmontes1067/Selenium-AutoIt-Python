from selenium import webdriver


def run_driver():
    driver_path = 'c:\\chromedriver\\chromedriver.exe'
    driver_options = webdriver.ChromeOptions()
    driver_options.debugger_address = "localhost:9090"

    cef_driver = webdriver.Chrome(executable_path=driver_path, options=driver_options)
