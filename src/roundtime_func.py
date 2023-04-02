import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import current_func
from datetime import datetime
import time



sheet_id = "1RzqqheHKMmwCbEM_gSTUep_S4hFu4ILMz__o0tjYPF0"
sheet_name = "FEBRUARY-2023"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
col_names = ["turns", "celine", "chocolat", "fergus", "lenny", "lednas"]
col_nums = [0,1,3,5,7,9]

df = pd.read_csv(url, usecols= col_nums, names = col_names, skiprows=1)
turns = range(1,df.count()['turns']+1)
df['turns'] = turns
df = df.dropna()[df['turns'] <= current_func.current('round')]
df


def roundtime(round):

        
    event_start = datetime(2023, 2, 8, 18)
    elapsed = int(round) * 3600
    untime = time.mktime(event_start.timetuple())


    total = int(untime) + int(elapsed)

    
    return total




