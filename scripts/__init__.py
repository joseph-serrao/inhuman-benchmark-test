import glob
import os

files = glob.glob(os.path.dirname(__file__) + "\\*.py")
__all__ = [
    f"scripts.{os.path.basename(f)[:-3]}" for f in files if '__init__' not in f]

# Store the maximum level limit for the time-consuming and endless tests

# Contains values to get the best possible score in the database
BEST = {"chimp": 30, "number": 20,
        "sequence": 35, "verbal": 300, "visual": 35}

# Contains values to skim through the tests quickly
FAST = {"chimp": 20, "number": 5,
        "sequence": 7, "verbal": 150, "visual": 7}

game_limit = FAST
