import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import current_func







def lsr(character):
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
    
    price = df[character]
    turns = df['turns']

    X = turns.values.reshape(-1, 1)
    Y = price.values.reshape(-1, 1)

    model = LinearRegression()
    model.fit(X, Y)
    lsr = model.predict(X)

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

    

    plt.title(str(character.capitalize()) + ' LSR', color='white')
    plt.xlabel('Turns')
    plt.ylabel('Price')
    plt.plot(price, label=str(character.capitalize()) + 'Price')
    plt.plot(X, lsr, label='Best Fit')
    plt.legend()
    
    plt.savefig(character+'.png', facecolor='#36393f')
    return (character+'.png')

