def howManyMedalsByCountry(df, country_name):
        df = df[df.Team == country_name]
        list_year = set(df.Year.to_list())
        # df =df[df.Medal.notnull()]
        df["CountMedal"] = 1
        df = df.groupby(['Year', 'Medal', 'Sport']).CountMedal.agg('mean')
        df = df.reset_index()
        df2 = df.groupby(['Year', 'Medal']).CountMedal.agg('count')
        # list_year = list(set(list(zip(*list(df.index)))[0]))
        df = df2.reset_index()
        
        # list_medal = list(set(list(zip(*list(df.index)))[1]))
        # dct = {y: {m: df[y][m] for m in list_medal} for y in list_year}
        dct = {y: {m: df2[y][m] for m in [x for x in df.Medal[df.Year ==y]]} for y in list_year}
        print(dct)
        return dct