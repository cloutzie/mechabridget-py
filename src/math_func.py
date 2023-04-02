import numpy as np
import pandas as pd
import current_func
import discord


def math(function, character, rounds):
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

    current = current_func.current('round')

    if function in ['average', 'avg', 'mean']:
        if rounds in ['all', 'max']:
            avg = int(df[character].mean())
            return '> ' + str(character.capitalize()) + ' ' + str(rounds.replace(rounds[0], rounds[0].upper())) + ' Round Average is ' + str(avg)
        else:
            avg = int(df[character][current-int(rounds):current].mean())
            return '> ' + str(character.capitalize()) + ' ' + str(rounds) + ' Round Average is ' + str(avg)

            
    elif function in ['spread', 'range', 'minmax']:
        if rounds in ['all' or 'max']:
            min = df[character].min()
            max = df[character].max()
            return "> Min = " + str(int(min))+", Max = "+ str(int(max))
        else:
            min = df[character][current-int(rounds):current].min()
            max = df[character][current-int(rounds):current].max()
            return "> Min = " + str(int(min))+", Max = "+ str(int(max))

    elif function in ['stddev', 'sdev', 'standard deviation']:
        if rounds in ['all', 'max']:
            stddev = df[character].std()
            return '> All Time Standard Deviation of ' + str(character.capitalize()) + ' is ' + str(int(stddev))
        else:
            stddev = df[character][current-int(rounds):current].std()
            return '> ' + str(rounds) + ' Round Standard Deviation of ' + str(character.capitalize()) + ' is ' + str(int(stddev))