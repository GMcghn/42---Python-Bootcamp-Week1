# https://www.geeksforgeeks.org/context-manager-in-python/
# You could use dir(f) to see all the methods of file object.
# Forbidden functionw : None (la fonction None)

class CsvReader():
    import pandas as pd
    import csv
    

    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        import sys
        self.filename = filename
        # Je déclare juste (normalement None est interdit mais c'est pas concerné je pense, j'aurais pu mettre 0)
        self.file = None
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.corrupted = False

        

    def __enter__(self):
        # __init__ is called when the object is created, __enter__ when it is entered 
        # with with statement, and these are 2 quite distinct things. Often it is so 
        # that the constructor is directly called in with initialization, with no intervening code, 
        # but this doesn't have to be the case.
        import sys
        try:
            # check corruption
            with open(self.filename) as f:
                import csv
                reader = csv.reader(f)
                list_reader = list(reader)
                lines = len(list_reader)
                sizex = len(str(list_reader[0]).split(','))
                
                for x in range(lines):
                    sizey = len(str(list_reader[x]).split(','))
                    if sizey > sizex:
                        print("ERROR : file corrupted (at least one line with too many elements)")
                        self.corrupted = True
                        return self
        except FileNotFoundError:
            print("ERROR: are you sure the file exists and is in the right directory ?")   
            sys.exit(1)






        if self.corrupted == True:
            return None
        else:
            return self


       

    # __exit__ must accept 3 arguments: type, value, traceback
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file = open(self.filename)
        self.file.close()

    
    def getdata(self):
        import csv
        import pandas as pd
        if self.corrupted == False:

            self.file = open(self.filename)
            
           
            list_r = self.file.readlines()
            
            length = len(list_r)
           
            
            list_x = list_r[self.skip_top : (length - self.skip_bottom)]
            return list_x
            # for x in list_x:
            #     print(x.replace('\n', ''))
            
         
        

    def getheader(self):
        
        if self.corrupted == False:

            self.file = open(self.filename)
            if self.header == True:
                return self.file.readline()
            else:
                print("No header.")
        