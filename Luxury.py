import os, sys
try:
    __import__("nokian").menu()
except Exception as e:
    exit(str(e))
