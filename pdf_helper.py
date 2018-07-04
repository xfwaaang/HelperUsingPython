#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 08:19:00
# @Author  : xfwang
# @email   : xfwangmm@gmail.com

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
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

		print('spliting pdf ' + pdf_path)

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

key = sys.argv[1]
if key == 'merge':
	PDFHelper.merge(sys.argv[2:])
elif key == 'merge_all':
	PDFHelper.merge_all(sys.argv[2])
elif key == 'split':
	PDFHelper.split(sys.argv[2], sys.argv[3:])
	pass
else:
	print('input error!!!')
	
		