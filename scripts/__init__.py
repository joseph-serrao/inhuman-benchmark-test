import glob
import os

files = glob.glob(os.path.dirname(__file__) + "\\*.py")
__all__ = [
    f"scripts.{os.path.basename(f)[:-3]}" for f in files if '__init__' not in f]

# Store the maximum level limit for the time-consuming and endless tests

# Contains values to get the best possible score in the database
BEST = {"chimp_test": 30, "number_memory": 20,
        "sequence_memory": 35, "verbal_memory": 300, "visual_memory": 35}

# Contains values to skim through the tests quickly
FAST = {"chimp_test": 10, "number_memory": 5,
        "sequence_memory": 10, "verbal_memory": 100, "visual_memory": 10}

game_level_limit = BEST
