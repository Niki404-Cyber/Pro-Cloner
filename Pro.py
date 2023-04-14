import os, sys
try:
    __import__("META").menu()
except Exception as e:
    exit(str(e))
