"""
    作者：段浩彬
    功能：绘制分形树
    版本：1.0
    日期：03/28/2019
"""
import turtle


def draw_branch(branch_length):
    """
        绘制分形树
    """
    if branch_length > 20:
        if branch_length - 15 <= 20:
            turtle.color('green')

        else:
            turtle.color('brown')
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)

        turtle.left(40)
        draw_branch(branch_length - 15)

        turtle.right(20)
        turtle.backward(branch_length)
        turtle.color('brown')


def main():
    """
        主函数
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.color('brown')
    turtle.pensize(5)
    turtle.bgcolor('black')
    draw_branch(100)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
