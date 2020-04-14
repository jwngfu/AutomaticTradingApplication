import readfile
import timefunction as tm
import order

order_time = []

f = readfile.read(input('Enter the path: '))

#Place Order
def placeOrder():
    for cell in f:
        #Place order
        order.place(cell[5],cell[7], cell[4], 123, 1234) #testing only
        #Records the order time in timestamp format
        order_time.append(tm.now())
    print("\n")
    print(order_time)

#monitor order
def monitor(i):
    pass

#confirm order
def confirmOrder(i):
    while order.status() != 1:
        if tm.difference(order_time) >= f[i][9]:
            print("Timeout. Cancel the order.")
            break
    if order.status() == 1:
        monitor(i)

def main():
    placeOrder()
    confirmOrder(1) #testing only

if __name__ == "__main__":
    main()
