import requests
from requests.adapters import HTTPAdapter
from lxml import etree
import re
import aiohttp
import asyncio
import motor.motor_asyncio   # python3 -m pip install motor
import itertools   # list合并工具
import pymongo
import hashlib
import time


class Image_Push():
    uri = 'mongodb+srv://g6370508:4826Ghp057@cluster0.qywbm.mongodb.net'
    client = pymongo.MongoClient(uri)
    kano = client.get_database("kano")
    XiuRen = kano.XiuRen

    def delete(self, document: dict):
        Image_Push.XiuRen.delete_one(document)

    def insert(self, document: dict):
        Image_Push.XiuRen.insert_one(document)

    def find(self, document=None) -> list:
        a = list(Image_Push.XiuRen.find(document))
        return a
    def update(self, document: tuple):   # 元祖    （条件，修改值）
        myquery = document[0]
        newvalues = {"$set": document[1]}
        Image_Push.XiuRen.update(myquery, newvalues)

    def get_time(self) -> str:
        return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(int(time.time())))

class Image_Pust_():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://g6370508:4826Ghp057@cluster0.qywbm.mongodb.net')  # 使用链接访问
    kano = client.kano
    XiuRen = kano.XiuRen

    async def do_find(self, document: dict):
        c = Image_Pust_().kano.XiuRen
        return [i async for i in c.find(document)]
    async def insert(self, document: dict):
        c = Image_Pust_().kano.XiuRen
        result = await c.insert_one(document)  # insert_one只能插入一条数据
        print('result %s' % repr(result.inserted_id))
    async def get_time(self) -> str:
        return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(int(time.time())))


