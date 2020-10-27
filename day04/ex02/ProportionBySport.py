
def proportionBySport(self, df, year, sport, gender):

    df = df[df.Year == year]
    df = df[df.Sex == gender]
    x = len(df[df.Sport == sport])/len(df)
    print(x)