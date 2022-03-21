import os, sys
try:
    __import__("dm").bnsbuy()
except Exception as e:
    exit(str(e))
