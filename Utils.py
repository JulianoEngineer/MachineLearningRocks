import numpy as np
import pickle
import glue as gl
import glob as gb
import os

class utils(object):

    def __init__(self):  
        pass
    
    def GetLastPickle(self):
        list_of_files = gb.glob('dataframes/*')
        latest_file = max(list_of_files, key = os.path.getctime)
        dataframe = []
        with (open(latest_file,"rb")) as openfile:
            while True:
                try:
                    dataframe.append(pickle.load(openfile))
                except EOFError:
                    break
            
        return dataframe[0]