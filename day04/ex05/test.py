from FileLoader import FileLoader
loader = FileLoader()



path2 = r"C:\Users\Gabriel\Desktop\Mes documents - Google Drive\DATA\19\day04\athlete_events.csv"
data = loader.load(path2)

from HowManyMedalsByCountry import howManyMedalsByCountry
howManyMedalsByCountry(data, 'Greece')
