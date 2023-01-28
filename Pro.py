import os, sys
try:
    __import__("pron").menu()
except Exception as e:
    exit(str(e))
