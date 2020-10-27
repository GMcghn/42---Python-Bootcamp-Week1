class SpatioTemporalData:

    def __init__(self, dff):
        self.dataf = dff
        



    def when(self, location):
        df_when = self.dataf[self.dataf.City == location]
        x = set(df_when.Year)
        print(x)
        return x

    def where(self, date):
        df_where = self.dataf[self.dataf.Year == date]
        x = set(df_where.City)
        print(x)
        return x