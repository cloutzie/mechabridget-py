
import get_round as gr
import get_sheet as gs

def currentcheck():

    # Get sheet data
    df = gs.sheet()

    # Get current round
    cr = gr.round()

    for i in ["celine", "chocolat", "fergus", "lenny", "lednas"]:

        if df[i][cr] == 0:
            return 1
        else:
            return 0