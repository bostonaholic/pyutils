"""
    author: mboston
"""

import fnmatch
import os

class FileUtils():

    def __init__(self):
        pass

def findFileName(dir, pattern):
    files = os.listdir(dir)
    for name in files:
        if(fnmatch.fnmatch(name, pattern)):
            return name

def main ():
    pass

if __name__ == '__main__': main()
