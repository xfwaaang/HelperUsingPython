#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-05 08:11:28
# @Author  : xfwang
# @email   : xfwangmm@gmail.com

from pdf_helper import PDFHelper
from batch_rename_file import batch_rename_file
import sys

key = sys.argv[1]
if key == 'rename_files':
	batch_rename_file(sys.argv[2])
elif key == 'pdf_merge':
	PDFHelper.merge(sys.argv[2:])
elif key == 'pdf_merge_all':
	PDFHelper.merge_all(sys.argv[2])
elif key == 'pdf_split':
	PDFHelper.split(sys.argv[2], sys.argv[3:])
elif key == 'pdf_mark_word':
	print('creating word watermark...')
	mark_pdf = PDFHelper.create_word_mark(sys.argv[3], sys.argv[2])
	print('the watermark is saved as ' + str(mark_pdf))
	print('adding watermark...')
	PDFHelper.add_mark(sys.argv[2], mark_pdf)
elif key == 'pdf_mark_image':
	print('creating image watermark...')
	mark_pdf = PDFHelper.create_image_mark(sys.argv[3], sys.argv[2])
	print('the watermark is saved as ' + str(mark_pdf))
	print('adding watermark...')
	PDFHelper.add_mark(sys.argv[2], mark_pdf)
elif key == 'pdf_2_txt':
	PDFHelper.to_txt(sys.argv[2])
else:
	print('input error!!!')