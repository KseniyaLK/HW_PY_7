# юзер интерфейс, модуль с кнопками для пользователя

def view_data(data): # просто вывод данных, которые поступят к нам из model
    print (f'result = {data}')


def get_value(): # метод получения данных из терминала
    return float(input('введите значение value = '))    
