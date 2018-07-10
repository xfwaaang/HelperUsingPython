#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-10 11:43:02
# @Author  : xfwang
# @email   : xfwangmm@gmail.com
from bs4 import BeautifulSoup
import urllib.request
import urllib
import os

class DLVideo(object):
	"""docstring for DLVideo"""
	def getHtml(url):
		head = {}
		head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
		req = urllib.request.Request(url, headers=head)
		return urllib.request.urlopen(req).read().decode('utf-8')
		pass

	def getUrlsFromQQ(html):
		"""
		get video url list from detail page of v.qq.com 
		"""
		soup = BeautifulSoup(html, 'html.parser')
		tags = soup.find('div', class_ = 'mod_episode').find_all('a')
		urls = []
		for tag in tags:
			url = tag['href']
			urls.append(url)
		return urls
		pass

	def dlVideos(url):
		"""
		batch download videos from the given url
		"""
		qq = 'v.qq.com'
		html = DLVideo.getHtml(url)

		urls = []
		if url.find(qq) != -1:
			# v.qq.com
			urls = DLVideo.getUrlsFromQQ(html)

		print('There are ' + str(len(urls)) + ' videos to be downloaded ...')

		for url in urls:
			print(url)
			os.system('you-get ' + url)
		pass

# url = 'https://v.qq.com/detail/6/639agzdh10yu2q2.html'
# DLVideo.getUrlsFromQQ(DLVideo.getHtml(url))
# DLVideo.dlVideos(url)