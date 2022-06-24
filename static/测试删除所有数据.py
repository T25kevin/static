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


if __name__ == '__main__':
    a = Image_Push()
    # b = a.find()
    # for i in b:
    #     print(i['title'])
    #     a.delete({'title': i['title']})
    s_dict = {'title': '[XiuRen秀人网]No.5120_模特田冰冰酒店室内性感捆带式装扮露傲人豪乳极致诱惑写真48P'}
    sq = a.find(s_dict)
    print(sq)
    a.delete(s_dict)
    sq = a.find(s_dict)
    print(sq)