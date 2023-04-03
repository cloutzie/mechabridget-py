
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import get_sheet as gs


# Backend for Least Squared Regression Graph
def lsr(character):
    
    df = gs.sheet()
    
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

