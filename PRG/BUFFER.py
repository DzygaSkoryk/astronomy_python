common_path = '/home/dzyga/Docs/Work/Data/'

# Name of particular file:
filename = common_path + 'E220213_201439.jds' 



#*************************************************************
#                   IMPORT LIBRARIES                         *
#*************************************************************
import os
import struct
import numpy as np

#*************************************************************
#                       FUNCTIONS                            *
#*************************************************************

Dir = '/home/dzyga/Docs/Work/Data/'
Name = 'E220213_201439'
Format = 'jds'

FileName = os.path.join(Dir, Name + "." + Format)
#print(FileName)
FileName = [Dir+Name+'.'+Format]
#print(FileName)

#Dir_in = input('Input path to file: ')
#print(Dir_in)


def FileHeaderReaderDSP(FileName):
    

    
FileHeaderReaderDSP(FileName)    


