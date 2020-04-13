#Used for dealing with time
from datetime import datetime, date, time

def now():
    #returns the current time as a timestamp
    return datetime.timestamp(datetime.now())

def difference(initialTime):
    #returns the tifference between the timestamps in minutes in float type
    return (datetime.timestamp(datetime.now())-initialTime)/60

#main() is for testing only
def main():
    print(now())

if __name__ == "__main__":
    main()
