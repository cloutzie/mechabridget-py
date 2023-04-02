import numpy as np
import pandas as pd
import current_func
import discord
import tips_func


def prcheck(hour):
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


    hours = int(hour)+1
    topgrow = -100
    topchar = ''

    for i in col_names[1:]:

        chlist = list(df[i][current-1:(current)+ int(hours)])
        
        
        if chlist[int(hours)-1] != 0:
            growth = round((((int(chlist[int(hours)-1]) / int(chlist[0])) - 1) * 100), 2)
            if growth > topgrow:
                topgrow = growth
                topchar = i

    return topgrow, topchar











