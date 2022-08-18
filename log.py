
from datetime import datetime as  dt
import rational_num as rat


def loggi():
    time = dt.now().strftime('%H%M')
    res =rat.calk() 
    with open ('log.txt', 'a') as log:
        log.writelines(f'{time} {res}\n')




# def loggi_view (sensor):
#     data = rat.calk(sensor)
#     loggi(data)
#     return data







      
   