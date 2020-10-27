import pandas as pd
from FileLoader import FileLoader

fl = FileLoader()
path2 = r"C:\Users\Gabriel\Desktop\Mes documents - Google Drive\DATA\19\day04\athlete_events.csv"
df = fl.load(path2)

dct = fl.howManyMedals(df, 'Juhamatti Tapio Aaltonen')
dct