from  pymongo import MongoClient
from gridfs import *
import os
client = MongoClient("mongodb://127.0.0.1:27017")
db = client["douyu"]
images = db["images"]
dirs = "c:/users/administrator/douyu/images/"
files = os.listdir(dirs)
for file in files :
    # 图片的全路径
    fileName = dirs + file
    # 区分图片的格式和名称
    f = file.split(".")
    # 打开图片文件
    datatmp = open(fileName,"rb")
    # 创建写入流
    inputImg = GridFS(db)
    # 将图片写入数据库
    insertImg = inputImg.put(datatmp,filename=f[0],content_type=f[1])
    datatmp.close()