"""
    作者：段浩彬
    功能：五角星的绘制
    脚本：1.0
    日期：03/25/2019
"""
import turtle


def draw_pentagram(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    size += 10
    if size <= 100:
        draw_pentagram(size)


def main():
    """
        主函数
    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')
    size = 50
    draw_pentagram(size)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
