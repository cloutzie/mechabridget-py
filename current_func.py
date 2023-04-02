from datetime import datetime
import pandas as pd





def current(character):
    sheet_id = "1RzqqheHKMmwCbEM_gSTUep_S4hFu4ILMz__o0tjYPF0"
    sheet_name = "FEBRUARY-2023"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    col_names = ["turns", "celine", "chocolat", "fergus", "lenny", "lednas"]
    col_nums = [0,1,3,5,7,9]

    df = pd.read_csv(url, usecols= col_nums, names = col_names, skiprows=1)
    turns = range(1,df.count()['turns']+1)
    df['turns'] = turns
    df = df.dropna()
    
    
    event_start = datetime(2023, 2, 8, 19)
    current = datetime.now()
    elapsed = current - event_start
    seconds = elapsed.total_seconds()
    hours = divmod(seconds, 3600)[0]

    if character == 'round':
        return int(hours+1)
    
    else:
        return int(df[character][hours])
    


