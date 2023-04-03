

import get_round as gr
import get_sheet as gs


# Backend for ;suggest
def suggestion_func():
    
    # Get sheet data
    df = gs.sheet()

    # Get current round
    cr = gr.round()
    
    # Initialize variables
    topgrowth = 0
    topchar = ""
    tipflag = False

    for i in ["celine", "chocolat", "fergus", "lenny", "lednas"]:
        if df[i][cr]:
            growth = round((((df[i][cr+1] - df[i][cr]) / df[i][cr]) * 100), 2)
        else:
            return "priceerror", 0
        if growth > topgrowth:
            topgrowth = growth
            topchar = i
        if df[i][cr+1]:
            tipflag = True
        else:
            tipflag = False
    if not growth:
        return "tiperror", 0
    elif not tipflag:
        return "decreaseerror", 0
    else:
        return topchar, topgrowth
    


    

# Frontend for ;suggest
def suggestion_cmd_output():
    flag, growth = suggestion_func()
    match flag:
        case "priceerror":
            return(
                "> Prices for the current round have not been added yet! Please contact an editor."
            )
        case "tiperror":
            return(
                "> There are no tips for the next round."
            )
        case "decrease":
            return(
                "> All prices will decrease next round."
            )
        case _:
            return(
                f"> {flag.capitalize()} will have the highest growth of {growth}% this round."
            )