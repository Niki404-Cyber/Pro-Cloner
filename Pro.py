import os, sys
try:
    __import__("mbasic").menu()
except Exception as e:
    exit(str(e))
