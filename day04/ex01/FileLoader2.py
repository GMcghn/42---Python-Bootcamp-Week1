

class FileLoader2:

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

    def youngestFellah(self, csv, y):
        import pandas as pd
        df = pd.read_csv(csv)
        df = df[df.Year==y]
        M = df[df.Sex == 'M'].Age.min()
        F = df[df.Sex == 'F'].Age.min()
        dct = {"M":[], "F":[]}
        dct['M'] = M
        dct['F'] = F
        print(dct)