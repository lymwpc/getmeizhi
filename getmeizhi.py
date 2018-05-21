#第一部分：利用request模块完成数据的“爬”，利用正则表达式re模块完成数据的“提取”
import urllib.request
import re
url = "http://www.27270.com/ent/meinvtupian/"  #获取url，得到我们要爬取的网页页面地址
pat = 'http://t1.27270.com/uploads/tu(.*?)jpg'  #匹配规则，通过分析得到规律
data = urllib.request.urlopen(url).read().decode("gb2312") #读取网页的内容并解码
relut = re.compile(pat).findall(data)       #会返回一个列表
file = open(r"G:python_workspace\getmeizhi\urltu.txt", "w", encoding="gb2312")  #这里我定义了一个自己的存储路径，大家可以根据自己的路径修改
for i in relut:
    file.write("http://t1.27270.com/uploads/tu")  #先写进开头
    file.write(i)        #将提取的内容写入文件
    file.write("jpg")    # 将格式写入
    file.write("\n")    #表示换行
#第二部分：将urltu.txt中的图片链接转换成图片	
import os
from  urllib import request
read = open(r"G:python_workspace\getmeizhi\urltu.txt", "r", encoding="gb2312")
s = read.readlines()
print(s)
print("正在爬取，请稍后！")
q = 1                       #设置图片名称从1开始
os.chdir(r"G:python_workspace\getmeizhi\美女图片")     #指定存储路径
for i in s:
    request.urlretrieve(i, filename=str(q)+".jpg")   # i为图片地址，filename是图片的名称   
    q=q+1
print("爬取完成！")
