

import pandas
import matplotlib.pyplot as plt
import numpy
import xlrd

from os import system

import glob

path = 'c:\\Users\\Gui_S\\Desktop\\work\\Python\\Data'

files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

for f in files:
    pandas.read_excel(f,0).to_csv(f+'.csv', index=False)