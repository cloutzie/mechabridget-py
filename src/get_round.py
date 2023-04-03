
from dotenv import load_dotenv
import os
import time

load_dotenv()

# ;round
def round():

    # Determine the current round
    round=((time.time() - int(os.getenv("START"))) // 3600) + 1
    
    return int(round)

def roundstr():

    return f"> The current round is {round()}"
