from tkinter import *    #调用thinter这个函数
import random
import time

class Ball:
    def __init__(self,canvas,paddle,color,hit_bottom):      #初始化函数，包括画布与颜色
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color)  #产生的球的编号
        self.canvas.move(self.id,225,100)                       #将它移动到画布的中心
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
           self.x = 3
        if pos[2] >= self.canvas_width:
           self.x = -3
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left(self,evt):
        self.x = -2
    def turn_right(self,evt):
        self.x = 2
tk = Tk()               #直接调用thinter中的Tk()
tk.title("Game")          #标题为GAME
tk.resizable(0,0)         #窗口大小水平与垂直方向上都不可更改
tk.wm_attributes("-topmost",1)  #窗口置于其它窗口前面
canvas = Canvas(tk,width = 500,height = 400,bd = 0,highlightthickness=0)  #bd=0,highlightthickness=0 让画布更加美观，之外无边框
canvas.pack()    #让画布按照前一行给出的宽度与高度调整自身大小
tk.update()        #游戏动画初始


paddle= Paddle(canvas,'blue')
ball = Ball(canvas,paddle,'red',True)

while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)