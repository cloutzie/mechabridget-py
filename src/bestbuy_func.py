import numpy as np
import pandas as pd
import current_func
import discord
import tips_func



def bestbuy():
    sheet_id = "1RzqqheHKMmwCbEM_gSTUep_S4hFu4ILMz__o0tjYPF0"
    sheet_name = "FEBRUARY-2023"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    col_names = ["turns", "celine", "chocolat", "fergus", "lenny", "lednas"]
    col_nums = [0,1,3,5,7,9]

    df = pd.read_csv(url, usecols= col_nums, names = col_names, skiprows=1)
    turns = range(1,df.count()['turns']+1)
    df['turns'] = turns
    df = df.fillna(0)
    df
    current = current_func.current('round')
    
    topgrow = -100
    topchar = ''
    oneval = 0
    twoval = 0
    diff = 0
    
    for i in col_names[1:]:
        if ((int(df[i][current])) != 0):
            growth = round((((int(df[i][current])) / (int(df[i][current-1])) - 1) * 100), 2)
            if growth > topgrow:
                topgrow = growth
                topchar = i
                oneval = (int(df[i][current]))
                twoval = (int(df[i][current-1]))
                diff = (int(df[i][current])) - (int(df[i][current-1]))
    return topgrow, topchar, oneval, twoval, diff
