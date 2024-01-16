'''
自动登录163邮箱，并发送邮件
'''
from selenium import webdriver
from time import sleep
import time
 
def login(email,password):
    
    iframe = driver.find_element_by_xpath("//iframe[contains(@id, 'x-URS-iframe')]")    #使用Xpath提供的contains定位
    driver.switch_to.frame(iframe)    #切换到iframe
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('password').send_keys(password)
    # sleep(2)
    driver.find_element_by_id('dologin').click()
    sleep(1)
 
def sendeamil():
    login(email,password)
    sleep(2)
    driver.find_element_by_id('_mail_component_132_132').click()
    sleep(1)
    driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys(addressee)
    sleep(1)
    driver.find_element_by_xpath("//div[@class = 'bz0']/div/input[@class = 'nui-ipt-input']").send_keys(main)
    sleep(1)
 
    #切换到iframe界面
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@class,'APP-editor-iframe')]"))
    driver.find_element_by_xpath("/html/body").send_keys(content)
    sleep(1)
    driver.switch_to.default_content()    #退出iframe界面
    sleep(1)
    driver.find_element_by_id('_mail_button_2_239').click()
 
 
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()    #窗口最大化
    # time.sleep(1)
    url = 'https://mail.163.com'
    driver.get(url)#不需要再加上引号了
 
    email = 'htn45565@163.com'            #输入邮箱用户名
    password = 'dytbb138186'            #输入邮箱密码
 
    addressee = '收件人'        #输入收件人
  
    main = time.strftime('%Y-%m-%d',time.localtime(time.time()))    #输入邮件主题
    
    content = '今天是: ' + main    #输入邮件内容
 
    sendeamil()