
import get_round as gr
import get_sheet as gs

# Backend for ;tips
def tips(character):

    # Get sheet data
    df = gs.sheet()

    # Get current round
    cr = gr.round()

    num = 0
    round = 0
    for i in range(cr+1, df.index[-1]):
        if df[character][i]:
            num = df[character][i]
            round = df.index[i-1]
            break
    
    return num, round


# Frontend for ;tips
def tips_output(character):

    # Get sheet data
    df = gs.sheet()

    # Get current round
    cr = gr.round()

    def tipstr(ch):

        num, rounds = tips(ch.lower())
        growth = round((((df[ch][cr+1] - df[ch][cr]) / df[ch][cr]) * 100), 2)

        string = ""
        if num:
            string += f"> {ch.capitalize()} will be {int(num)} on round {rounds}. A change of {growth}%\n"
        else:
            string += f"> No tips available for {ch.capitalize()}"
        
        return string

    match character:
        case 'all':
            string = ""
            for ch in ['celine', 'chocolat', 'fergus', 'lenny', 'lednas']:
                
                string += tipstr(ch)
                
        case _:

            string = tipstr(character)
        
    return string

