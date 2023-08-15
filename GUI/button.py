#给窗口添加button
from tkinter import *
windows=Tk()
windows.title('welcome')
btn=Button(windows,text='确定')#Button()用于给窗口创建按钮，text参数是给按钮添加文本
btn.grid(column=0,row=1)#给按钮确定位置
windows.mainloop()