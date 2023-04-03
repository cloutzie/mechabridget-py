
import get_round as gr
import get_sheet as gs

def last(rounds, character):

    # Get sheet data
    df = gs.sheet()

    # Get current round
    cr = gr.round()

    # Create range for table
    all_rounds = df[character][cr-(int(rounds)+1):cr]
    # Initialize variables
    growth = ''
    turn = ''
    num = ''
    table = '```ansi\n╔══════════╦══════════╦══════════╗\n║' + ('Turn #').center(10) + '║' + ('Price').center(10) + '║' + ('Growth').center(10) + '║\n╠══════════╬══════════╬══════════╣\n'

    # Code to make a janky but workable table in discord maybe will comment later
    for r in all_rounds.index[1:]: 
        growth = round(((all_rounds[r] / all_rounds[r-1] - 1) * 100), 2)
        if growth > 0:
            form = '\u001b[0;32m'
        elif growth < 0:
            form = '\u001b[0;31m'
        elif growth == 0:
            form = '\u001b[0;33m'
        growth = str(growth) + ' %'
        turn = str('Turn ' + str(r))
        num = str(int(all_rounds[r]))
        table += '║' + str(turn).center(10) + '║' + str(num).center(10) + '║' + form + str(growth).center(10) + '\u001b[0m' + '║ \n╠══════════╬══════════╬══════════╣\n'

    table = table[:-35] + '╚══════════╩══════════╩══════════╝\n```'

    return table
