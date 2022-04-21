import os
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
#截图保存的路径
screenshot_dir = os.path.join(base_dir,"Outputs/pageshots")
#日志保存的路径
log_dir = os.path.join(base_dir,r"Outputs/logs/text.log")
#下单后订单号存放文件
order_number = os.path.join(base_dir,r"Outputs/orders/order.txt")

print(order_number)