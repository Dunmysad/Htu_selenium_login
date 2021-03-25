from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

#   宿舍外校园网账号密码
my_username_outdoor = ''
my_password_outdoor = ''

#   宿舍内校园网账号密码
my_username_indoor = ''
my_password_indoor = ''

#   代码运行提示
print('代码已经运行，请稍后!')

#   打开浏览器
driver = webdriver.Chrome()

#   打开校园网网址
driver.get("http://119.29.29.29")

#   获取当前页面标题
title_page = driver.title

#   等待浏览器相响应
while (title_page != '河南师范大学校园网登录' and title_page != '登录'):
    driver.refresh()
    title_page = driver.title

#   自动选择校园网区域
if title_page == '河南师范大学校园网登录':
    choose = 1
else:
    choose = 2

def login_in():

    #   教室校园网
    if choose == 2:
        #   找到账号密码对应的 html 元素
        input_username = driver.find_element(By.XPATH,'//*[@id="useridtemp"]')
        input_password = driver.find_element(By.XPATH,'//*[@id="passwd"]')
        
        #   输入账号、密码
        input_username.send_keys(my_username_outdoor)
        input_password.send_keys(my_password_outdoor)

        #   点击登录按钮
        login_btn = driver.find_element_by_id('checkButton')
        ActionChains(driver).click(login_btn).perform()

        #   错误处理
        error_text = driver.find_element(By.XPATH,'//*[@id="_alert_msg"]').text  
        
        if error_text:
            print(error_text)
        else:
            print('登录成功!')

    if choose == 1:

        #   找到账号、密码以及运营商对应的html元素
        input_username = driver.find_element(By.XPATH,'//input[@id="userName"]')
        input_password = driver.find_element(By.XPATH,'//input[@id="passwd"]')
        yys = driver.find_element(By.XPATH,'//*[@id="yd"]')

        #   点击登录
        ActionChains(driver).click(yys).perform()

        #   输入账号、密码
        input_username.send_keys(my_username_indoor)
        input_password.send_keys(my_password_indoor)

        #   点击登录
        login_btn = driver.find_element_by_id('loginButton')
        ActionChains(driver).click(login_btn).perform()

        #   处理弹窗事件
        result = EC.alert_is_present()(driver) # 如果存在 返回alter对象，否则返回false, 源码
        if result:
            #   返回错误信息
            # print(result.text)
            error = result.text

            #  创建弹窗对象
            alert=driver.switch_to.alert 

            #点击弹窗中的【确定】
            alert.accept() 

            #   异常处理
            if login_btn:
                print(error)
                if error == '此帐号已在其它设备登录，点击‘确定’按钮重新登录':
                    login_in()
            else:
                print('登录成功!')

        else:
            print('登录成功!!')

if __name__ == '__main__':
    login_in()

    time.sleep(2)

    #   关闭浏览器
    driver.close()
