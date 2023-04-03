
import matplotlib.pyplot as plt

import get_sheet as gs

# Backend for simple moving average
def sma(character):

    # Get sheet data
    df = gs.sheet()

    # Get price list
    price = df[character] 

    # Get SMA
    def get_sma(prices, rate):
        return prices.rolling(rate).mean()
    sma = get_sma(price, 20) # Get 20 day SMA

    # Set up graph
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

    # Plot the graph
    plt.title(str(character.replace(character[0], character[0].upper())) + ' SMA', color='white')
    plt.xlabel('Turns')
    plt.ylabel('Price')
    plt.plot(price, label=str(character.replace(character[0], character[0].upper())) + 'Price')
    plt.plot(sma, label='20 Turn SMA')
    plt.legend()

    plt.savefig(character+'.png', facecolor='#36393f')
    return (character+'.png')


