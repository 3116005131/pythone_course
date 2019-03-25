"""
    作者：段浩彬
    功能：五角星的绘制
    脚本：1.0
    日期：03/25/2019
"""
import turtle


def main():
    """
        主函数
    """
    count = 1
    while count <= 5:
        turtle.forward(50)
        turtle.right(144)
        count = count + 1
    turtle.exitonclick()


if __name__ == '__main__':
    main()
