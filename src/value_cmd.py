
import get_round as gr
import get_sheet as gs






def value():
    
    under = []
    fair = []
    over = []
    table = '```ansi\n╔══════════╦══════════╦══════════╗\n║' + ('Good').center(10) + '║' + ('Fair').center(10) + '║' + ('Bad').center(10) + '║\n╠══════════╬══════════╬══════════╣\n'

    for i in ['celine', 'chocolat', 'fergus', 'lenny', 'lednas']:
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
    # Get sheet data
    df = gs.sheet()

    # Get current round
    cr = gr.round()

    chlist = df[character][cr-7:cr]
        
    avg = chlist.mean()
    stdev = chlist.std()
    currentpr = df[character][cr]
    if (currentpr < (int(avg) - int(stdev))):
        return 0

    elif (currentpr > (int(avg) + int(stdev))):
        return 1

    else:
        return 2
