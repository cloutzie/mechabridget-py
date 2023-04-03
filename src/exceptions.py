
import get_round as gr
import get_sheet as gs

def currentcheck():

    # Get sheet data
    df = gs.sheet()

    # Get current round
    cr = gr.round()

    for i in ["celine", "chocolat", "fergus", "lenny", "lednas"]:

        if not df[i][cr]:
            return 1
        else:
            return 0