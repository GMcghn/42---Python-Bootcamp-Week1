import pandas as pd
from YoungestFellah import youngestFellah
from FileLoader2 import FileLoader2



fl2 = FileLoader2()
path3 = r"C:\Users\Gabriel\Desktop\Mes documents - Google Drive\DATA\19\day04\athlete_events.csv"
df = fl2.load(path3)




youngestFellah(path3, 1994)