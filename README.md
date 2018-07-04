# HelperUsingPython
使用Python实现常用的工作助手

- 批量重命名文件

```
PS E:\WorkSpace> python batch_rename_file.py E:\WorkSpace\test
E:\WorkSpace\test\3d.txt -> E:\WorkSpace\test\第1章.txt
E:\WorkSpace\test\bb.txt -> E:\WorkSpace\test\第2章.txt
E:\WorkSpace\test\ds.txt -> E:\WorkSpace\test\第3章.txt
E:\WorkSpace\test\gd.txt -> E:\WorkSpace\test\第4章.txt
E:\WorkSpace\test\gg.txt -> E:\WorkSpace\test\第5章.txt
E:\WorkSpace\test\qw.txt -> E:\WorkSpace\test\第6章.txt
E:\WorkSpace\test\rt.txt -> E:\WorkSpace\test\第7章.txt
E:\WorkSpace\test\tt.txt -> E:\WorkSpace\test\第8章.txt
E:\WorkSpace\test\vv.txt -> E:\WorkSpace\test\第9章.txt
```

- 拼接给定的PDF文件
    
```
PS E:\WorkSpace\HelperUsingPython> python pdf_helper.py merge E:\WorkSpace\HelperUsingPython\test\test.pdf E:\WorkSpace\HelperUsingPython\test\test-1.pdf
There are 2 pdfs to be merged
merging E:\WorkSpace\HelperUsingPython\test\test.pdf
merging E:\WorkSpace\HelperUsingPython\test\test-1.pdf
save the merged pdf to E:\WorkSpace\HelperUsingPython\test\merge-1530680353.pdf
```
    
- 拼接给定目录下的所有PDF文件

```
PS E:\WorkSpace\HelperUsingPython> python pdf_helper.py merge_all E:\WorkSpace\HelperUsingPython\test
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
PS E:\WorkSpace\HelperUsingPython> python pdf_helper.py split E:\WorkSpace\HelperUsingPython\test\ggg.pdf 4 10 15
spliting pdf E:\WorkSpace\HelperUsingPython\test\ggg.pdf to 4 parts 
save the splited pdf from page 0 to 4 to E:\WorkSpace\HelperUsingPython\test\ggg--0-4.pdf
save the splited pdf from page 5 to 10 to E:\WorkSpace\HelperUsingPython\test\ggg--5-10.pdf
save the splited pdf from page 11 to 15 to E:\WorkSpace\HelperUsingPython\test\ggg--11-15.pdf
save the splited pdf from page 16 to 20 to E:\WorkSpace\HelperUsingPython\test\ggg--16-20.pdf
```

- 添加文字水印

```
PS E:\WorkSpace\HelperUsingPython> python pdf_helper.py mark_word E:\WorkSpace\HelperUsingPython\test\IDN_XD.pdf 'hello world!'
the watermark is saved as E:\WorkSpace\HelperUsingPython\test\water_mark-1530712159.pdf
the watermarked pdf is saved as E:\WorkSpace\HelperUsingPython\test\IDN_XD--watermarked-1530712160.pdf
```

![文字水印](/files/文字水印.png)
<center>
<img src="/files/文字水印PDF.png" width="25%" height="25%" />
添加文字水印的PDF
</center>

### ToDo
- [x] 批量重命名文件
- [ ] 批量下载百度图片 
- [ ] 批量下载视频
- [ ] PDF操作
    - [x] 拼接，分割
    - [x] 加水印
    - [ ] 转Word或文本
- [ ] Word文档操作--转PDF或文本
- [ ] Excel表格操作