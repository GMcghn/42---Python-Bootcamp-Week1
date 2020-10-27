from csvreader2 import CsvReader

if __name__ == "__main__":
    with CsvReader('good.csv', header = True) as file:
        data = file.getdata()
        header = file.getheader()
        print(data)
        print(header)
        



# a = CsvReader('good.csv')

# # a.getdata()
# print(a.getdata())
# print(a.getheader())
