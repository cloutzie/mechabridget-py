import pandas as pd
import current_func
from datetime import datetime
import time
import sheet_hook as sh








def roundtime(round):

        
    event_start = datetime(2023, 2, 8, 18)
    elapsed = int(round) * 3600
    untime = time.mktime(event_start.timetuple())


    total = int(untime) + int(elapsed)

    
    return total




