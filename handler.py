import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def hello(event, context):
    super_proxy_url = os.environ.get('PROXY_URL')
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    # Create a copy of desired capabilities object.
    desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    # Change the proxy properties of that copy.
    desired_capabilities['proxy'] = {
        "httpProxy": super_proxy_url,
        "ftpProxy": super_proxy_url,
        "sslProxy": super_proxy_url,
        "noProxy": None,
        "proxyType": "MANUAL",
        "class": "org.openqa.selenium.Proxy",
        "autodetect": False
    }

    driver = webdriver.Chrome('/opt/chromedriver', chrome_options=options, desired_capabilities=desired_capabilities)
    driver.get('https://mobile.bet365.com')
    cookies_list = driver.get_cookies()
    driver.close()
    driver.quit()

    response = {
        "statusCode": 200,
        "cookies": cookies_list
    }

    return response
