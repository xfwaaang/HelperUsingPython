#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 08:19:00
# @Author  : xfwang
# @email   : xfwangmm@gmail.com

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from reportlab.pdfgen import canvas 
from reportlab.lib.units import cm 
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter,process_pdf
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from docx import Document
from io import StringIO
import os
import sys
import time

class PDFHelper(object):
	""" helper to operate PDF """

	# def merge(file_path_list):
	# 	"""
	# 	merge PDF files given
	# 	"""
	# 	pdfFileWriter = PdfFileWriter()

	# 	print('There are ' + str(len(file_path_list)) + ' pdfs to be merged')

	# 	for file_path in file_path_list:
	# 		print('merging ' + str(file_path))

	# 		pdfReader = PdfFileReader(file_path)

	# 		page_num = pdfReader.getNumPages()
	# 		for i in range(0, page_num):
	# 			page_obj = pdfReader.getPage(i)
	# 			pdfFileWriter.addPage(page_obj)

	# 	out_file = os.path.join(os.path.split(file_path_list[0])[0], 'merge-' + str(int(time.time())) + '.pdf')
	# 	pdfFileWriter.write(open(out_file, 'wb'))

	# 	print('save the merged pdf to the ' + str(out_file))
	# 	pass

	def merge(file_path_list):
		"""
		merge PDF files given 
		"""
		print('There are ' + str(len(file_path_list)) + ' pdfs to be merged')
		pdf_merge = PdfFileMerger()

		for file_path in file_path_list:
			print('merging ' + str(file_path))
			pdf_merge.append(file_path)

		out_file = os.path.join(os.path.split(file_path_list[0])[0], 'merge-' + str(int(time.time())) + '.pdf')
		pdf_merge.write(out_file)

		print('save the merged pdf to ' + str(out_file))
		pass

	def merge_all(path):
		"""
		merge all pdfs in the directory
		"""
		pdf_path_list = []
		file_list = os.listdir(path)
		for file in file_list:
			file_path = os.path.join(path, file)
			if os.path.isdir(file_path):
				continue
			file_type = os.path.splitext(file_path)[1]
			if file_type != '.pdf':
				continue
			pdf_path_list.append(file_path)
		PDFHelper.merge(pdf_path_list)
		pass

	def split(pdf_path, index_list):
		"""
		split the pdf
		pdf_path: absolute path of pdf file
		index_list: list of page index to be split
		"""
		pdf_reader = PdfFileReader(pdf_path)
		page_num = pdf_reader.getNumPages()
		index_list.append(page_num-1)
		start = 0

		print('spliting pdf ' + pdf_path + ' to ' + str(len(index_list)) + ' parts')

		for index in index_list:
			index = int(index)
			if index <= 0 or index >= page_num or index < start:
				continue
			pdf_writer = PdfFileWriter()
			for i in range(start, index+1):
				pdf_writer.addPage(pdf_reader.getPage(i))
			# 获取PDF所在目录和PDF文件名
			pdf_dir = os.path.split(pdf_path)[0]
			pdf_name = os.path.splitext(os.path.split(pdf_path)[1])[0]
			# 保存分割的PDF
			out_file = os.path.join(pdf_dir, pdf_name + '--' + str(start) + '-' + str(index) + '.pdf')
			pdf_writer.write(open(out_file, 'wb'))

			print('save the splited pdf from page ' + str(start) + ' to ' + str(index) + ' to ' + str(out_file))

			start = index + 1;
		pass

	def create_word_mark(content, path):
		"""
		create word watermark and save it to the directory of the pdf to be added watermark
		content: the words of watermark
		path: the absolute path of the pdf to be added watermark
		"""
	    #默认大小为21cm*29.7cm
		mark_pdf = os.path.join(os.path.split(path)[0], 'water_mark-' + str(int(time.time())) + '.pdf')
		c = canvas.Canvas(mark_pdf, pagesize = (30*cm, 30*cm))
		#移动坐标原点(坐标系左下为(0,0))
		c.translate(5*cm, 10*cm)
		                                                                                                                        
		#设置字体
		c.setFont("Helvetica", 50)
		# #指定描边的颜色
		# c.setStrokeColorRGB(1, 1, 1)
		# #指定填充颜色
		# c.setFillColorRGB(1, 1, 1)
		# #画一个矩形
		# c.rect(cm, cm, 7*cm, 7*cm, fill=1)
		                                                                                                                        
		#旋转25度，坐标系被旋转
		c.rotate(25)
		#指定填充颜色
		c.setFillColorRGB(0.6, 0.5, 0.4)
		#设置透明度，1为不透明
		# c.setFillAlpha(0.3)
		#画几个文本，注意坐标系旋转的影响
		# c.drawString(3*cm, 0*cm, content)
		c.setFillAlpha(0.6)
		c.drawString(6*cm, 3*cm, content)
		# c.setFillAlpha(1)
		# c.drawString(9*cm, 6*cm, content)
		                                                                                                                        
		#关闭并保存pdf文件
		c.save()
		return mark_pdf

	def create_image_mark(image, path):
		"""
		create image watermark and save it to the directory of the pdf to be added watermark
		image: the image of watermark
		path: the absolute path of the pdf to be added watermark
		"""
		mark_pdf = os.path.join(os.path.split(path)[0], 'water_mark-' + str(int(time.time())) + '.pdf')                                                                               
		c = canvas.Canvas(mark_pdf, pagesize = (30*cm, 30*cm))
		c.setFillAlpha(0.4) #设置透明度
		c.rotate(25)
		c.translate(5*cm, 5*cm)
		c.drawImage(image, 7*cm, 7*cm, 6*cm, 6*cm)    #这里的单位是物理尺寸
		c.save()
		return mark_pdf

	def add_mark(pdf, mark_pdf):
		"""
		add watermark
		"""
		# 获取PDF文件所在目录和PDF文件名
		pdf_dir = os.path.split(pdf)[0]
		pdf_name = os.path.splitext(os.path.split(pdf)[1])[0]

		pdf_reader = PdfFileReader(pdf)
		mark_pdf_reader = PdfFileReader(mark_pdf)
		mark_page = mark_pdf_reader.getPage(0)
		page_num = pdf_reader.getNumPages()
		pdf_writer = PdfFileWriter()
		for i in range(0, page_num):
			page = pdf_reader.getPage(i)
			page.mergePage(mark_page)
			pdf_writer.addPage(page)
		out_file = os.path.join(pdf_dir, pdf_name + '--' + 'watermarked-' + str(int(time.time())) + '.pdf')
		pdf_writer.write(open(out_file, 'wb'))
		print('the watermarked pdf is saved as ' + str(out_file))
		pass

	def read_pdf(pdf):
		"""
		read PDF file
		"""
		rsrcmgr = PDFResourceManager()
		retstr = StringIO()
		laparams = LAParams()
		device = TextConverter(rsrcmgr, retstr, laparams=laparams)

		process_pdf(rsrcmgr, device, open(pdf, 'rb'))
		device.close()

		content = retstr.getvalue()
		retstr.close()
		return content

	# def pdf_2_txt(pdf):
	# 	#rb以二进制读模式打开本地pdf文件
	# 	fn = open(pdf,'rb')
	# 	#创建一个pdf文档分析器
	# 	parser = PDFParser(fn)
	# 	#创建一个PDF文档
	# 	doc = PDFDocument()
	# 	#连接分析器 与文档对象
	# 	parser.set_document(doc)
	# 	doc.set_parser(parser)
	# 	# 提供初始化密码doc.initialize("lianxipython")
	# 	# 如果没有密码 就创建一个空的字符串
	# 	doc.initialize("")
	# 	# 检测文档是否提供txt转换，不提供就忽略
	# 	if not doc.is_extractable:
	# 		raise PDFTextExtractionNotAllowed
	# 	else:
	# 		#创建PDf资源管理器
	# 		resource = PDFResourceManager()
	# 		#创建一个PDF参数分析器
	# 		laparams = LAParams()
	# 		#创建聚合器,用于读取文档的对象
	# 		device = PDFPageAggregator(resource,laparams=laparams)
	# 		#创建解释器，对文档编码，解释成Python能够识别的格式
	# 		interpreter = PDFPageInterpreter(resource,device)
	# 		# 循环遍历列表，每次处理一页的内容
	# 		# doc.get_pages() 获取page列表
	# 		for page in doc.get_pages():
	# 			#利用解释器的process_page()方法解析读取单独页数
	# 			interpreter.process_page(page)
	# 			#使用聚合器get_result()方法获取内容
	# 			layout = device.get_result()
	# 			#这里layout是一个LTPage对象,里面存放着这个page解析出的各种对象
	# 			for out in layout:
	# 				#判断是否含有get_text()方法，获取我们想要的文字
	# 				if hasattr(out,"get_text"):
	#					# print(out.get_text())
	# 					with open('test.txt','ab') as f:
	# 						f.write((out.get_text()+'\n').encode('utf-8'))
	# 	pass

	def to_txt(pdf):
		"""
		convert pdf to txt
		"""
		pdf_dir = os.path.split(pdf)[0]
		pdf_name = os.path.splitext(os.path.split(pdf)[1])[0]
		print('reading pdf ' + str(pdf) + ' ...')
		content = PDFHelper.read_pdf(pdf)
		# print(content)
		out_file = os.path.join(pdf_dir, pdf_name + '--txt-' + str(int(time.time())) + '.txt')
		with open(out_file, 'wb') as file:
			file.write(content.encode('utf-8'))

		print('save pdf as txt ' + str(out_file))
		pass

	def to_word(pdf):
		"""
		convert pdf to word
		"""

		pass

# key = sys.argv[1]
# if key == 'merge':
# 	PDFHelper.merge(sys.argv[2:])
# elif key == 'merge_all':
# 	PDFHelper.merge_all(sys.argv[2])
# elif key == 'split':
# 	PDFHelper.split(sys.argv[2], sys.argv[3:])
# elif key == 'mark_word':
# 	print('creating word watermark...')
# 	mark_pdf = PDFHelper.create_word_mark(sys.argv[3], sys.argv[2])
# 	print('the watermark is saved as ' + str(mark_pdf))
# 	print('adding watermark...')
# 	PDFHelper.add_mark(sys.argv[2], mark_pdf)
# elif key == 'mark_image':
# 	print('creating image watermark...')
# 	mark_pdf = PDFHelper.create_image_mark(sys.argv[3], sys.argv[2])
# 	print('the watermark is saved as ' + str(mark_pdf))
# 	print('adding watermark...')
# 	PDFHelper.add_mark(sys.argv[2], mark_pdf)
# else:
# 	print('input error!!!')
	
		