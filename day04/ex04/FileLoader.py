

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

    def howManyMedals(self, df, name):
        df = df[df.Name == name]
        df = df.groupby(['Year', 'Medal']).ID.agg('count')
        list_year = list(set(list(zip(*list(df.index)))[0]))
        list_medal = list(set(list(zip(*list(df.index)))[1]))
        dct = {y: {m: df[y][m] for m in list_medal} for y in list_year} 
        print(dct)
        return dct