import requests
from lxml import etree
from time import sleep



url = 'https://www.smzdm.com/'

user_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"

header = {"user-agent": user_Agent}


def get_url_name(url):
    response = requests.get(url, headers=header)

    #生成HTML格式
    selector = etree.HTML(response.text)

    # 商品名称列表
    item_title = selector.xpath('//*[@id="feed-main-list"]/li[1]/div/div[2]/h5/a/text()')

    # 商品链接列表
    item_content = selector.xpath('//*[@id="feed-main-list"]/li[1]/div/div[2]/h5/a/@href')

    # 遍历关系对应字典
    item_info = dict(zip(item_title, item_content))

    #写入文件
    with open('data.text', 'a', newline='',encoding='utf-8') as f:
        for i in item_info:
            temp = i.split('\n')[1].lstrip()
            f.write(f'商品名称:{temp}\t\t商品链接:{item_info[i]}')


if __name__ == "__main__":
    get_url_name(url)
