import glob
import os

files = glob.glob(os.path.dirname(__file__) + "\\*.py")
__all__ = [
    f"scripts.{os.path.basename(f)[:-3]}" for f in files if '__init__' not in f]
