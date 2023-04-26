from selenium import webdriver

def get_configs():
    configs = {}

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    configs['chrome_options'] = chrome_options

    configs['url_main'] = "https://auto.danawa.com/usedcar/?Work=list&Tab=classify&Page="

    driver = webdriver.Chrome(options=chrome_options)

    dicts = {
        'car_name':[], 
        'car_number':[],
        'car_img':[],
    }
    return configs