#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-09 21:41:45
# @Author  : xfwang
# @email   : xfwangmm@gmail.com

import urllib.request
import urllib
import re
import os
import time

class DLImg(object):
	"""docstring for DlImg"""
	def getHtml(url):
		head = {}
		head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
		req = urllib.request.Request(url, headers=head)
		return urllib.request.urlopen(req).read().decode('utf-8')
		pass

	def getImg(html):
		# reg = 'src=".+?\.jpg" alt='
		# 找出jpg链接
		reg = r'https.{50,80}\.jpg|https.{50,80}\.png'
		imgre = re.compile(reg)
		imgurls = re.findall(imgre, html)
		# 提取出jpg名称
		regname = r'\w+-.+\.jpg|\w+-.+\.png'
		namere = re.compile(regname)
		# 去重
		imgurls = set(imgurls)
		print('There are ' + str(len(imgurls)) + ' pictures to be downloaded which all will be saved in the current directory.')
		for imgurl in imgurls:
			imgname = re.findall(namere, imgurl)[0]
			# print(imgurl)
			print(imgname)
			urllib.request.urlretrieve(imgurl, imgname)
		pass

	def dlImg(url):
		DLImg.getImg(DLImg.getHtml(url))
		pass


# def getImg(html):
#     reg = 'src="(.+?\.jpg)"'        #正则表达式
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre, html.decode('utf-8'))
#     x = 1
#     for imgurl in imglist  :
#         urllib.request.urlretrieve(imgurl,'%s.jpg' % x)    # 设置了要下载的图片资源路径和要命名的名字
#         print('正在下载第%s张图片' % x)
#         x+=1
#         if x>6:                     #设置爬取图片的张数
#             break
#     return None

# <img srcset="https://cdn.pixabay.com/photo/2018/07/04/23/17/soap-bubbles-3517247__340.jpg 1x, 
# https://cdn.pixabay.com/photo/2018/07/04/23/17/soap-bubbles-3517247__480.jpg 2x" 
# src="https://cdn.pixabay.com/photo/2018/07/04/23/17/soap-bubbles-3517247__340.jpg" 
# alt="肥皂泡沫, 丰富多彩, 飞, 使肥皂泡沫, 镜像, 肥皂水, 球" 
# title="肥皂泡沫, 丰富多彩, 飞, 使肥皂泡沫, 镜像, 肥皂水, 球">

# url = 'https://pixabay.com/zh/photos/?'
# print(DLImg.getHtml(url))
# DLImg.getImg(DLImg.getHtml(url))
		