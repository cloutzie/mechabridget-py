import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import current_func





def ema(character):

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
    def get_ema(prices, rate):
        return prices.ewm(span=rate, adjust=False).mean()
    
    price = df[character]

    ema = get_ema(price, 20) # Get 20 turn EMA

    # Axes
    plt.cla()
    plt.clf()
    ax = plt.axes()
    ax.set_facecolor('#36393f')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')

    # Plot

    plt.title(str(character.replace(character[0], character[0].upper())) + ' EMA', color='white')
    plt.xlabel('Turns')
    plt.ylabel('Price')
    plt.plot(price, label=str(character.replace(character[0], character[0].upper())) + 'Price')
    plt.plot(ema, label='20 Turn EMA')
    plt.legend()
    
    plt.savefig(character+'.png', facecolor='#36393f')
    return (character+'.png')
