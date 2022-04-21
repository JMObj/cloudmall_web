class login_datas:

    #登录失败测试数据
    cases = [
        {"user_mobile": "", "user_pwd": "", "user_code": "", "ass": "Phone number cannot be empty"},
        {"user_mobile": "123456789", "user_pwd": "", "user_code": "", "ass": "The password cannot be empty"},
        {"user_mobile": "123456789", "user_pwd": "123456", "user_code": "",
         "ass": "The verification code cannot be empty."},
        {"user_mobile": "123456789", "user_pwd": "1234545152", "user_code": "",
         "ass": "The verification code cannot be empty."}
    ]