#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 依赖包
import cv2
import os
import json
import sys
from opencv import imageProcessing

# 正面图片预处理
def frontPicture(path):
    try:
        if (not os.path.isfile(path)):
            print  "文件不存在"
            data = {
                "code": -1,
                "error": "上传失败"
            }
            # json封装
            errorData = json.dumps(data)
            return errorData
        # 调用图片处理
        dst = imageProcessing(path)

        # 缓存在本地 判断是否存在此文件夹 没有就创建一个
        if not os.path.exists('temp'):
            os.makedirs('temp')
        tempPath = "temp/front.jpg"

        cv2.imwrite(tempPath, dst)
    except BaseException:
        print "！！！！请处理异常：", sys.exc_info()

    # 回调识别功能
    from indentify import frontPictureIdentify
    return frontPictureIdentify(tempPath)

# 背面图像预处理
def backPicture(path):
    try:
        if(not os.path.isfile(path)):
            print  "文件不存在"
            data = {
                "code": -1,
                "error": "上传失败"
            }
            # json封装
            errorData = json.dumps(data)
            return errorData
        # 调用图片处理
        dst = imageProcessing(path)
        """
            函数cv2.imwrite（）来保存图像。
                第一个参数是文件名(可以带路径)，第二个参数是要保存的图像。
        """
        # 缓存在本地
        if not os.path.exists('temp'):
            os.makedirs('temp')
        tempPath = "temp/back.jpg"
        cv2.imwrite(tempPath, dst)
    except BaseException:
        print "！！！！请处理异常：", sys.exc_info()

    # 回调识别功能
    from indentify import backPictureIdentify
    return backPictureIdentify(tempPath)

