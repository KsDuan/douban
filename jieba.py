# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:28:51 2020

@author: DUAN
"""

# 1、表格库
import csv
import jieba
import numpy
from PIL import Image
from wordcloud import WordCloud

# 将数据从表格里读取出来
    # 设置星级等级
    stars = ("很差","较差","还行","推荐","力荐")
    # 设置空列表，装从表格里面读出来的所有数据
    comments = []
    # 打开表格，"r"读取模式  读取数据
    with open("D:\\workspace\\douban\\douban.csv","r",encoding="utf-8") as file:
        # 表格操作读数据
        reader = csv.reader(file)
        # 遍历表格里得到所有数据     [用户名,星级,评论]
        for i in reader:
            comments.append(i)
        # print(comments)
        file.close()
    # 将装有数据的列表返回出来

# 定义函数，将解析的评论做成词云
    # 调用函数：得到表格中所有的数据
    data = comments
    # 定义空的字符串，把所有的评论装进来
    str = ""
    # 遍历所有的数据
    for i in data:
        # [用户名, 星级, 评论]
        str+=i[2]
    # print(str)
    # 通过jieba分词器将评论里面的词语用空格分离出来
    cutWord = " ".join(jieba.cut(str))
    # print(cutWord)
    # 读取图片模型
    bgImg = numpy.array(Image.open("D:\\workspace\\douban\\model.jpg"))
    # 准备词云参数
    cloud = WordCloud(
        # 文字的路径：本地的系统文件路径
        font_path="C:\Windows\Fonts\STZHONGS.TTF",
        # 生成词云的图片背景
        background_color="white",
        # 参考图片（参数，没有引号）
        mask=bgImg
    ).generate(cutWord)
    # 将做成的结果生成图片
    cloud.to_file("D:\\workspace\\douban\\ciyun2.png")
