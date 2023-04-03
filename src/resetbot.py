import dotenv
import os

import counter

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def resetrr(timestamp, sheet):
    os.environ["START"] = timestamp
    os.environ["SHEET"] = sheet
    counter.resetcounter()