#-*- coding:utf-8 -*-
exec('import pyautogui')
#import pyautogui
import tkinter as tk
import multiprocessing,sys

x, y = 0, 0
xstart,ystart = 0 ,0
xend,yend = 0, 0
rec = ''
#pat=os.path.split(sys.argv[0])[0]+'\\'+'sept.png'
def move(event):
    global x, y ,xstart,ystart
    new_x = (event.x-x)+canvas.winfo_x()
    new_y = (event.y-y)+canvas.winfo_y()
    s = "300x200+" + str(new_x)+"+" + str(new_y)    
    canvas.place(x = new_x - xstart,y = new_y -ystart)   
    #print("s = ", s)
    #print(rot.winfo_x(), rot.winfo_y())
    #print(event.x, event.y)
def button_1(event):
    global x, y ,xstart,ystart
    global rec
    x, y = event.x, event.y
    xstart,ystart = event.x, event.y
    #print("event.x, event.y = ", event.x, event.y)
    xstart,ystart = event.x, event.y  
    cv.configure(height=1)
    cv.configure(width=1)
    cv.config(highlightthickness=0) # 无边框
    cv.place(x=event.x, y=event.y)
    rec = cv.create_rectangle(0,0,0,0,outline='blue',width=4,dash=(1, 1))
def b1_Motion(event):
    global x, y,xstart,ystart
    x, y = event.x, event.y
    #print("event.x, event.y = ", event.x, event.y)
    cv.configure(height = event.y - ystart)
    cv.configure(width = event.x - xstart)
    cv.coords(rec,0,0,event.x+xstart,event.y+ystart)
def buttonRelease_1(event):
    global xend,yend
    xend, yend = event.x, event.y
#截屏并保存图片
def button_3(event):
    global xstart,ystart,xend,yend,pat,cv,canvas,rot,full
    cv.delete(rec)
    cv.place_forget()
    img = pyautogui.screenshot(region=[xstart,ystart,xend-xstart,yend-ystart]) # x,y,w,h
    img.save(pat)#####这里是保存
    try:
        with open(pat,'rb') as f:
            full=f.read()
    except:
        full=None
    cv.destroy()
    canvas.destroy()
    rot.destroy()
    return full
def sys_out(even):
    global cv, canvas,rot,pat,full
    cv.destroy()
    canvas.destroy()
    rot.destroy()
    full=False
    return full
#运行
def run(patt='sept.png'):
    global x, y,xstart,ystart,xend,yend,rec,cv,rot,canvas,pat
    multiprocessing.freeze_support()
    pat=patt
    rot = tk.Tk()
    rot.overrideredirect(True)         # 隐藏窗口的标题栏
    rot.attributes("-alpha", 0.1)      # 窗口透明度10%
    rot.geometry("{0}x{1}+0+0".format(rot.winfo_screenwidth(), rot.winfo_screenheight()))
    rot.configure(bg="black")

    cv = tk.Canvas(rot)
    canvas = tk.Canvas(rot)
    canvas.configure(width=300)
    canvas.configure(height=100)
    canvas.configure(bg="yellow")
    canvas.configure(highlightthickness=0)  # 高亮厚度
    canvas.place(x=(rot.winfo_screenwidth()-500),y=(rot.winfo_screenheight()-300))
    canvas.create_text(150, 50,font='Arial -20 bold',text='ESC退出')
    # 绑定事件
    canvas.bind("<B1-Motion>", move)   # 鼠标左键移动->显示当前光标位置
    rot.bind('<Escape>',sys_out)      # 键盘Esc键->退出
    rot.bind("<Button-1>", button_1)  # 鼠标左键点击->显示子窗口 
    rot.bind("<B1-Motion>", b1_Motion)# 鼠标左键移动->改变子窗口大小
    rot.bind("<ButtonRelease-1>", buttonRelease_1) # 鼠标左键释放->记录最后光标的位置
    rot.bind("<Button-3>",button_3)   #鼠标右键点击->截屏并保存图片
    #运行
    rot.mainloop()
    return full
    #rot.join()
if __name__=='__main__':
    if sys.argv[1:]:
        pass
        #run(sys.argv[1])
    else:
        run()
