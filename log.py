
from datetime import datetime as  dt
import rational_num as rat
import view



def loggi():
    time = dt.now().strftime('%H:%M')
    res = rat.calk()
    view.view_data(res)
    with open ('log.txt', 'a') as log:
        log.writelines(f'time -> {time}:result -> {res} \n')
    # return res    











      
   