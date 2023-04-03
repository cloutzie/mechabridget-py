
import get_round as gr
import get_sheet as gs



def next(rounds, character):
    
    # Get sheet data
    df = gs.sheet()

    # Get current round
    cr = gr.round()

    # Initialize variables
    all_rounds = df[character][cr:cr+(int(rounds) -1)]
    growth = ''
    turn = ''
    num = ''
    table = '```ansi\n╔══════════╦══════════╦══════════╗\n║' + ('Turn #').center(10) + '║' + ('Price').center(10) + '║' + ('Growth').center(10) + '║\n╠══════════╬══════════╬══════════╣\n'

    # Comment later maybe
    for r in all_rounds.index[1:]: 
        

        if all_rounds[r] != 0:
            growth = round(((all_rounds[r] / all_rounds[r-1] - 1) * 100), 2)
            if growth > 0:
                form = '\u001b[0;32m'
                growth = str(growth) + ' %'
            elif growth < 0:
                form = '\u001b[0;31m'
                growth = str(growth) + ' %'
            elif growth == 0:
                form = '\u001b[0;33m'
                growth = str(growth) + ' %'
            
            num = str(int(all_rounds[r]))
        else:
            growth = ''
            num = ''
            form = ''
        if all_rounds[r-1] == 0:
            growth = ''
        
        
        
        
        turn = str('Turn ' + str(r+1))
        table += '║' + str(turn).center(10) + '║' + str(num).center(10) + '║' + form + str(growth).center(10) + '\u001b[0m' + '║ \n╠══════════╬══════════╬══════════╣\n'

    table = table[:-35] + '╚══════════╩══════════╩══════════╝\n```'
    return table

