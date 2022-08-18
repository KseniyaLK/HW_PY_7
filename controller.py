import rational_num as rat
import log as l
import view

#метод нажатия на кнопку
def button_click():
    print('Вас приветсвует калькулятор!\nВыберите необходимый пункт меню: ')
    print('1. Подсчет с рациональными числами')
    print('2. Просмотр логирования')
    print('3. Выход из программы')
    status = False
    while status != True:
        k = input('введите пункт меню: ')
        if  k == '1':
            value_a = view.get_value()
            value_b = view.get_value()
            rat.init(value_a, value_b) # инициализация входных данных
            result =  rat.calk()
            view.view_data(result)# возврат значения в view
            status = False
        elif k == '2':  
            result = l.loggi()
            view.view_data(result)# возврат значения в view
            status = False
        elif k == '3':  
            break
        else:    
            print ('Некорректный ввод. Введите число от 1 до 3')
    return result    


   
