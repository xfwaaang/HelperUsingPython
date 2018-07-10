#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-05 16:29:00
# @Author  : xfwang
# @email   : xfwangmm@gmail.com

from win32com import client
import docx
import os
import time

class DocHelper(object):
	"""
	help to operate doc
	"""
	def word_2_pdf(word_path):
		"""
		convert word to pdf
		"""
		print('converting word ' + str(word_path) + ' to pdf...')
		word_dir = os.path.split(word_path)[0]
		word_name = os.path.splitext(os.path.split(word_path)[1])[0]
		out_file = os.path.join(word_dir, word_name + '--pdf-' + str(int(time.time())) + '.pdf')

		word = client.DispatchEx("Word.Application")
		worddoc = word.Documents.Open(word_path,ReadOnly = 1)
		worddoc.SaveAs(out_file, FileFormat = 17)
		worddoc.Close()
		print('save word as pdf ' + str(out_file))
		pass

	def excel_2_pdf(excel_path):
		"""
		convert excel to pdf
		"""
		print('converting excel ' + str(excel_path) + ' to pdf...')
		excel_dir = os.path.split(excel_path)[0]
		excel_name = os.path.splitext(os.path.split(excel_path)[1])[0]
		out_file = os.path.join(excel_dir, excel_name + '--pdf-' + str(int(time.time())) + '.pdf')

		xlApp = client.Dispatch("Excel.Application")
		excel = xlApp.Workbooks.Open(excel_path)
		excel.ExportAsFixedFormat(0, out_file)
		xlApp.Quit()
		print('save excel as pdf ' + str(out_file))
		pass

	def ppt_2_pdf(ppt_path):
		"""
		convert ppt to pdf
		"""
		print('converting ppt ' + str(ppt_path) + ' to pdf...')
		ppt_dir = os.path.split(ppt_path)[0]
		ppt_name = os.path.splitext(os.path.split(ppt_path)[1])[0]
		out_file = os.path.join(ppt_dir, ppt_name + '--pdf-' + str(int(time.time())) + '.pdf')

		p = client.Dispatch("PowerPoint.Application")
		ppt = p.Presentations.Open(ppt_path, False, False, False)
		ppt.ExportAsFixedFormat(out_file, 2, PrintRange=None)
		p.Quit()
		print('save ppt as pdf ' + str(out_file))
		pass

	def convert(path, fun):
		file_path_list = []
		# print(path)
		# print(path[0])
		if os.path.isdir(path[0]):
			# print('isdir')
			for file in os.listdir(path[0]):
				file_path = os.path.join(path[0], file)
				# print(file_path)
				if os.path.isdir(file):
					continue
				file_type = os.path.splitext(file_path)[1]
				# print(file_type)
				if not (file_type == '.doc' or file_type == '.docx' or file_type == '.ppt' or file_type == '.pptx' or file_type == '.xlsx'):
					continue
				file_path_list.append(file_path)
				# print(file_path)
		else:
			file_path_list = path
		print('There are ' + str(len(file_path_list)) + ' files to be converted')
		for file_path in file_path_list:
			# print(file_path)
			fun(file_path)
		pass

	# def convert_all(fun, dir_path):
	# 	file_path_list = []
	# 	for file in os.listdir(dir_path):
	# 		file_path = os.path.join(dir_path, file)
	# 		if os.path.isdir(file):
	# 			continue
	# 		file_type = os.path.splitext(file_path)[1]
	# 		if not file_type == '.doc' or file_type == '.docx' or file_type == '.ppt' or file_type == '.pptx' or file_type == '.xlsx':
	# 			continue
	# 		file_path_list.append(file_path)
	# 	convert(fun, file_path_list)
	# 	pass