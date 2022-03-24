import os, sys
try:
    __import__("zsb").bnsbuy()
except Exception as e:
    exit(str(e))
