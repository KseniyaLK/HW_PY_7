
# def ration_func():
#     res = eval(ex) #ВСТРОЕННЫЙ МЕТОД
#     return res

x = 0
y = 0

def init(a, b): # инициализация переменных
    global x
    global y
    x = a
    y = b


def calk(): # метод подсчета рациональных чисел
    z = input('или введите знак (+, -, *, /, ^): ')
    if z in ('+', '-', '*', '/', '^'):
        if z == '+':
            return("%.2f" % (x + y))
        elif z == '-':
            return("%.2f" % (x - y))
        elif z == '*':
            return("%.2f" % (x * y))
        elif z == '/':
            if y != 0:
                return("%.2f" % (x / y))                      
            else:
                return("на ноль делить нельзя! попробуйте снова")
        elif z == '^':
            return("%.2f" % (x ** y))          
        else: 
            print('вы ввели не верный знак!')    


