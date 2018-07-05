# HelperUsingPython
使用Python实现常用的工作助手

- 批量重命名文件

```
PS E:\WorkSpace\HelperUsingPython> python helper.py rename_files E:\WorkSpace\HelperUsingPython\test
E:\WorkSpace\HelperUsingPython\test\3d.txt -> E:\WorkSpace\HelperUsingPython\test\第1章.txt
E:\WorkSpace\HelperUsingPython\test\bb.txt -> E:\WorkSpace\HelperUsingPython\test\第2章.txt
E:\WorkSpace\HelperUsingPython\test\ds.txt -> E:\WorkSpace\HelperUsingPython\test\第3章.txt
E:\WorkSpace\HelperUsingPython\test\gd.txt -> E:\WorkSpace\HelperUsingPython\test\第4章.txt
E:\WorkSpace\HelperUsingPython\test\gg.txt -> E:\WorkSpace\HelperUsingPython\test\第5章.txt
E:\WorkSpace\HelperUsingPython\test\qw.txt -> E:\WorkSpace\HelperUsingPython\test\第6章.txt
E:\WorkSpace\HelperUsingPython\test\rt.txt -> E:\WorkSpace\HelperUsingPython\test\第7章.txt
E:\WorkSpace\HelperUsingPython\test\tt.txt -> E:\WorkSpace\HelperUsingPython\test\第8章.txt
E:\WorkSpace\HelperUsingPython\test\vv.txt -> E:\WorkSpace\HelperUsingPython\test\第9章.txt
```

- 拼接给定的PDF文件
    
```
PS E:\WorkSpace\HelperUsingPython> python helper.py pdf_merge E:\WorkSpace\HelperUsingPython\test\test.pdf E:\WorkSpace\HelperUsingPython\test\test-1.pdf
There are 2 pdfs to be merged
merging E:\WorkSpace\HelperUsingPython\test\test.pdf
merging E:\WorkSpace\HelperUsingPython\test\test-1.pdf
save the merged pdf to E:\WorkSpace\HelperUsingPython\test\merge-1530680353.pdf
```
    
- 拼接给定目录下的所有PDF文件

```
PS E:\WorkSpace\HelperUsingPython> python helper.py pdf_merge_all E:\WorkSpace\HelperUsingPython\test
There are 5 pdfs to be merged
merging E:\WorkSpace\HelperUsingPython\test\hhh.pdf
merging E:\WorkSpace\HelperUsingPython\test\merge-1530680353.pdf
merging E:\WorkSpace\HelperUsingPython\test\test - 副本.pdf
merging E:\WorkSpace\HelperUsingPython\test\test-1.pdf
merging E:\WorkSpace\HelperUsingPython\test\test.pdf
save the merged pdf to E:\WorkSpace\HelperUsingPython\test\merge-1530680513.pdf
```

- 分割给定的PDF文件

```
PS E:\WorkSpace\HelperUsingPython> python helper.py pdf_split E:\WorkSpace\HelperUsingPython\test\ggg.pdf 4 10 15
spliting pdf E:\WorkSpace\HelperUsingPython\test\ggg.pdf to 4 parts 
save the splited pdf from page 0 to 4 to E:\WorkSpace\HelperUsingPython\test\ggg--0-4.pdf
save the splited pdf from page 5 to 10 to E:\WorkSpace\HelperUsingPython\test\ggg--5-10.pdf
save the splited pdf from page 11 to 15 to E:\WorkSpace\HelperUsingPython\test\ggg--11-15.pdf
save the splited pdf from page 16 to 20 to E:\WorkSpace\HelperUsingPython\test\ggg--16-20.pdf
```

- 为PDF添加文字水印

```
PS E:\WorkSpace\HelperUsingPython> python helper.py pdf-mark-word E:\WorkSpace\HelperUsingPython\test\IDN_XD.pdf 'hello world!'
creating word watermark...
the watermark is saved as E:\WorkSpace\HelperUsingPython\test\water_mark-1530712159.pdf
adding watermark...
the watermarked pdf is saved as E:\WorkSpace\HelperUsingPython\test\IDN_XD--watermarked-1530712160.pdf
```

<table align="center" border="0"><tr>
<td>
<img src="/files/文字水印.png" width="50%"/>
</td>
<td>
<img src="/files/文字水印PDF.png" width="50%"/>
</td>
</tr></table>

- 为PDF添加图片水印

```
PS E:\WorkSpace\HelperUsingPython> python helper.py pdf-mark-image E:\WorkSpace\HelperUsingPython\test\IDN_XD.pdf E:\Wor
kSpace\HelperUsingPython\test\test.png
creating word watermark...
the watermark is saved as E:\WorkSpace\HelperUsingPython\test\water_mark-1530714771.pdf
adding watermark...
the watermarked pdf is saved as E:\WorkSpace\HelperUsingPython\test\IDN_XD--watermarked-1530714772.pdf
```
<table align="center" border="0">
<tr>
<td><img src="/files/图片水印.png" width="50%"/></td>
<td><img src="/files/图片水印PDF.png" width="50%"/></td>
</tr>
</table>

- PDF转txt
```
PS E:\WorkSpace\HelperUsingPython> python helper.py pdf-2-txt E:\WorkSpace\HelperUsingPython\test\test.pdf
reading pdf E:\WorkSpace\HelperUsingPython\test\test.pdf ...
save pdf as txt E:\WorkSpace\HelperUsingPython\test\test--txt-1530763169.txt
```

- PDF转Word
```
PS E:\WorkSpace\HelperUsingPython> python helper.py pdf-2-word E:\WorkSpace\Help
erUsingPython\test\test.pdf
converting pdf E:\WorkSpace\HelperUsingPython\test\test.pdf to word ...
save pdf as word E:\WorkSpace\HelperUsingPython\test\test--doc-1530778603.doc
PS E:\WorkSpace\HelperUsingPython>
```

### ToDo
- [x] [批量重命名文件](/batch_rename_file.py)
- [ ] 批量下载百度图片 
- [ ] 批量下载视频
- [x] [PDF操作](/pdf_helper.py)
    - [x] 拼接，分割
    - [x] 加水印
    - [x] 转Word或文本
- [ ] Word文档操作--转PDF或文本
- [ ] Excel表格操作