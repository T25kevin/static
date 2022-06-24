import motor.motor_asyncio
import asyncio



    # client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)   # 指定端口访问
    # client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:123456@localhost:27017')  # 使用链接访问

# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://g6370508:4826Ghp057@cluster0.qywbm.mongodb.net')  # 使用链接访问
# kano = client.kano
# XiuRen = kano.XiuRen
# async def do_find_one():
#     document = await kano.XiuRen.find_one()  # find_one只能查询一条数据
#     print(document)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_find_one())
# # {'_id': ObjectId('...'), 'i': 0}



class Image_Pust_():
    ####  文档地址  https://www.cnblogs.com/aduner/p/13532504.html
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://g6370508:4826Ghp057@cluster0.qywbm.mongodb.net')  # 使用链接访问
    kano = client.kano
    XiuRen = kano.XiuRen

    async def do_find_one(self):
        document = Image_Pust_().kano.XiuRen.find()  # find_one只能查询一条数据
        for documents in await document.to_list(length=100):
            print(documents)
    async def do_find(self, document=None):
        c = Image_Pust_().kano.XiuRen
        # async for document in c.find():
        #     print(document)
        return [i async for i in c.find(document)]

if __name__ == '__main__':
    asss = asyncio.get_event_loop().run_until_complete(Image_Pust_().do_find())
    # for i in asss:
    #     print(i)
    print(len(asss))
    girl_s = []
    for i in asss:
        if i['girl'] == '王馨瑶':
            page_img = f"{i['title']}  {i['domain']}{i['page_pic']}"
            print(page_img)
            for ii in i['images']:
                img_ = f"{i['title']}  https://p.xiurenb.com{ii}"
                print(img_)
            print(f'\n\n')
            girl_s.append(i)
    print(f"王馨瑶 一共有  {len(girl_s)} 部写真")

