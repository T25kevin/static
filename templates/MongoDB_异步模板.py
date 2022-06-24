import motor.motor_asyncio
import asyncio



class Image_Pust_():
    ####  文档地址  https://www.cnblogs.com/aduner/p/13532504.html
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://g6370508:4826Ghp057@cluster0.qywbm.mongodb.net')  # 使用链接访问
    kano = client.kano
    XiuRen = kano.XiuRen

    async def do_find_one(self):
        document = Image_Pust_().kano.XiuRen.find()  # find_one只能查询一条数据
        for documents in await document.to_list(length=100):
            print(documents)

    async def do_find(self, document: dict):
        c = Image_Pust_().kano.XiuRen
        return [i async for i in c.find(document)]

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    a = loop.run_until_complete(Image_Pust_().do_find({}))
    print(a)