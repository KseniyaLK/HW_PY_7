# юзер интерфейс, модуль с кнопками для пользователя
import log

def view_data(data): # просто вывод данных, которые поступят к нам из model
    print (f'result = {data}')
    # log.loggi()



def get_value(): # метод получения данных из терминала
    return float(input('введите значение value = ')) 
       
