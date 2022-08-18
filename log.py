
from datetime import datetime as  dt
import rational_num as rat

# now = datetime.datetime.now()
def loggi(data):
    time = dt.now().strftime('%H^%M')
    with open ('log.txt', 'a') as log:
        log.writelines('{}; result; {}'
                        .format(time, data))


# def loggi_view (sensor):
#     data = rat.calk(sensor)
#     loggi(data)
#     return data







      
   