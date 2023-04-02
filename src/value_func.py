import numpy as np
import pandas as pd
import current_func
import discord
import tips_func




def value():
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
    
    
    under = []
    fair = []
    over = []
    table = '```ansi\n╔══════════╦══════════╦══════════╗\n║' + ('Good').center(10) + '║' + ('Fair').center(10) + '║' + ('Bad').center(10) + '║\n╠══════════╬══════════╬══════════╣\n'

    for i in col_names[1:]:
        flag = valfind(i)
        if flag == 0:
            under.append(i.capitalize())
        elif flag ==1:
            over.append(i.capitalize())
        else:
            fair.append(i.capitalize())
    listof = [under, fair, over]
    bigg = len(max(listof, key=len))
    while len(under) != bigg:
        under.append('')
    while len(fair) != bigg:
        fair.append('')
    while len(over) != bigg:
        over.append('')
    for num in range(bigg):
        
        table += '║' + str(under[num]).center(10) + '║' + str(fair[num]).center(10) + '║' + str(over[num]).center(10) + '║ \n'
    table += '╚══════════╩══════════╩══════════╝\n```'
    return table
        





def valfind(character):
    sheet_id = "1RzqqheHKMmwCbEM_gSTUep_S4hFu4ILMz__o0tjYPF0"
    sheet_name = "AUGUST-2022"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    col_names = ["turns", "celine", "chocolat", "fergus", "lenny", "lednas"]
    col_nums = [0,1,3,5,7,9]

    df = pd.read_csv(url, usecols= col_nums, names = col_names, skiprows=1)
    turns = range(1,df.count()['turns']+1)
    df['turns'] = turns
    df = df.fillna(0)
    df

    current = current_func.current('round')
    chlist = df[character][current-7:current]
        
    avg = chlist.mean()
    stdev = chlist.std()
    currentpr = current_func.current(character)
    if (currentpr < (int(avg) - int(stdev))):
        return 0

    elif (currentpr > (int(avg) + int(stdev))):
        return 1

    else:
        return 2
