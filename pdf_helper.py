#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 08:19:00
# @Author  : xfwang
# @email   : xfwangmm@gmail.com

from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import sys

class PDFHelper(object):
	""" helper to operate PDF """

	def merge(file_path_list):
		"""
		merge PDF files given
		"""
		pdfFileWriter = PdfFileWriter()

		print('pdfs to be merged: ' + str(file_path_list))

		for file_path in file_path_list:
			print('merging ' + str(file_path))

			pdfReader = PdfFileReader(file_path)

			page_num = pdfReader.getNumPages()
			for i in range(0, page_num):
				page_obj = pdfReader.getPage(i)
				pdfFileWriter.addPage(page_obj)

		out_file = os.path.join(os.path.split(file_path_list[0])[0], 'merge.pdf')
		pdfFileWriter.write(open(out_file, 'wb'))
		
		print('save the merged pdf to the ' + str(out_file))
		pass

PDFHelper.merge(sys.argv[1:])

	# def merge(path):
	# 	pdf_path_list = []
	# 	for root, dir, file in os.walk(path):
	# 		if os.path.splitext(file)[1] == '.pdf':
	# 			continue
	# 		pdf_path_list.append(os.path.join(root, file))
	# 	merge(pdf_path_list)
	# 	pass
	
		