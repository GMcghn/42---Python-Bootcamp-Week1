def youngestFellah(csv, y):
    import pandas as pd
    df = pd.read_csv(csv)
    df = df[df.Year==y]
    M = df[df.Sex == 'M'].Age.min()
    F = df[df.Sex == 'F'].Age.min()
    dct = {"M":[], "F":[]}
    dct['M'] = M
    dct['F'] = F
    print(dct)
