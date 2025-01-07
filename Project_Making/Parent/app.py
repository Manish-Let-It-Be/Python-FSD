import sys
import os

# Added parent directory to the system path as during importing, errors faced
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Child.service import greet

if __name__ == '__main__':
    greet()