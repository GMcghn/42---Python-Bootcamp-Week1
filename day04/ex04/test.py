from FileLoader import FileLoader
loader = FileLoader()



path2 = r"C:\Users\Gabriel\Desktop\Mes documents - Google Drive\DATA\19\day04\athlete_events.csv"
data = loader.load(path2)

from SpatioTemporalData import SpatioTemporalData
sp = SpatioTemporalData(data)
sp.where(1896)

sp.where(2016)

sp.when('Athina')

sp.when('Paris')