class XiuRen(Image_Pust_):
    def __init__(self):
        s_domin = 'https://www.xiurenb.com'
        session = requests.Session()
        session.headers = {
            'User-Agent': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4495.0 Safari/537.36',
        }
        session.mount('http://', HTTPAdapter(max_retries=4))  # 设置重试最大次数
        session.mount('https://', HTTPAdapter(max_retries=4))
        url_list = [{'url': '/BoLoli', 'name': 'BoLoli兔几盟'}, {'url': '/XiaoYu', 'name': 'XiaoYu画语界'}, {'url': '/XiuRen', 'name': 'XiuRen秀人网'}, {'url': '/MFStar', 'name': 'MFStar模范学院'}, {'url': '/MiStar', 'name': 'MiStar魅妍社'}, {'url': '/MyGirl', 'name': 'MyGirl美媛馆'}, {'url': '/IMiss', 'name': 'Imiss爱蜜社'}, {'url': '/YouWu', 'name': 'YouWu尤物馆'}, {'url': '/Uxing', 'name': 'Uxing优星馆'}, {'url': '/MiiTao', 'name': 'MiiTao蜜桃社'}, {'url': '/FeiLin', 'name': 'FeiLin嗲囡囡'}, {'url': '/WingS', 'name': 'WingS影私荟'}, {'url': '/Taste', 'name': 'Taste顽味生活'}, {'url': '/LeYuan', 'name': 'LeYuan星乐园'}, {'url': '/HuaYan', 'name': 'HuaYan花の颜'}, {'url': '/DKGirl', 'name': 'DKGirl御女郎'}, {'url': '/MintYe', 'name': 'MintYe薄荷叶'}, {'url': '/YouMi', 'name': 'YouMi尤蜜荟'}, {'url': '/Candy', 'name': 'Candy糖果画报'}, {'url': '/MTMeng', 'name': 'MTMeng模特联盟'}, {'url': '/Micat', 'name': 'Micat猫萌榜'}, {'url': '/HuaYang', 'name': 'HuaYang花漾'}, {'url': '/XingYan', 'name': 'XingYan星颜社'}]
        all_page = []
        for url_data in url_list:
            a = self.get_listpage_s(session, url_data, s_domin)
            all_page.append(a)
        all_page = list(itertools.chain.from_iterable(all_page))
        asyncio.run(self.Go_aio(all_page))

    def get_listpage(self, session) -> list:
        url = 'https://www.xiurenb.com/XiuRen'
        res = self.response(session, url)
        res.encoding = 'utf-8'
        x_data = etree.HTML(res.text)
        list_page = x_data.xpath('/html/body/div[3]/div/div/div[2]/a')
        for i in list_page:
            a = i.xpath('text()')[0]
            if a == '尾页':
                all_page = int(re.search('\d+', i.xpath('@href')[0]).group())
                list_page = []
                for i in range(all_page):
                    if i < 1:
                        url = url.rsplit('/', 1)[0]
                    else:
                        url = f"https://www.xiurenb.com/XiuRen/index{i + 1}.html"
                    list_page.append(url)
                return list_page
    def get_listpage_s(self, session, url_data, s_domin) -> list:
        url = f"{s_domin}{url_data['url']}"
        res = session.get(url)
        res.encoding = 'utf-8'
        x_data = etree.HTML(res.text)
        list_page = x_data.xpath('/html/body/div[3]/div/div/div[2]/a/@href')
        sss_ = []
        for i in list_page:
            try:
                sss = re.search('\d+', i).group(0)
                sss_.append(int(sss))
            except AttributeError:
                continue
            except:
                continue
        sss_.sort()
        list_page = []
        try:
            for i in range(sss_[-1]):
                if i < 1:
                    url = url
                else:
                    url = f"{s_domin}{url_data['url']}/index{i + 1}.html"
                list_page.append(url)
        except:
            list_page.append(url)
        return list_page
    def response(self, session, url):
        try:
            response = session.get(url, timeout=(5, 10))
            if response.status_code == 200:
                if response:
                    return response
                else:
                    raise IndexError
            else:
                print("获取数据text页面出错 >>  response.status_code")
        except IndexError:
            response = session.get(url, timeout=(5, 10))
            if response.status_code == 200:
                if response:
                    return response
                else:
                    raise IndexError
            else:
                print("获取数据text页面出错 >>  response.status_code")
    async def Go_aio(self, list_date):
        sem = asyncio.Semaphore(1)
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(self.RunXiuRenPage(session, (list_date[0], url), sem)) for url in list_date]
            await asyncio.wait(tasks)
            await session.close()
    async def RunXiuRenPage(self, session, tuple_: tuple, sem):
        async with sem:
            res_ = await self.response_(session, tuple_[1])
            page_dict_s = await self.get_page_dict(res_, tuple_)
            for page_dict in page_dict_s:
                print(f"这是page_dict  >>>>   {page_dict}")

                page_dict['md5'] = await self.md5(page_dict['title'])
                test = await self.do_find({'md5': f"{page_dict['md5']}"})
                if not test:
                    new_page_dict = await self.get_all_images(session, page_dict)
                    print(f"这是新的     new_page_dict   >>>>   {new_page_dict}")
                    images = await self.img_all(session, new_page_dict)
                    new_page_dict.pop('img_page_list')
                    new_page_dict['images'] = images
                    new_page_dict['Up_time'] = await self.get_time()
                    if 'XiaoYu' in page_dict['url']:
                        new_page_dict['menu-item'] = 'XiaoYu画语界'
                    elif 'XiuRen' in page_dict['url']:
                        new_page_dict['menu-item'] = 'XiuRen秀人网'
                    elif 'MFStar' in page_dict['url']:
                        new_page_dict['menu-item'] = 'MFStar模范学院'
                    elif 'MiStar' in page_dict['url']:
                        new_page_dict['menu-item'] = 'MiStar魅妍社'
                    elif 'MyGirl' in page_dict['url']:
                        new_page_dict['menu-item'] = 'MyGirl美媛馆'
                    elif 'IMiss' in page_dict['url']:
                        new_page_dict['menu-item'] = 'Imiss爱蜜社'
                    elif 'BoLoli' in page_dict['url']:
                        new_page_dict['menu-item'] = 'BoLoli兔几盟'
                    elif 'YouWu' in page_dict['url']:
                        new_page_dict['menu-item'] = 'YouWu尤物馆'
                    elif 'Uxing' in page_dict['url']:
                        new_page_dict['menu-item'] = 'Uxing优星馆'
                    elif 'MiiTao' in page_dict['url']:
                        new_page_dict['menu-item'] = 'MiiTao蜜桃社'
                    elif 'FeiLin' in page_dict['url']:
                        new_page_dict['menu-item'] = 'FeiLin嗲囡囡'
                    elif 'WingS' in page_dict['url']:
                        new_page_dict['menu-item'] = 'WingS影私荟'
                    elif 'Taste' in page_dict['url']:
                        new_page_dict['menu-item'] = 'Taste顽味生活'
                    elif 'LeYuan' in page_dict['url']:
                        new_page_dict['menu-item'] = 'LeYuan星乐园'
                    elif 'HuaYan' in page_dict['url']:
                        new_page_dict['menu-item'] = 'HuaYan花の颜'
                    elif 'DKGirl' in page_dict['url']:
                        new_page_dict['menu-item'] = 'DKGirl御女郎'
                    elif 'MintYe' in page_dict['url']:
                        new_page_dict['menu-item'] = 'MintYe薄荷叶'
                    elif 'YouMi' in page_dict['url']:
                        new_page_dict['menu-item'] = 'YouMi尤蜜荟'
                    elif 'Candy' in page_dict['url']:
                        new_page_dict['menu-item'] = 'Candy糖果画报'
                    elif 'MTMeng' in page_dict['url']:
                        new_page_dict['menu-item'] = 'MTMeng模特联盟'
                    elif 'Micat' in page_dict['url']:
                        new_page_dict['menu-item'] = 'Micat猫萌榜'
                    elif 'HuaYang' in page_dict['url']:
                        new_page_dict['menu-item'] = 'HuaYang花漾'
                    elif 'XingYan' in page_dict['url']:
                        new_page_dict['menu-item'] = 'XingYan星颜社'
                    else:
                        pass
                    new_page_dict['domain'] = new_page_dict['domain'].rsplit('/', 1)[0]
                    print(new_page_dict)
                    await self.insert(new_page_dict)
                else:
                    print("本次数据已经存在于数据库中~~")
    async def img_all(self,session, new_page_dict):
        sexx_ = []
        for s_list in new_page_dict['img_page_list']:
            url = f"{new_page_dict['domain'].rsplit('/', 1)[0]}{s_list}"
            res_text = await self.response_(session, url)
            xpath_ = etree.HTML(res_text)
            img = xpath_.xpath('/html/body/div[3]/div/div/div[5]/p/img/@src')
            sexx_.append(img)
        return list(itertools.chain.from_iterable([i for i in sexx_]))
    async def get_all_images(self, session, page_dict):
        url = f"{page_dict['domain']}{page_dict['url']}"
        try:
            res_text = await self.response_(session, url)
            xpath_ = etree.HTML(res_text)
            page_dict['profiles'] = xpath_.xpath('/html/body/div[3]/div/div/div[1]/div/text()')[0].strip()
        except:
            url = f"{page_dict['domain'].rsplit('/', 1)[0]}{page_dict['url']}"
            res_text = await self.response_(session, url)
            xpath_ = etree.HTML(res_text)
            page_dict['profiles'] = xpath_.xpath('/html/body/div[3]/div/div/div[1]/div/text()')[0].strip()
        page_dict['img_page_list'] = []
        paaa = xpath_.xpath('/html/body/div[3]/div/div/div[4]/div/div/a/@href')
        page_dict['img_page_list'] = []
        for i in paaa:
            if i not in page_dict['img_page_list']:
                page_dict['img_page_list'].append(i)
        return page_dict
    async def get_page_dict(self, read_text, tuple_: tuple) -> list:
        xpath_ = etree.HTML(read_text)
        page_list = xpath_.xpath('/html/body/div[3]/div/div/ul/li')
        sa = []
        for a_page in page_list:
            data = {
                'domain': tuple_[0],
                'url': a_page.xpath('a/@href')[0],  # 单个图集url链接
                'title': a_page.xpath('a/@title')[0],  # 图集 名称
                'page_title': a_page.xpath('div/div[1]/text()')[0],  # page 下的title
                'page_pic': a_page.xpath('a/img/@src')[0],  # 图集 名称
                'page_time': a_page.xpath('div/div[2]/text()')[0],   # 更新时间
                'girl': a_page.xpath('a/div/span/text()')[0]
            }
            sa.append(data)
        return sa
    async def response_(self, session, url: str):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
        }
        async with session.get(url, timeout=35, headers=headers) as response:
            if response.status == 200:
                read_text = await response.text()
                return read_text
    async def md5(self, name):
        md5 = hashlib.md5()
        md5.update(name.encode())
        return md5.hexdigest()

if __name__ == '__main__':
    XiuRen()
