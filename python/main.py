import sys
import os

# Pyhton anti-design pattern: Add files directly to the PYTHONPATH
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.search.binary_search import binary_search  # noqa
from src.search.linear_search import linear_search  # noqa
