import os
import logging
import time

def func():
    current_time = time.strftime("%Y-%m-%d")#获取当前日期
    path = os.getcwd() + f"/var/log/python-{current_time}/"#生成目录
    if not os.path.exists(path):#不存在就创建目录
        os.makedirs(path)
    os.chdir(path)#切换至指定目录下
#logging配置
    logging.basicConfig(level=logging.DEBUG,
                        filename="func.log",
			datefmt='%Y-%m-%d %H:%M:%S',
                        format="%(asctime)s %(name)s %(levelname)s %(message)s"
                        )
    logging.debug("func")

if __name__=="__main__":
	func()
