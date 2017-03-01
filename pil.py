#!/usr/bin/python
#coding=utf-8

import Image,ImageFilter,ImageDraw,ImageFont
import random

im = Image.open('/Library/WebServer/Documents/mainwork/storestatic/html/images/aboutus/1.jpg')
# 获得图像尺寸:
w,h = im.size

# 缩放到50%:
im.thumbnail((w//2, h//2))

# 把缩放后的图像用jpeg格式保存:
im.save('/Users/guoruiqing/skill/serverlet/python/basic/test.jpg','jpeg')	

#模糊效果
im2 = im.filter(ImageFilter.BLUR)
im2.save('/Users/guoruiqing/skill/serverlet/python/basic/test1.jpg','jpeg')

#生成字母验证码


#随机字母:
def rndChar():
	return chr(random.randint(65,90))
	
#随机颜色1:
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色2:
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))	
	
width = 60 * 4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
#创建font对象：
font = ImageFont.truetype('Arial.ttf', 36)
#创建draw对象：
draw = ImageDraw.Draw(image)

#填充每个像素：
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())

#输出文字:
for t in range(4):
	draw.text((60 * t + 10, 10)	,rndChar(),font=font,fill = rndColor2())	

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('/Users/guoruiqing/skill/serverlet/python/basic/code.jpg','jpeg')				
		
		