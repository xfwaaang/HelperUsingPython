#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-05 08:11:28
# @Author  : xfwang
# @email   : xfwangmm@gmail.com

from pdf_helper import PDFHelper
from doc_helper import DocHelper
from batch_rename_file import batch_rename_file
import sys

key = sys.argv[1]
if key == 'rename-files':
	batch_rename_file(sys.argv[2])
elif key == 'pdf-merge':
	PDFHelper.merge(sys.argv[2:])
elif key == 'pdf-merge-all':
	PDFHelper.merge_all(sys.argv[2])
elif key == 'pdf-split':
	PDFHelper.split(sys.argv[2], sys.argv[3:])
elif key == 'pdf-mark-word':
	print('creating word watermark...')
	mark_pdf = PDFHelper.create_word_mark(sys.argv[3], sys.argv[2])
	print('the watermark is saved as ' + str(mark_pdf))
	print('adding watermark...')
	PDFHelper.add_mark(sys.argv[2], mark_pdf)
elif key == 'pdf-mark-image':
	print('creating image watermark...')
	mark_pdf = PDFHelper.create_image_mark(sys.argv[3], sys.argv[2])
	print('the watermark is saved as ' + str(mark_pdf))
	print('adding watermark...')
	PDFHelper.add_mark(sys.argv[2], mark_pdf)
elif key == 'pdf-2-txt':
	PDFHelper.to_txt(sys.argv[2])
elif key == 'pdf-2-word':
	PDFHelper.to_word(sys.argv[2])
elif key == 'word-2-pdf':
	DocHelper.word_2_pdf(sys.argv[2])
elif key == 'excel-2-pdf':
	DocHelper.excel_2_pdf(sys.argv[2])
elif key == 'ppt-2-pdf':
	DocHelper.ppt_2_pdf(sys.argv[2])
elif key == 'extract-tables':
	DocHelper.extract_tables(sys.argv[2])
else:
	print('input error!!!')