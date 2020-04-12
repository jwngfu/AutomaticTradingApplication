import csv

rows = []

#Function to read CSV file
def read(path):
    with open(path, 'r') as file:
        #reader is a csv reader object
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    return rows

#main function for testing the script only, it wont run when imported
if __name__ == "__main__":
    #path = r'Bitmex Order History  2019-12-13.csv'
    path = str(input("Enter the path of the CSV file and press enter: "))
    rws = read(path)
    for row in rws:
        for col in row:
            print("%1s"%col, end = " |")
        print("") #prints newline
