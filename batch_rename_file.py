#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-03 16:51:40
# @Author  : xfwang
# @email   : xfwangmm@gmail.com

import os
import sys

def batch_rename_file(path):
	"""batch rename all files in the directory"""
	file_list = os.listdir(path)
	i = 1
	for file in file_list:
		old_file = os.path.join(path, file) 
		if os.path.isdir(old_file):
			continue
		file_name = os.path.splitext(file)[0]
		file_type = os.path.splitext(file)[1]
		new_file_name = file_name.replace(file_name, '--' + str(i))
		i += 1
		new_file = os.path.join(path, new_file_name + file_type)
		os.rename(old_file, new_file)

		print(old_file + ' -> ' + new_file)
	pass


batch_rename_file(sys.argv[1])

# path = r'E:\WorkSpace\HelperUsingPython\test'
# batch_rename_file(path)
# input()