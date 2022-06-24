import re
import requests
from lxml import etree


#
# url = '	https://www.xiurenb.com/uploadfile/202206/12/E4153911239.jpg'
url = 'https://www.xiurenb.com/XiuRen'
a = url.rsplit('/', 1)[0]
print(a)
# res = requests.get(url)
# res.encoding = 'utf-8'
# xpath_ = etree.HTML(res.text)
# page_list = xpath_.xpath('/html/body/div[3]/div/div/div[1]/div/text()')[0].strip()
# print(page_list)
# paaa = xpath_.xpath('/html/body/div[3]/div/div/div[4]/div/div/a/@href')
# print(paaa)
# sass = []
# for i in paaa:
#     if i not in sass:
#         sass.append(i)
# print(sass)
# for a_page in page_list:
#     data = {
#         'url': a_page.xpath('a/@href')[0],   # 单个图集url链接
#         'title': a_page.xpath('a/@title')[0],   # 图集 名称
#         'page_pic': a_page.xpath('a/img/@src')[0],  # 图集 名称
#         'girl': a_page.xpath('a/div/span/text()')[0]
#     }
#     print(data)
#
#
# # jianjie = xpath_.xpath('/html/body/div[3]/div/div/div[1]/div/text()')
# # print(jianjie[0].strip())
# # pages = xpath_.xpath('/html/body/div[3]/div/div/div[4]/div/div/a')
# # for i in pages:
# #     b = ''.join(i.xpath("text()"))
# #     if "上页" not in b and "下页" not in b and '/页' not in b:
# #         # print(i.xpath("@href"))
# #         print(i.xpath("@href")[0])
#         # a.append("https://www.xiurenji.net" + i.xpath("@href")[0])

# url = 'https://www.xiurenb.com/XiuRen/10836.html'
# url = 'https://www.xiurenb.com/uploadfile/202206/18/86163258994.jpg'
# res = requests.get(url)
# sateam = open('./测试.jpg', 'wb')
# sateam.write(res.content)
# sateam.close()
# xpath_ = etree.HTML(res.text)
# img = xpath_.xpath('/html/body/div[3]/div/div/div[5]/p/img/@src')
# print(len(img))
# print(img)

