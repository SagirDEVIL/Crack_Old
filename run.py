import os, sys
try:
    __import__("old").Main()
except Exception as e:
    exit(str(e))