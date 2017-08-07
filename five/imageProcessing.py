#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 依赖包
import heapq
import cv2

# 正面图片预处理
def frontPicture(path):

    ## 原先识别过程 定点裁剪 对照片要求高
    # img = cv2.imread(path, 0)
    # img = cv2.resize(img, (2100, 1480))
    # heigth = 480
    # width = 630
    # img = img[heigth:heigth + 540, width:width + 856]
    #
    ## 高斯模糊 二值处理
    # blur = cv2.GaussianBlur(img, (1, 1), 0)
    # retval, binarized = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # # print "front retval:",retval
    #
    ## 缓存路径
    # tempPath="temp/temp.jpg"
    # cv2.imwrite(tempPath,binarized)
    # from indentify import frontPictureIdentify
    # return frontPictureIdentify(tempPath)


    # 改进后图片处理
    img = cv2.imread(path, 0)

    # 测试用 规定大小 方便调试
    # img = cv2.resize(img,(900,600))

    # 显示图片 测试用
    # cv2.imshow("orginal",img)
    # cv2.waitKey(0)

    # 高斯模糊 qtsu二值
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    retval, binarized = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 算出的阈值
    # print "retval:",retval

    # 显示图片 测试用
    # cv2.imshow("binarized",binarized)
    # cv2.waitKey(0)

    # 膨胀图片 方便裁剪
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilated = cv2.dilate(binarized, kernel)

    # 框选图片
    _, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # 测试用 画框
    # cv2.drawContours(img, contours,-1, (255, 255, 255), 3)

    # 保存所有框选出的图像宽度
    widths = []
    for index, cnt in enumerate(contours):
        x, y, width, height = cv2.boundingRect(cnt)
        widths.insert(index, width)

    # 寻找最长的一个宽度
    IDList = heapq.nlargest(1, widths)

    # 找出最长的这个图形的矩形框
    IDcnts = []
    for index, item in enumerate(IDList):
        index2 = widths.index(item)
        IDcnts.insert(index, contours[index2])

    # 裁剪图像
    IDimgs = []
    for index, IDcnt in enumerate(IDcnts):
        x, y, w, h = cv2.boundingRect(IDcnt)
        IDimg = img[y: y + h, x: x + w]
        IDimgs.insert(index, IDimg)

    # 显示图片 测试用
    # cv2.imshow("Cut Picture", IDimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # 高斯模糊 二值处理
    blur = cv2.GaussianBlur(IDimg, (1, 1), 0)
    retval, binarized = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # print "front retval:",retval

    # 缓存在本地
    tempPath = "temp/front.jpg"
    cv2.imwrite(tempPath, IDimg)

    # 回调功能
    from indentify import frontPictureIdentify
    return frontPictureIdentify(tempPath)

# 背面图像预处理
def backPicture(path):

    ## 原先识别过程 定点裁剪 对照片要求高
    # img = cv2.imread(path, 0)
    # img = cv2.resize(img, (2100, 1480))
    # heigth = 480
    # width = 630
    # img = img[heigth:heigth + 540, width:width + 856]
    #
    ## 高斯模糊 二值处理
    # blur = cv2.GaussianBlur(img, (3, 3), 0)
    # retval, binarized = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # # print "front retval:",retval
    #
    # tempPath="temp/temp2.jpg"
    # cv2.imwrite(tempPath,binarized)
    # from indentify import backPictureIdentify
    # return backPictureIdentify(tempPath)

    # 改进后图像处理
    img = cv2.imread(path, 0)

    # 测试用 规定大小 方便调试
    # img = cv2.resize(img,(900,600))

    # 显示图片 测试用
    # cv2.imshow("orginal",img)
    # cv2.waitKey(0)

    # 高斯模糊 qtsu二值
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    retval, binarized = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 算出的阈值
    # print "retval:",retval

    # 显示图片 测试用
    # cv2.imshow("binarized",binarized)
    # cv2.waitKey(0)

    # 膨胀图片 方便裁剪
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilated = cv2.dilate(binarized, kernel)

    # 框选图片
    _, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # 测试用 画框
    # cv2.drawContours(img, contours,-1, (255, 255, 255), 3)

    # 保存所有框选出的图像宽度
    widths = []
    for index, cnt in enumerate(contours):
        x, y, width, height = cv2.boundingRect(cnt)
        widths.insert(index, width)

    # 寻找最长的一个宽度
    IDList = heapq.nlargest(1, widths)

    # 找出最长的这个图形的矩形框
    IDcnts = []
    for index, item in enumerate(IDList):
        index2 = widths.index(item)
        IDcnts.insert(index, contours[index2])

    # 裁剪图像
    IDimgs = []
    for index, IDcnt in enumerate(IDcnts):
        x, y, w, h = cv2.boundingRect(IDcnt)
        IDimg = img[y: y + h, x: x + w]
        IDimgs.insert(index, IDimg)

    # 显示图片 测试用
    # cv2.imshow("Cut Picture", IDimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 高斯模糊 二值处理
    blur = cv2.GaussianBlur(IDimg, (7, 7), 0)
    retval, binarized = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # print "front retval:",retval

    # 缓存在本地
    tempPath = "temp/back.jpg"
    cv2.imwrite(tempPath, binarized)

    # 回调功能
    from indentify import backPictureIdentify
    return backPictureIdentify(tempPath)
