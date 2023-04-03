
import matplotlib.pyplot as plt

import get_sheet as gs

# Backend for exponential moving average
def ema(character):

    # Get sheet data
    df = gs.sheet()

    # Price list
    price = df[character]

    # Get EMA
    def get_ema(prices, rate):
        return prices.ewm(span=rate, adjust=False).mean()
    ema = get_ema(price, 20) # Get 20 turn EMA

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

    # Plot points
    plt.title(str(character.replace(character[0], character[0].upper())) + ' EMA', color='white')
    plt.xlabel('Turns')
    plt.ylabel('Price')
    plt.plot(price, label=str(character.replace(character[0], character[0].upper())) + 'Price')
    plt.plot(ema, label='20 Turn EMA')
    plt.legend()
    
    plt.savefig(character+'.png', facecolor='#36393f')
    return (character+'.png')
