import os
import logging
import time

def func():
    current_time = time.strftime("%Y-%m-%d")
    path = os.getcwd() + f"/var/log/python-{current_time}/"
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)
    logging.basicConfig(level=logging.DEBUG,
                        filename="func.log",
			datefmt='%Y-%m-%d %H:%M:%S',
                        format="%(asctime)s %(name)s %(levelname)s %(message)s"
                        )
    logging.debug("func")

if __name__=="__main__":
	func()
