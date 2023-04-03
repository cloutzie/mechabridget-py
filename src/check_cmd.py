
import get_round as gr
import get_sheet as gs



def prcheck(hour):

    # Get sheet data
    df = gs.sheet()

    # Get current round
    cr = gr.round()

    topgrowth = 0
    topchar = ''

    for i in ["celine", "chocolat", "fergus", "lenny", "lednas"]:
        growth = round((((df[i][cr+int(hour)] - df[i][cr]) / df[i][cr]) * 100), 2)
        if growth > topgrowth:
            topgrowth = growth
            topchar = i
        if df[i][cr+int(hour)]:
            tipflag = True

    if tipflag and (topgrowth < 0):
        return "decreaseerror", 0
    elif not tipflag:
        return "tiperror", 0
    else:
        return topchar, topgrowth



# Frontend for ;suggest
def check_output(hour):
    # Get current round
    cr = gr.round()

    flag, growth = prcheck(hour)
    match flag:

        case "tiperror":
            return(
                "> There are no tips for the next round."
            )
        
        case "decreaseerror":
            return(
                f"> All characters with tips will decrease in {hour} rounds."
            )
        
        case _:
            return(
                f"> {flag.capitalize()} will have the highest growth of {growth}% by round {hour+cr}"
            )





