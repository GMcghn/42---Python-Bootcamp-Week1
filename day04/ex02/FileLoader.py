

class FileLoader:
   

    def load(self, path):
        import pandas as pd
        csv = pd.read_csv(path)
        # df = pd.DataFrame(x)
        print('('+ str(len(csv)) + ',' + str(len(csv.columns)) + ')')
        return csv

    def display(self, df, n):
        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(n))

    def proportionBySport(self, df, year, sport, gender):

        df = df[df.Year == year]
        df = df[df.Sex == gender]
        x = len(df[df.Sport == sport])/len(df)
        print(x)