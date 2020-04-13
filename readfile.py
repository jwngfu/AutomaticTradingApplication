import csv
from pandas import read_excel

rows = []

#Function to read CSV file
def readCsv(path):
    with open(path, 'r') as file:
        #reader is a csv reader object
        reader = csv.reader(file)
        #Skips the header row
        next(reader)
        for row in reader:
            rows.append(row)
    return rows

#Function to read Excel file
def readXls(path):
    print("Reading Excel file, Please wait.")
    data_xls = read_excel(path)
    data_xls.to_csv('temp.csv', encoding='utf-8',index=False)
    print("Copying data to temp.csv")
    return readCsv('temp.csv')

#Function to read the input file
def read(path):
    try:
        #try to read the file as csv
        return readCsv(path)
    except:
        try:
            #try to read the file as excel sheet
            return readXls(path)
        except:
            #returns negative if file cannot be read
            return -1

#main function for testing the script only, it wont run when imported
def main():
    path = str(input("Enter the path of the file and press enter: "))
    rws = read(path)
    if rws == -1:
        print("The File cannot be read.")
    else:
        for row in rws:
            for col in row:
                print("%1s"%col, end = " |")
            print("") #prints newline

if __name__ == "__main__":
    main()
