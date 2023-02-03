import os, sys
try:
    __import__("mm").menu()
except Exception as e:
    exit(str(e))
