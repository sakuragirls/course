#image对象的介绍
"""
Image 类是 Pillow 库中最为重要的类，该类被定义在和与其同名的 Image 模块中。
"""

#2.导入image对象
"""
from PIL import Image
"""


#3.open()
#3.1.介绍
"""
使用 Image 类的 open() 方法，可以创建一个 Image 对象，语法格式如下：
"""
#3.2.语法
"""
im = Image.open(fp,mode="r")
"""

#参数说明：
"""
fp：即 filepath 的缩写，表示图片路径，字符串格式；
mode：可选参数，若出现该参数，则必须设置为 "r"，否则会引发 ValueError 异常。
"""
"""
from PIL import Image
im=Image.open('E://everything/图片/二次元/kokomi.jpg')#打开一图片文件
im.show()#要显示图像需要调用 show()方法
"""


#4.image常用方法
#4.1.width,height:前者可以得知图片的宽，后者可以得知图片的长
"""
from PIL import Image
im=Image.open('E://everything/图片/二次元/kokomi.jpg')#打开一图片文件
print('图片的长为%s,图片的宽为%s'%(im.height,im.width))
"""



#4.2. format：查看图片的格式
"""
from PIL import Image
im=Image.open('E://everything/图片/二次元/kokomi.jpg')#打开一图片文件
print('该图片的格式为%s'%(im.format))
"""
#结果
"""
该图片的格式为JPEG
"""



#4.3.size：查看图像的尺寸
"""
from PIL import Image
im = Image.open('E://everything/图片/二次元/kokomi.jpg')
#或者通过size查看
print("图像的大小size:",im.size)
"""
#结果
"""
图像的大小size: (1748, 2480)
"""




#4.4.图片格式转换
#4.4.1.save
#4.4.1.1.介绍
"""
save() 方法用于保存图像，当不指定文件格式时，它会以默认的图片格式来存储；
如果指定图片格式，则会以指定的格式存储图片。
"""
#4.4.1.2.语法
"""
Image.save(fp, format=None)
参数说明如下：
fp：图片的存储路径，包含图片的名称，字符串格式；
format：可选参数，可以指定图片的格式。
"""
"""
from PIL import Image
im = Image.open('E://everything/图片/二次元/kokomi.jpg')
im.save('E://everything/图片/二次元/2.bmp')
"""
#4.4.1.3.注意
"""
使用save()保存修改后的图片，图片名必须重新命名。
"""


#4.4.2.convert()+save()
#4.4.2.1.介绍
"""
注意，并非所有的图片格式都可以用 save() 方法转换完成，比如将 PNG 格式的图片保存为 JPG 格式.
Image 类提供的 convert() 方法可以实现图像模式的转换。

"""
#4.4.2.2.语法
"""
convert(mode,parms**)
mode：指的是要转换成的图像模式；
params：其他可选参数。
"""
"""
from PIL import Image
im = Image.open('E://everything/图片/二次元/kokomi.bmp')
#此时返回一个新的image对象，转换图片模式
image=im.convert('RGB')
#调用save()保存
image.save('E://everything/图片/二次元')
"""



#4.5.resize():实现任意缩小和放大图像。
"""
from PIL import Image
im = Image.open('E://everything/图片/二次元/kokomi.bmp')
ims=im.resize((800,800))
ims.save('E://everything/图片/二次元/1.bmp') #对缩放后的图片进行保存，图片名也要改

"""