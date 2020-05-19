#利用turtle库画一组同心圆。用户输入最小圆的半径、画笔宽度和颜色

import turtle

radius = eval(input()) #接收用户输入的半径并转换成数值
number = eval(input())   #接收用户输入的画笔宽度并转换成数值
cl = input()           #接收用户输入的颜色

turtle.pencolor(cl)
turtle.goto(0,0)
for i in range(number):
    turtle.circle(radius)      #画圆
    radius=radius+20    #修改半径的值
    turtle.penup()             #抬起笔
    turtle.goto(0, -20*(i+1))     #移动到新的起点，下一个圆的最低点
    turtle.pendown()           #落笔
turtle.hideturtle()
turtle.done()
