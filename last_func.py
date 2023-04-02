import numpy as np
import pandas as pd
import current_func
import discord
import dataframe_image as dfi
import six
import matplotlib.pyplot as plt






def last(rounds, character):
    sheet_id = "1RzqqheHKMmwCbEM_gSTUep_S4hFu4ILMz__o0tjYPF0"
    sheet_name = "FEBRUARY-2023"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    col_names = ["turns", "celine", "chocolat", "fergus", "lenny", "lednas"]
    col_nums = [0,1,3,5,7,9]

    df = pd.read_csv(url, usecols= col_nums, names = col_names, skiprows=1)
    turns = range(1,df.count()['turns']+1)
    df['turns'] = turns

    df
    current = current_func.current('round')
    all_rounds = df[character][current-(int(rounds)+1):current]
    growth = ''
    turn = ''
    num = ''
    bord = '║'
    table = '```ansi\n╔══════════╦══════════╦══════════╗\n║' + ('Turn #').center(10) + '║' + ('Price').center(10) + '║' + ('Growth').center(10) + '║\n╠══════════╬══════════╬══════════╣\n'
    for r in all_rounds.index[1:]: 
        growth = round(((all_rounds[r] / all_rounds[r-1] - 1) * 100), 2)
        if growth > 0:
            form = '\u001b[0;32m'
        elif growth < 0:
            form = '\u001b[0;31m'
        elif growth == 0:
            form = '\u001b[0;33m'
        growth = str(growth) + ' %'
        turn = str('Turn ' + str(r+1))
        num = str(int(all_rounds[r]))
        table += '║' + str(turn).center(10) + '║' + str(num).center(10) + '║' + form + str(growth).center(10) + '\u001b[0m' + '║ \n╠══════════╬══════════╬══════════╣\n'

    table = table[:-35] + '╚══════════╩══════════╩══════════╝\n```'
    return table


