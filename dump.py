import os, sys
try:
    __import__("dm").prodan()
except Exception as e:
    exit(str(e))
