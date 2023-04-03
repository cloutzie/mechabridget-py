
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# Create dataframe for use in other commands
def sheet():

    df = pd.read_csv(

        # URL
        filepath_or_buffer = f"https://docs.google.com/spreadsheets/d/{os.getenv('SHEET_ID')}/gviz/tq?tqx=out:csv&sheet={os.getenv('SHEET_NAME')}",

        # Specify columns
        usecols = [2, 7, 12, 17, 22],

        # Column headers
        names = ["celine", "chocolat", "fergus", "lenny", "lednas"],

        # Strip original headers
        skiprows = 1

    # Fill empty values with '0'
    ).fillna(0)

    # Begin index at 1 to equal round number
    df.index += 1 

    return df


