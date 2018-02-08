import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(name, passwd):
    url = 'https://passport.baidu.com/v2/?login'
    # 这里可以用Chrome、Phantomjs等，如果没有加入环境变量，需要指定具体的位置
    driver = webdriver.Chrome()
    driver.get(url)
    print('开始登录')
    chg_field =WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "TANGRAM__PSP_3__footerULoginBtn")))
    chg_field.click()
    name_field = driver.find_element_by_id('TANGRAM__PSP_3__userName')
    name_field.send_keys(name)
    passwd_field = driver.find_element_by_id('TANGRAM__PSP_3__password')
    passwd_field.send_keys(passwd)
    login_button = driver.find_element_by_id('TANGRAM__PSP_3__submit')
    login_button.click()
    return set_sessions(driver)


def set_sessions(browser):
    time.sleep(10)
    request = requests.Session()
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    request.headers.update(headers)
    cookies = browser.get_cookies()
    for cookie in cookies:
        #print cookie['name']+":"+cookie['value']
        request.cookies.set(cookie['name'], cookie['value'])
    return request





# 验证登录是否成功  看看个人中心页面就知道啦
# def isSuccess():
#     request = login(config.username,config,password)
#     html_index = request.get('http://i.baidu.com/')
#     with open("tieba.html", 'wb') as f:
#         f.write(html_index.content)
#         f.close()
