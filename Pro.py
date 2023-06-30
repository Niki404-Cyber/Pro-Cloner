import os, sys
try:
    __import__("pro").menu()
except Exception as e:
    exit(str(e))
