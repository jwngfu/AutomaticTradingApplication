#Suppoting programs
import readfile
import timefunction as tm
import order

#Library
from threading import Thread

#Variables
order_time = []
threads = []

#Attempt to read the input file
try:
    f = readfile.read(input('Enter the path: '))
    number_of_rows = len(list(f))
except:
    print("Sorry, the input file couldn't be opened.")
    exit(0)

#Place Order
def placeOrder():
    for cell in f:
        #Place order
        #Cell number starts from zero
        order.place(cell[5],cell[7], cell[4], 123, 1234)
        #Records the order time in timestamp format
        order_time.append(tm.now())
    print("\n")
    print(order_time)

#monitor order
def monitor(i):
    print("Monitoring order number", i+1) #testing

#confirm order
def confirmOrder(i):
    while order.status() != 1:
        if tm.difference(order_time) >= f[i][9]:
            print("Timeout. Cancel the order.")
            break
    if order.status() == 1:
        monitor(i)

def main():
    #Print the number of orders to work with
    print("Number of orders in the file : ", number_of_rows)

    #Place the Order
    placeOrder()
    
    #Attemp the order
    for row in range(number_of_rows):
        #Multithreading to monitor multiple orders simultaneously
        process = Thread(target=confirmOrder, args=(row,))
        process.start()
        threads.append(process)
    
    #joining the threads before exiting main()
    for process in threads:
        process.join()

if __name__ == "__main__":
    main()
