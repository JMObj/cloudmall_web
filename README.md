### 该项目是web日常测试

####依赖的环境和第三方库
    1.下载对应的chromedriver驱动(网上有可以去搜索)，驱动版本号
    需要和谷歌浏览器版本一致，下载后解压到python安装目录下
    2.安装依赖的第三方库 pip install -r Library.text

####项目结构

```
web-daily：
 |- README.md                   #描述文件
 |- run.py                      # 主程序
 |- common                      # 封装的方法
 |   |- basepage                #对selenium中的元素操作方法进行二次封装
 |   |- dir_config              #日志、截图、订单号文件路径
 |   |- handle_log              #封装的日志方法
 |- Qutputs                     # 日志、下单后订单号、截图、报告文件
 |   |- logs                    #日志文件
 |   |- orders                  #订单号文件
 |   |- pageshots               #截图文件
 |   |- reports                 #报告文件
 |- PageLocators                # 元素定位（根据页面存放）
 |- PageObject                  # 页面操作对象（根据页面存放）
 |- TestCases                   # 测试用例
 |- TestDatas                   # 测试数据（没有用到可以忽略）
 |- Library.text                # 依赖的第三方库
 |- pytest.ini                  # pytest配置文件（目前只用于用例筛选）
 |- run.py                      # 主运行程序，用例依赖的数据也放在run文件中了，根据注释运行指定站点
```
