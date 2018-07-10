#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-05 08:11:28
# @Author  : xfwang
# @email   : xfwangmm@gmail.com

from pdf_helper import PDFHelper
from doc_helper import DocHelper
from batch_rename_file import batch_rename_file
from dl_img import DLImg
from dl_video import DLVideo
import sys

if len(sys.argv) < 2:
	print('User Manual:')
	print(' 1. helper rename-files [directory-path]:\n    rename all files in the given directory')
	print(' 2. helper pdf-merge [pdf-path-1] [pdf-path-2] ... [pdf-path-n]:\n    merge the given pdfs')
	print(' 3. helper pdf-merge-all [directory-path]:\n    merge all pdfs in the given directory')
	print(' 4. helper pdf-split [pdf-path] [index-1] [index-2] ... [index-n]:\n    split the given pdf to specified parts(n+1)')
	print(' 5. helper pdf-mark-word [pdf-path] [words]:\n    add word watermark to the given pdf')
	print(' 6. helper pdf-mark-img [pdf-path] [image-path]:\n    add image watermark to the given pdf')
	print(' 7. helper pdf-2-txt [pdf-path]:\n    convert the given pdf to txt')
	print(' 8. helper pdf-2-word [pdf-path]:\n    convert the given pdf to word')
	print(' 9. helper word-2-pdf [word-path...]|[directory-path]:\n    convert all the given word(in the directory) to pdf')
	print('10. helper excel-2-pdf [excel-path...]|[directory-path]:\n    convert all the given excel(in the directory) to pdf')
	print('11. helper ppt-2-pdf [ppt-path...]|[directory-path]:\n    convert all the gievn ppt(in the directory) to pdf')
	print('12. helper dl-img [url]:\n    batch download images from https://pixabay.com/')
	print('13. helper dl-video [url]:\n    batch download videos from v.qq.com')
else:
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
	elif key == 'pdf-mark-img':
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
		# DocHelper.word_2_pdf(sys.argv[2])
		DocHelper.convert(sys.argv[2:], fun = DocHelper.word_2_pdf)
	elif key == 'excel-2-pdf':
		# DocHelper.excel_2_pdf(sys.argv[2])
		DocHelper.convert(sys.argv[2:], fun = DocHelper.excel_2_pdf)
	elif key == 'ppt-2-pdf':
		# DocHelper.ppt_2_pdf(sys.argv[2])
		DocHelper.convert(sys.argv[2:], fun = DocHelper.ppt_2_pdf)
	elif key == 'dl-img':
		DLImg.dlImg(sys.argv[2])
	elif key == 'dl-video':
		DLVideo.dlVideos(sys.argv[2])
	else:
		print('Input error!!!')
		print('Errors may occur if the file path contains spaces!!!')
