#label为为指定的窗口添加图像与文本


from tkinter import *

windows=Tk()
windows.title('welcome')
windows.geometry('400*400')
w=Label(windows,text="hello") #text="hello"是给窗口windows显示文本'hello',windows是建立窗口的对象，给label指定添加对象
w.grid(column=0,row=0)  #grid是给label添加的文本‘hello’设定位置
windows.mainloop()