from selenium.webdriver.common.by import By

class LoginLocators:
    '''
    登录页面元素定位
    '''
    #首页注册登录按钮
    login_or_register_button = (By.XPATH,'//*[@id="root"]/div/div/div/nav/div[3]/div[1]/div[1]/div[1]/div/p[1]')
    #选择邮箱注册按钮
    email_button = (By.XPATH,'//*[@id="authui-modal"]/div/div[1]/form/ul/li[4]/button')
    #注册邮箱输入框
    email_enter =(By.XPATH,'//*[@id="authui-modal"]/div/form/div[2]/div/div[1]/input')
    #输入邮箱后的注册按钮
    email_ragister_button = (By.XPATH,'//*[@id="authui-modal"]/div/form/div[3]/div/button[2]')
    #邮箱注册姓名输入框
    name_enter = (By.XPATH,'//*[@id="authui-modal"]/div/form/div[2]/div[3]/input')
    #邮箱注册密码输入框
    password_enter = (By.XPATH,'//*[@id="authui-modal"]/div/form/div[2]/div[5]/div[1]/input')
    #邮箱注册输入完所填的信息后的保存按钮
    save_button = (By.XPATH,'//*[@id="authui-modal"]/div/form/div[3]/div/button[2]')
